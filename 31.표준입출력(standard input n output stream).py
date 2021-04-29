# print("python", "Java", "JavaScript", sep=" vs ")

# print("python", "Java", end="? ")
# print("Which is the funniest?")

# import sys
# print("Python", "Java", file=sys.stdout) #standard output
# print("Python", "Java", file=sys.stderr) #standard error
# #필요할때 지정해서 따로 에러처리 가능함

scores = {"Math":0, "English":50, "Music":100}
for subject, score in scores.items():
    #print(subject, score)
    print(subject.ljust(8), str(score).rjust(4), sep=":")

#make a waiting list
# 001, 002, 003, ...
for num in range(1, 21):
    print("Waiting number : " + str(num).zfill(3)) # Before zfill 1, 2, ... 11, 12, ...
                                                   # After zfill  001, 002, ... 011, 012, ...

answer = input("Input any value : ")
answer = 10
#print("You just input " + answer +".")
print(type(answer))
#class 'int'의 의미는 사용자 입력을 통해 받은 밸류는 항상 문자열 형태라는 것을 의미