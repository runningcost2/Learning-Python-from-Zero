python = "Python is Amazing"
print(python.lower()) #모든 문자 소문자화
print(python.upper()) #모든 문자 대문자화
print(python[0].isupper()) # 0번에 위치한 문자가 대문자가 true 인지 false인지 판단
print(len(python)) #전체 문자열의 길이를 말해줌
print(python.replace("Python", "Java")) #replace를 이용해서 Python을 Java라는 문자로 바꿈

index = python.index("n")   # n이라는 문자가 어디에(몇번째에 위치해) 있는지 확인
print(index)
index = python.index("n", index + 1) #기본적으로 똑같은에 첫번째 n 위치 이후의 n 위치 탐색
print(index)

print(python.find("Java"))
#없는값을 찾으려는 시도는 -1로 출력
# print(python.index("Java")) 이렇게도 java를 찾을 수 있는데 없으면 오류남 index와 find의 차이

print(python.find("o"))

print(python.count("n"))
# #n이라는 글짜가 몇개 있는가? 