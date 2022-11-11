from tkinter import *
basic_data_dict = {
  "title_name" : "HTML maker",
  "window_width" : 300,
  "window_height" : 300,
  "resizable_x" : True,
  "resizable_y" : True,
}

class Resizable: 
  def __init__(self, width, height) :
    self.width = width,
    self.height = height,
    @property
    def size(self):
      set_tuple = self.width + self.height
      return set_tuple

# ?  Resizable class 만들어 보기
# * 사이즈는 어디에나 사용 할 수 있을 것 같은 생각이 들어 클래스로 지정해 보기로 함 
# * getter의 형태가 자바스크립트로 클래스와 다른 점을 발견함
# ** @데코레이터(C++) 라는 문법으로 getter를 사용 할 수 있는 것이 특징
#** get 키워드를 사용하는 자바스크립트 getter

test = Resizable(100, 200)
# print(dir(test))
# print(test.size)
# print(type(test.size[0]))
# print(type(str(test.size[1])))
# 수많은 타워체킹 과정

window = Tk()
window.title(basic_data_dict["title_name"])

geometry_value = Resizable(basic_data_dict["window_width"], basic_data_dict["window_height"]).size
# ? geometry_value 변수 : 위에서 선언한 클래스를 할당하면서 필요한 값을 가져오기 위해 getter인 size를 불러옴
# * 값을 불러오다보니 자바스크립트는 타입을 지정할 수 없는데, 파이썬에서는 무조건 튜플로 처리되는 것을 확인 할 수 있었음
# * 코드양으로 보았을 땐 더 길어진 현상이 일어났지만, 사이즈를 사용 하는 일이 많아지면 조금 편해질 듯

window.geometry(str(geometry_value[0])+"x"+str(geometry_value[1]))
window.resizable(basic_data_dict["resizable_x"], basic_data_dict["resizable_y"])


def html_maker():
  temp_string = """
  <html>
    <head></head>
    <body></body>
  </html>
  """
  button["text"] = temp_string

  button = Button(window, text="HTML 찍어내기!!!", width=20, height=5, command=html_maker)

  #? Button() 첫글자가 대문자인 것으로 보아 class문법응로 제작 된 덕을 유추 할 수 있었다.
  #* 의도 : 버튼을 누르면 원하는 문자열이 나타났으면 좋겠다.
  # pseudo : 최종적으로 html 파일이 생성되서 저장되면 좋겠다.
  button.pack()

window.mainloop()