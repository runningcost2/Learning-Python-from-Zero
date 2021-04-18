# Changing attendance number. ex)1, 2, 3, 4 => 101, 102, 103, 104

students = [1,2,3,4,5]
print(students)
students = [i+100 for i in students] #loading every i in students and add 100 each
print(students)

# changing name to length of name
students1 = ["Zeus", "Hestia", "Poseidon", "Julius Caesar"]
students1 = [len(i) for i in students1]
print(students1)

# Making uppper letters name
students2 = ["Robert", "Chris", "Natasha"]
students2 = [i.upper() for i in students2]
print(students2)