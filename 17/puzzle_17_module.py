Registers = dict[str, int]

def execute_instructions(registers: Registers, program: list[int]):
    instruction_pointer = 0
    outs = []
    instructions = {
        0: adv,
        1: bxl,
        2: bst,
        3: jnz,
        4: bxc,
        5: out,
        6: bdv,
        7: cdv,
    }

    while instruction_pointer < len(program):
        instruction = program[instruction_pointer]
        operand = program[instruction_pointer + 1]
        instruction_fn = instructions[instruction]

        if instruction == 3:
            res = jnz(registers, operand)
            if res != -1:
                instruction_pointer = res
                continue

        output = instruction_fn(registers, operand)
        if instruction == 5:
            outs.append(output)

        instruction_pointer += 2

    return outs

def adv(registers: Registers, operand: int):
    numerator = registers["A"]
    divisor = get_combo_value(registers, operand)
    registers["A"] = numerator // pow(2, divisor)


def bxl(registers: Registers, operand: int):
    registers["B"] = registers["B"] ^ operand


def bst(registers: Registers, operand: int):
    value = get_combo_value(registers, operand)
    registers["B"] = value % 8


def jnz(registers: Registers, operand: int) -> int:
    if registers["A"] == 0:
        return -1
    return operand


def bxc(registers: Registers, _):
    registers["B"] = registers["B"] ^ registers["C"]


def out(registers: Registers, operand: int) -> int:
    value = get_combo_value(registers, operand)
    return value % 8


def bdv(registers: Registers, operand: int):
    numerator = registers["A"]
    divisor = get_combo_value(registers, operand)
    registers["B"] = numerator // pow(2, divisor)


def cdv(registers: Registers, operand: int):
    numerator = registers["A"]
    divisor = get_combo_value(registers, operand)
    registers["C"] = numerator // pow(2, divisor)

def get_combo_value(registers: Registers, operand: int) -> int:
    value = -1
    if operand in {0, 1, 2, 3}:
        value = operand
    match operand:
        case 4:
            value = registers["A"]
        case 5:
            value = registers["B"]
        case 6:
            value = registers["C"]
        case 7:
            raise ValueError("Invalid combo operand")
    return value

def find_quine(program: list[int], registers: Registers) -> int:
    queue = [(len(program) - 1, 0)]

    while queue:
        # Want to find smallest quine value, so pop from the front
        offset, value = queue.pop(0)
        for i in range(8):
            # Try all possible 3-bit values
            new_value = (value << 3) + i

            # Reset registers
            registers["A"] = new_value
            registers["B"] = 0
            registers["C"] = 0

            new_outs = execute_instructions(registers, program)

            # Found value that produces a
            # prefix of the original output
            if new_outs == program[offset:]:
                if offset == 0:
                    # Found the quine value
                    return new_value

                # Compute the next bit of the quine
                queue.append((offset - 1, new_value))

    return -1