score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read())
score_file.close() 
#모든 파일을 불러옴


score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) # 줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline())
print(score_file.readline())
print(score_file.readline())


score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline(), end="") # 줄 붙임
print(score_file.readline(), end="")
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close


# 불러올 파일이 총 몇줄인지 모를 때는

score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close()


#list에 값을 넣어서 처리하는 방법

score_file = open("score.txt", "r", encoding="utf8")
lines = score_file.readlines # list 형태로 저장
for line in lines:
    print(line, end="")

score_file.close()