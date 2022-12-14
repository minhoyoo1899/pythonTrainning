import copy #파이썬에서는 복사를 위한 내장 모듈이 별도로 마련되어 있다. 
# deep copy
a = [1, 2, 3, 4]
b = copy.deepcopy(a) # 모듈의 메서드로 지원하는 깊은복사함수
b.append(5) # 자바스크립트의 .push()와 같은 .append()
print(a == b) # 자바스트립트의 === 일치 비교연산자이다. 
print(a)
print(b)
# shallow copy
c = ['a', 'b', 'c']
d = c # 'c'를 가리키는 변수 d는 '같은 메모리 주소'를 가리키고 있다. 
# 파이썬에서 지원하는 참조타입은 종류가 다양하다. 변하는(mutable) 타입과 불변하는 (immutable)타입을 별도로 지원한다. 
# 자바스크립트에서도 불변하는 새로운 데이터 타입인 symbol 타입이 유용하게 활용되고 있지만, 직관성면에서는 파이썬이 앞선다. 
d.append('d')
print(c == d)
print(c)
print(d)


# 값 그 자체를 가리키는 원시타입(primitive type)과 값이 모인 메모리 주소를 가리키는 참조타입(reference type)은 자바스크립트에서 다룬 개념보다 훨씬 방대하다. '메모리 주소를 가리킨다'라는 한 문장을 이해하기 위해 배열 메서드는 따져보고 비교를 수십 번 해봐야 감이 올 것만 같은 '안보이는 세계'의 전형을 훈련 했던 것처럼, 해당 개념은 입문자가 한 눈에 이해하기는 상당히 어렵다.
# 기가 바이트 단위의 방대한 RAM메모리 중 배정된 임의의 주소 값을 할당(assign)하는 과정이 고수준 언어인 자바스크립트와 파이썬에서는 자동화가 되어있다. 자동화에서 그치지 않고, 직점 볼 방법이 없어 체감형 실습 또한 제한적
# 서비스와 생산성 확보에 특화된 언어에서는 '메모리주소'를 집접 다루는 것이 다소 적합하지는(가능하나 언어컨셉이 다름)않다. 저수준의 언어에서 중요하게 다루는 메모리 주소 개념에 훨씬 더 가까운 '포인터' 데이터타입을 대체하는게 개념이기 때문에 꼼꼼한 컨셉확인이 필요하다. 

# 체감상 어렵지만 얕은복사와 깊은복사는 월씬 더 복잡한 개념을 꽤 사람에 가깝게 자동화(추상화) 한 것이다. 쉽다고 소문난 파이썬에서 조차 제대로된 이해를 목적으로 둔다면, 예외없이 익혀야 하는 개념이다. 때문에 개발입문자가 깊은 복사를 이해하기 어렵기 때문에, 이해하지 말고 사용 할 수있도록 별도의 모듈이 있을 수도 있다.

# '이해(understand)의 특징. 처음 이해가 어렵고 상당한 노력이 필요하지만, 이해하고 나면 아무것도 아니게 되는 경험'을 생각해보면, 본 예제가 설명하는 맥락을 단번에 간파 할 수 있을 것입니다. 자바스크립트에서는 메서드의 목적과 콜백함수로 참조복사를 구분하는 반면, 파이썬에서는 보다 명시적으로 사용하기 위함 때문인지 함수형으로 마련되어있고 훨씬 더 직관적이다. 

