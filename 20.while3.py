customer = "Thor"
person = "Unknown" #종업원에게 물어보는 사람

while person != customer :
    print("{0}, your order is ready.".format(customer))
    person = input("What's your name?") #person은 input과 같아야함 그래야 프로그램 작동이 한바퀴를 돌 수 있음.