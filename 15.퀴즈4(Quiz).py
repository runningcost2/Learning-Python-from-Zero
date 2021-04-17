# 퀴즈) 당신의 학교에서는 파이썬 코딩 대회를 주최합니다.
# 참석률을 높이기 위해 댓글 이벤트를 진행하기로 하였습니다.
# 댓글 작성자들 중에 추첨을 통해 1명은 치킨, 3명은 커피 쿠폰을 받게 됩니다.
# 추첨 프로그램을 작성하시오
# 조건1 : 편의상 댓글은 20명이 작성하였고 아이디는 1~20 이라고 가정
# 조건2 : 댓글 내용과 상관없이 무작위로 추첨하되 중복불가
#         즉, 치킨과 커피 동시 당첨 불가
# 조건3 : random 모듈의 shuffle 과 sample 을 활용

# (출력 예제)
# -- 당첨자 발표 --
# 치킨 당첨자 : 1
# 커피 당첨자 : [2, 3, 4]
# -- 축하합니다 --

# (활용예제) 랜덤과 셔플의 활용 예제임
# from  random import*
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)   #shuffle은 lst안의 값을 무작위로 바꿈
# print(lst)
# print(sample(lst, 1)) #lst중에서 하나를 무작위로 선정함

#답

# from random import *
# users = range(1, 21) # 1부터 20까지 숫자를 생성 이경우 class는 range가 됨
# users = list(users)
# shuffle(users)

# winners = sample(users, 4) #샘플을 뽑아서 4명중에서 1명은 치킨, 3명은 커피
# print("-- 당첨자 발표 --")
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))
# print("-- 축하합니다 --")

