# 퀴즈) 사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

# 예) http://naver.com
# 규칙1 : http:// 부분은 제외 => naver.com
# 규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
# 규칙3 : 남은 글자 중 처음 세자리 + 글자 갯수 + 글자 내 'e' 갯수 + "!" 로 작성
# 예) 생성된 비밀번호 : nav51!

url = "http://naver.com"

my_pass = url.replace("http://", "") # 규칙1

my_pass = my_pass[:my_pass.index(".")] #규칙2 #my_pass라는 변수 내에서 처음 나오는 . 의 위치

password = my_pass[0:3]
numb = len(my_pass)
count_e = my_pass.count("e")
#규칙3


print(password + str(numb) + str(count_e) + "!")

#정답

password1 = my_pass[:3] + str(len(my_pass)) + str(my_pass.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password1))