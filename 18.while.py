# while은 어떤 조건에 만족할때까지 반복 하는 것
customer = "Thor"
index = 5 # 5번 체크
while index >= 2 : #인덱스가 1보다 크거나 같을 때 까지 진행
    print("{0}, your order is ready. You got {1} chances to pick up you order".format(customer, index))
    index -= 1
    if index == 1:
         print("{0}, your order is ready. this is last chance to pick up your order".format(customer))
         index -= 1
    if index == 0:
         print("{0}, Your order has been disposed".format(customer))