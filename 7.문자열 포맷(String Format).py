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