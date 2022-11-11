from tkinter import *
# memo
# psudo HTML 찍어내는 기게 만들기
# ? 인스톨러 만드는 법 ?
# ? GUI tkinter가 있는 것을 알겠는데...


# Todo 1. 일단 작동되는지 확인하기

window = Tk()
# * 인터넷 검색해보니 Tk()라는 함수를 호출하면 필요한 모든 라이브러리 데이터를 변수에 대입 할 수 있음을 발견함


print(window)
# * 불러온 라이브러리에 무슨 함수와 값들이 있는지 확인하려고 디버거 사용함
# * 무엇인지 한눈에 안보이는 것 90프로
# * class variables 항목을 조회헤보니 얼추 기능을 유추 할 수 있는 것들을 확인 할 수 있음

# * HTML처럼 기본 형태는 무엇인지 검색함
label = Label(window, text="이게 무엇이지?")
label.pack()

window.mainloop()