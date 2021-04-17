# 집합 (set)
# 중복 안됨, 순서 없음(출력할때마다 정해진 순서가 없이 랜덤순서로 출력됨)

my_set = {1,2,3,3,3} 
print(my_set) #세트는 중복을 허용하지 않기때문에 1, 2, 3만 출력

java = {"유재석", "김종국", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java나 python을 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (예. java는 할 수 있지만 python은 할줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김종국")
print(python)

# java를 까먹음
java.remove("김종국")
print(java)