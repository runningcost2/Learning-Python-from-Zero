# def profile(name, age, main_lang):
#     print("Name : {0}\tAge : {1}\tMain Language: {2}" \
#         .format(name, age, main_lang)) # \ makes 2 lines work as 1 line

# profile("Tanaka", 20, "Python")
# profile("Kimberly", 25, "Java")

# Assume that other conditions are the same but names.

def profile(name, age=17, main_lang="Python"):
    print("Name : {0}\tAge : {1}\tMain Language: {2}" \
        .format(name, age, main_lang)) # \ makes 2 lines work as 1 line

profile("Tanaka")
profile("Kimberly")