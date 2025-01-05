

def run_gate(gate: str, inputs: dict[str, int]):
    left_input, operator, right_input, _, output = gate.split(" ")
    if left_input not in inputs or right_input not in inputs:
        return False
    match operator:
        case "AND":
            inputs[output] = inputs[left_input] & inputs[right_input]
        case "OR":
            inputs[output] = inputs[left_input] | inputs[right_input]
        case "XOR":
            inputs[output] = inputs[left_input] ^ inputs[right_input]
        case _:
            raise NotImplementedError(f"Operator {operator} not implemented")
    return True

def find_output_wire(a: str, b: str, operator: str, gates: list[str]):
    search = f"{a} {operator} {b}"
    search2 = f"{b} {operator} {a}"

    for gate in gates:
        if (search in gate) or (search2 in gate):
            return gate.split(" -> ")[1]


def swap_wires(a: str, b: str, gates: list[str]):
    new_gates = []

    for gate in gates:
        lhs, rhs = gate.split(" -> ")

        if rhs == a:
            new_gates.append(f"{lhs} -> {b}")
        elif rhs == b:
            new_gates.append(f"{lhs} -> {a}")
        else:
            new_gates.append(gate)

    return new_gates


def get_swaps(gates: list[str]):
    carry_wire = None
    swaps = []
    bit = 0

    while bit < 45:
        x = f"x{bit:02}"
        y = f"y{bit:02}"
        z = f"z{bit:02}"

        if bit == 0:
            carry_wire = find_output_wire(x, y, "AND", gates)
        else:
            xy_xor_wire = find_output_wire(x, y, "XOR", gates)
            xy_and_wire = find_output_wire(x, y, "AND", gates)

            assert (
                xy_xor_wire is not None
                and xy_and_wire is not None
                and carry_wire is not None
            )

            xy_carry_xor_wire = find_output_wire(carry_wire, xy_xor_wire, "XOR", gates)

            # If need to swap wires, check new gates from start

            # Swap x XOR y and x AND y
            if xy_carry_xor_wire is None:
                swaps.append(xy_xor_wire)
                swaps.append(xy_and_wire)
                gates = swap_wires(xy_xor_wire, xy_and_wire, gates)
                bit = 0
                continue

            # Swap x XOR y and z
            if xy_carry_xor_wire != z:
                swaps.append(xy_carry_xor_wire)
                swaps.append(z)
                gates = swap_wires(xy_carry_xor_wire, z, gates)
                bit = 0
                continue

            xy_carry_and_wire = find_output_wire(xy_xor_wire, carry_wire, "AND", gates)

            assert xy_carry_and_wire is not None

            carry_wire = find_output_wire(xy_and_wire, xy_carry_and_wire, "OR", gates)

        bit += 1

    return swaps