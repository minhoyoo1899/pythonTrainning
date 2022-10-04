# javascript class constructor 문법
# class Pokemon {
#   constructor(id, name) {
#     this.id = id;
#     this.name = name;
#   }
# }

# python에서도 생성자 함수를 지원한다. 
# class 작성법 '구조'는 동일 하지만, 작성법이 특이한 것을 확인
# javascript에서는 함수는 __init__ 단어 양옆 언더바 두 번씩 작성하는 형태로 함수를 선언한다. 
# js는 this 키워드를 매개변수 자리에 작성하진 않지만, python에서는 self라는 작성해야 한다.
# python에서 다루는 self는 javascript의 this와 비슷한 역할을 한다.

class Pokemon:
  def __init__(self, id, name):
    self.id = id
    self.name = name

    
getFromJson = ["피카츄", "라이츄", "파이리", "꼬부기", "버터풀", "야도란", "피존투", "또가스", "야도킹", "고오스"]
#list initalizes
pokemon_list=[]

#javascript의 배열에서는 프로퍼티 값으로 length가 기본값으로 제공되지만, 
# python의 length값은 여러 곳에서 꺼내 올 수 있다.
# range()라는 함수로 length를 꺼내 올 수 있다. __len__과 같은 속성으로 접근 할 수 있다. 
# python의 append() 함수는 javascript에서의 .push()메서드 함수와 같다. 
for i in range(getFromJson.__len__()):
  pokemon_list.append(Pokemon(i+1, getFromJson[i]))

#__dict__ 접근자는 javascript의 console.dir()로 데이터를 확인 하는 것과 같다. 
for obj in range(pokemon_list.__len__()):
  print(pokemon_list[obj].__dict__)
