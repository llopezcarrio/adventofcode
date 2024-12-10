import re

def calculateResults(text):

   regex = r"mul\(\b([0-9]|[1-9][0-9]|[1-9][0-9][0-9])\b,\b([0-9]|[1-9][0-9]|[1-9][0-9][0-9])\b\)"
   matches = re.finditer(regex, text)
   total=0
   for matchNum, match in enumerate(matches, start=1):
      total+=(int(match.group(1))*int(match.group(2)))

   return total
