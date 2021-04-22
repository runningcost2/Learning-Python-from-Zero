#지역변수란 함수호출할때 만들어졌다가 함수호출이 끝나면 사라짐
#전역변수는 프로그램내 모든 공간에서 어디서든 불러올 수 있는 것.

#지역변수 예시

# gun = 10 

# def checkpoint(soliders): # 경계근무에 나가는 군인 수
#     gun = 20
#     gun = gun - soliders # 이곳의 gun은 위의 gun이 아니고 checkpoint 안에서 만들어짊. 초기화가 안되었기때문에 위의 gun = 20 없이는 사용불가.
#     print("[총기함 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
# print("남은 총 : {0}".format(gun))

#result

#전체 총 : 10
#[총기함 내] 남은 총 : 18
#남은 총 : 10


# #전역변수 예시

# gun = 10 

# def checkpoint(soliders):
#     global gun      #전역 공간에 있는 gun 사용
#     gun = gun - soliders 
#     print("[총기함 내] 남은 총 : {0}".format(gun))

# print("전체 총 : {0}".format(gun))
# checkpoint(2) # 2명이 경계근무 나감
# print("남은 총 : {0}".format(gun))

# # 전역변수는 코드관리가 어려워서 권장되는 방법이 아님



# 권장 방법

gun = 10

def checkpoint(soliders):
    global gun      #전역 공간에 있는 gun 사용
    gun = gun - soliders 
    print("[총기함 내] 남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soliders):
    gun = gun - soliders
    print("[총기함 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계근무 나감
print("남은 총 : {0}".format(gun))