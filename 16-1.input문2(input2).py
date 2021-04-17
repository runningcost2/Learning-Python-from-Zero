# weather = input("오늘 날씨는 어때요?")
# #print(weather) # 사용자가 입력한 값 출력ㅇ

# if weather == "비": or weather == "눈"
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("준비물 필요 없어요")

temp =int(input("기온은 어때요? ")) #온도는 항상 정수이기 때문에 int 사용
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")