weather = input("오늘 날씨는 어때요?")
#print(weather) # 사용자가 입력한 값 출력ㅇ

if weather == "비":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물 필요 없어요")