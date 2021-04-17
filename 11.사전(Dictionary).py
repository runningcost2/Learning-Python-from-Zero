cabinet = {3:"유재석", 100:"김태호"} #숫자는 키 사람이름은 밸류 / 유재석은 3번키를 받음
print(cabinet[3]) #3번열쇠로 열리는 캐비넷에서는 유재석의 짐이 들어가있다
print(cabinet[100])

print(cabinet.get(3)) #이렇게도 값을 가져올 수 있음
#print(cabinet[5]) # 이렇게 적으면 키에러를 발생시키고 프로그램 종료됨 따라서 뒤의 hi는 미출력
print(cabinet.get(5)) #키에러대신 none을 출력하고 프로그램은 계속 됨 따라서 hi 출려됨
print("hi")

print(cabinet.get(5, "사용 가능")) #5를 불러오는데 5가 값이 없으면 none대신 사용가능 출력


print(3 in cabinet) #3이 캐비넷에 있는가? true가 나와야함
print(5 in cabinet) #5가 캐비넷이 있는가? 없으므로 false가 나와야함


#정수가 아닌 string도 가능
cabinet = {"A-3":"유재석", "B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])
print(cabinet)

#새 손님
cabinet["C-20"] = "조세호" #c-20이라는 새로운 키를 만들고 새로운 손님인 조세호를 받음
cabinet["A-3"] = "김종국" #a-3자리에 있던 유재석을 밀고 김종국이라는 새 손님을 받음
print(cabinet)

#간 손님
del cabinet["A-3"] #del을 이용해서 값을 지울 수 있음
print(cabinet)

# key 들만 출력
print(cabinet.keys())

#value들만 출력
print(cabinet.values())

#key, value 쌍으로 출력
print(cabinet.items())

# 목욕탕 영업종료
cabinet.clear()
print(cabinet) #값이 없으니 {}만 출력