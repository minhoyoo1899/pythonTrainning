# 자바스크립트에서는 ${변수} 작성방식으로 변화된 반면, 파이썬에서는 .format() 이라는 함수가 그 역할을 대체합니다. 
# 이와같이 파이썬에서는 자주 사용하는 테크닉이나, 작성법이 함수화 되어서 지원하는 것이 많아 상당히 특이한 구조의 형태를 보이기도 합니다. 
# 약간의 파이썬 작성에 대한 작성 기본이 갖추어진 다면, 이와 같은 형태를 자주 만나게 되며, 현재의 예제에서는 그리 좋아보이지는 않지만, 함수로 분리되어 관리되기 때문에 그만의 장점도 존재 합니다. 

# 특이한 템플릿 리터럴 작성 방식
# format() 이라는 내장함수로 인수를 정의 한 뒤 바뀌는 형태를 가지고 있다. 
set_string = "text : {template}, {wow}".format(template="hello", wow="yes")
print(set_string)