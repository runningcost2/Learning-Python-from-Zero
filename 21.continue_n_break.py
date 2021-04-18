absent = [2, 8] #There are students that absents today.
no_book = [7] #Student who didn't brought the book in need.
index = 0

for student in range(1, 20):
    
    if student in absent:
        continue
    elif student in no_book:
        print("{0}, borrow the book from {1}.".format(student, student + 1))
        if student + 1 in absent:
            print("Oh, i forgot {0} is absent today. {1}, borrow the book from {2}.".format(student +1, student, student + 2))
    print("{0}, please read the book.".format(student))
    index += 1
    if index >= 7:
        print("Today's class is over. Have a nice day")
        break