# print("대기번호 : 1") #이렇게는 계속 못한다
# print("대기번호 : 2")
# print("대기번호 : 3")
# print("대기번호 : 4")

#for waiting_no in [0, 1, 2, 3, 4]:  #이렇게 하거나

# for waiting_no in range(5): #0, 1, 2, 3, 4 # 이렇게 할 수 있다.
#     print("대기번호 : {0}". format(waiting_no))

for waiting_no in range(1, 6): #0이 아닌 1부터 세도록 만드는 것
    print("대기번호 : {}".format(waiting_no))