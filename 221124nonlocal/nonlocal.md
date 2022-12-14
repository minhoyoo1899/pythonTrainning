태생이 유현함을 갖춘 자바스크립트는 영역(scope)의 구분을 프로그래밍 언어레벨의 형태로 만드느라 상당한 노력을 기울이고 있는 반면, 파이썬은 자바스크립트가 가지지못한(?) 구분을 하고 있습니다. 이는 내부함수라고 비유할 수 있는 closure함수와 크게 연관이 되어있습니다. 

강의나, 테스트 상으로는 자유롭게 전역으로 선언하는 것이 자연스러지만, 사실 함수를 전역으로 선언하면 그 자체로 자바스크립트엔진은 함수데이터를 리딩하고 언제든지 호출 할 수 있는 상태로 임시로나마 저장합니다. 코드 실행 스케일이 커지면 커질 수 록 '전역 메모리' 낭비는 애플리케이션 최적화와 직결되는 문제로 소프트웨어 품질을 다루게 되는 시점에서는 상당히 중요해 지는데, 이때 제한적으로 함수를 열고 닫는 closure함수는 상당히 훌륭한 선택이자 테크닉입니다. 자바스크립트는 본질적인 한계 때문에 타입스크립트라는 선택지로 전환되어가는 방식이 채택되는 형태로 나아가고 있다면 (표준에서도 나름대로 노력은 하지만 물리적인 한계는 명확합니다.) 파이썬은 꽤 완성도가 높은 언어입니다. 그 대표적인 개념이 바로 본 예제가 다루는 형태입니다. 

js라고 이름이 작성되어있는 3번파일을 먼저확인하시면 innerFunc()는 내부함수로서 n번 실행이 되고 outerFunc()실행(콜 스택개념 이해필요)이 종료됩니다. 그리고 count라는 변수는 1,2,3,4찍히게 되는데 이것이 가진 자체의 문제점을 '자바스크립트 유저'로서는 정상작동하고 있는 상태이기 때문에 무엇이 어디서 문제가 되는지 발견하기 쉽지않습니다. 자바스크립트에서는 정상작동되도록 설계되어있지만, 전역, 지역이 한데 뒤엉켜있는 형태로 올바른 방식이라 보기 어렵습니다. innerFunc()입장에서 선언된 count 변수는 전역이긴 하나, '마음대로 접근' 하는 것은 문제가 될 수 있었습니다. 

같은 형태가 nonlocal-1 파일의 파이썬 예제입니다. 언어만 다르고 완전히 동일한 형태를 취하고 있습니다. 하지만 해당 코드는 정삭작동하지 않습니다.
mount되지 않았다. 라는 에러사인을 보냅니다. 리액트의 생명주기인 마운트 개념과 같습니다. inner_func()는 상대적으로 전역에 건언된 count를 '인지(메모리에 있기 때문에 마운트 입니다. 없다면 정의되지 않았다고 합니다.)하고 있지만, 마운트 되어있는 것으로 판명되지 않았기 때무에 함부로 데이터를 변형하지 않습니다. 즉 틀별한 경우가 아니라면 불변하게 설계되어 있습니다. 그래서 자바스크립트입장에서는 특별한 키워드 nonlocal 키워드 개념이 존재합니다. 
말 그대로 '지역이 아닌'이라는 뜻으로 "내 여역 바깥에 있는 데이터를 살아있게 만드는" 즉 생명주기상 마운트 시키는 키워드로 mutable하게, 즉 변할 수 있는 데이터로 상태를 바꿉니다. 

자바스크립트 유저 입장에서는 '당연해보이는 과정에 키워드가 끼어 들어간 현태' 이지만 변수가 많거나 관리할 데이터가 많을 경우에 non-local 사용유무는 상당히 효과적으로 데이터를 처리하고 관리하는 불변성에 지대한 영향을 끼치게 됩니다. 

더 나아가 '전역 리딩', "전역 선언"은 최대한 사용하지 않으려는 개발자들의 철학이 담겨있기도 합니다. 언제든지 선언을 할당을 할 수 있기 때문에 그 자체로 개발자는 편리하지만, 의외의 복병을 만들어내거나, 성능최적화의 문제를 야기 할 수 있기 때문입니다. 


전역, 지역 변수를 너머, 메모리, 리닝, 마운트, 생명주기, 상태제어까지 개념 하나하나 거미줄 처럼 연관되어 있음을 발견해 보시기 바라며, 서비스 스케일업 할 수록 closure기느으이 지원은 상당히 고마운 일이 되기 때문에 아직은 체감이 되지 않더라도, 한 두번 작동이 어떻게 돌아가는지 정도 점검하는 시간을 갖는다면, 머지않아서 필요성을 확인 하게 될 것으로 예상합니다. 이에 비슷한 global이라는 키워드도 있으므로 자바스크립트에 비해 꽤 엄격한 파이썬의 안정성을 살펴 보시기 바랍니다. 