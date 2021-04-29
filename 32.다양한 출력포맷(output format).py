# Leave empty space as blank, align to the right, secure 10 spaces for digits in total.
print("{0: >10}".format(500)) # 10자리 공간을 확보하고 오른쪽 정렬을 하고 빈자리는 그대로 출력

# If number is positive, mark "+". If number is negative, mark "-"
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500))

# Align to the left, Fill blank with "_"
print("{0:_<+10}".format(500))

# Comma every 3 digits.
print("{0:,}".format(1000000000000000000))

# Comma every 3 digits with "+" or "-"
print("{0:,}".format(-1000000000000000000))

# Comma every 3 digits with "+" or "-" and secure spaces for digits.
# Fill blank with "^"
print("{0:^<+30,}".format(100000000000000)) #30자리만큼의 공간 확보(30), +-부호 붙임(+), 왼쪽정렬(<), 빈자리는 ^로 출력(^)

# Decimal output
print("{0:f}".format(5/3))

# Rounding to decimal places (Round to 2nd decimal place)
print("{0:.2f}".format(5/3)) 