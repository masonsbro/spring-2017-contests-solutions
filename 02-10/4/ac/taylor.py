import fileinput
import heapq
lines = fileinput.input()

class AirportCode():
    priorities = []

    def __init__(self, code):
        self.code       = code

    def sort_key(self):
        try:
            return AirportCode.priorities[self.code]
        except KeyError:
            value = 0
            multiplier = 10000
            for ch in self.code:
                value += multiplier * ord(ch)
                multiplier //= 100
            return len(AirportCode.priorities) + value

cases = int(lines.readline())
for _ in range(cases):
    num_priority  = int(lines.readline())
    priority_codes = []
    for _ in range(num_priority):
        priority_codes.append(lines.readline().strip())
    priority_codes.sort()
    priority_codes = {code: index for index,code in enumerate(priority_codes)}
    AirportCode.priorities = priority_codes

    num_input = int(lines.readline())
    input_codes = []
    for _ in range(num_input):
        input_codes.append(AirportCode(lines.readline().strip()))

    for code in sorted(input_codes, key=lambda c: c.sort_key()):
        print("{}".format(code.code))
#         print("Key: {}, value: {}".format(code.code, code.sort_key()))
