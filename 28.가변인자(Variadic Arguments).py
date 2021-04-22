# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print("name : {0}\tage : {1}\t".format(name, age), end=" ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("Kimberly", 20, "python", "Java", "C", "C++", "C#")
# profile("Robert", 25, "Kotlin", "Swift", "", "", "")

#In the case, you have to rewrite your code to add or delete funtion
#Variadic Arguments can be used for these cases

def profile(name, age, *language):
    print("name : {0}\tage : {1}\t".format(name, age), end=" ")
    for lang in language:
        print(lang, end=" ")
    print()


profile("Kimberly", 20, "python", "Java", "C", "C++", "C#", "JavaScript")
profile("Robert", 25, "Kotlin", "Swift")