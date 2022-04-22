def divide(dividend, divisor):
  if dividend == 0:
    return 0
  if divisor == 0:
    return None

  # fully divided
  int_quotient, remainder = get_quotient_and_remainder(dividend, divisor)
  if remainder == 0:
    return str(int_quotient)

  decimals = ''
  # not fully divided, infinite cycle detected
  while remainder > 0:
    quotient, remainder = get_quotient_and_remainder(dividend * 10, divisor)
    dividend = remainder
    decimals += str(quotient)

    cycle = detect_cycle(decimals)
    if cycle is not None:
      return str(int_quotient) + '.(' + cycle + ')'
  # not fully divided, no infinite cycle
  return str(int_quotient) + '.' + decimals


def get_quotient_and_remainder(dividend, divisor):
  # can be replaced by / and %
  quotient = 0
  while dividend - divisor >= 0:
    dividend -= divisor
    quotient += 1
  return (quotient, dividend)


def detect_cycle(s):
  length = len(list(s))
  if length % 2 == 0 and s[:length // 2] == s[(length // 2):]:
    return s[:length // 2]


print(divide(4, 2) == '2')
print(divide(2, 4) == '0.5')
print(divide(1, 3) == '0.(3)')
print(divide(1, 7) == '0.(142857)')
print(divide(11, 77) == '0.(142857)')
