# Quiz) You are an Ubar taxi driver.
# You have a chance to match 50 passengers.
# Code a program to find the total number of passengers on board.

# * Total elapsed time for each passenger is set by random numbers between 5 to 50 minutes.
# * You can only match passengers between 5 and 15 minutes of total time.

# ex)
# [0] 1st passenger (Total elapsed time : 15 min)
# [ ] 2st passenger (Total elapsed time : 50 min)
# [0] 3st passenger (Total elapsed time : 5 min)
# ...
# [ ] 50st passenger (Total elapsed time : 16 min)

# You have picked up 5 passengers today

#My Answer
from random import *

index = 0
index1 = 0

for passengers in range(1, 51):
    TETime = randrange(5, 51)
    if 5 <= TETime <= 15:
        print("[0] {0}st passenger (Total elapsed time : {1} min)".format(passengers, TETime))
        index += 1
        index1 += 1
    if TETime >= 16:
        print("[ ] {0}st passenger (Total elapsed time : {1} min)".format(passengers, TETime))
        index1 += 1
    if index1 >= 50:
        print(" ")
        print("You have picked up {0} passengers today.".format(passengers))


#Exemplary answer
from random import *
cnt = 0
for i in range(1, 51):
    time = randrange(5, 51)
    if 5 <= time <= 15:
        print("[0] {0}st passenger (Total elapsed time : {1} min".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}st passenger (Total elapsed time : {1} min".format(i, time))

print("You have picked up {0} passengers today.".format(cnt))