from tkinter import *
# memo 
# pseudo HTML 찍어내는 기계 만들기
# ? 인스톨러 만드는 방법?
# ? GUI tkinter가 있는 것은 알겠는데....

# Todo 1. 일단 작동되는지 확인 하기

window = Tk()
window.title("HTML maker")
# * HTML의 <title> 역할을 하는 함수가 있는 것을 발견, 적용

window.geometry("300x300")
# * 특이하게 브라우저 창 사이즈도 개발자가 직접 지정 할 수 있는 것 확인, 적용

window.resizable(True, True)
# * 브라우저는 기본 값인 사이즈 조정 여부도 개발자가 직접 허용/블허 할 수있음을 발견

label = Label(window, text="이게 무엇이지?")
# * Label() 레이블이라는 클래스는 HTML <p>태그 처럼 인터페이스 창에서 글시를 쓸 때 사용하는 것을 발견

label.pack(side="bottom")
# * pack()이라는 단어의 의미가 추론이 안되어 찾아보니 <HTML>의 display:block과 비슷한 역할을 하는 것으로 추측

window.mainloop()