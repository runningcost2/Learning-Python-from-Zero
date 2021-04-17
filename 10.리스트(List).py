# 리스트 []

#지하철 칸별로 10명, 20명, 30명이 있다고 가정

# subway1 = 10
# subway2 = 20
# subway3 = 30

subway = [10, 20, 30]

print(subway)

subway = ["유재석", "조세호", "박명수"]
print(subway)

#조세호는 몇 번째 칸에 타고 있는가?
print(subway.index("조세호"))

#하하가 다음 정류장에서 다음탄에 탐
subway.append("하하")
print(subway) #append는 항상 맨 뒤에 붙게 된다

#정형돈을 유재석과 조세호 사이에 태워봄
subway.insert(1, "정형돈")  #1번째 자리에 정형돈이 들어가도 조세호 부터 한칸씩 뒤로 밀림
print(subway)

#지하철에 있는 사람을 한 명씩 뒤에서 꺼냄 이경우 하하가 빠짐
print(subway.pop())
print(subway)

print(subway.pop()) #한명씩 뒤에서 빠지는걸 볼 수 있음.
print(subway)

print(subway.pop())
print(subway)

subway.append("조세호")
subway.append("박명수")
subway.append("하하") #원상복구
print(subway)

subway.append("유재석")
print(subway)

#유재석은 몇명이 있는가?
print(subway.count("유재석")) #이것은 유재석이란 사람이 몇번인지 카운트함 결과로 2 출력

#정렬도 가능
num_list = [5, 2, 4, 3, 1] #랜덤한 순서로 숫자 배치
num_list.sort() #이걸 쓰고 프린트하면
print(num_list) #1, 2, 3, 4, 5로 출력됨

num_list.reverse() #순서를 뒤집어서 출력하기
print(num_list)

# 모두 기우기
num_list.clear()
print(num_list)

#다양한 자료형 함께 사용
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5, 2, 4, 3, 1]
num_list.extend(mix_list)
print(num_list)