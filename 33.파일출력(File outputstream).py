score_file = open("score.txt", "w", encoding="utf8")
print("Math : 0", file=score_file)
print("English : 50", file=score_file)
score_file.close

# txt 파일이 생김


score_file = open("score.txt", "a", encoding="utf8")
score_file.write("Science : 80")
score_file.write("\nMusic : 100") #\n은 줄바꿈을 명시적으로 하기 위함
score_file.close