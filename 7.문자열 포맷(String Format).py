# print("a" + "b")  +사용하면 띄어쓰기 없이 붙어서 나옴
# print("a", "b") 콤마 사용시 띄어쓰기 취급

# #Method 1
# print("나는 %d살입니다." % 20) #뒤에있는 %뒤에 있는 값을 앞에 불러와서 출력함
# print("나는 %s을 좋아해요." %"파이썬")
# print("Apple은 %c로 시작해요." % "A")

# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# #Method 2
# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# #Method 3
# print("나는 {age}살이며, {color}색을 좋아해요.".format(age = 20, color="빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age = 20))

# 방법 4 (v3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요")


# Method 5
from random import * #셔플을 쓰기위함

evwinner = range(1, 11)
evwinner = list(evwinner)
shuffle(evwinner)

print("Winners of the event are nunber {0}" .format(evwinner[0:2]))
# # {0}을 써야 리스트에서 불러오기 가능
# # {}에는 .format이 따라옴 콤마에 주목할 것
# #[0:2]의 의미는 리스트 안에서 0번자리부터 2번자리 직전 즉, 1번자리까지 불러온 다는 것은 의미