# Quiz 4 File I/O


## Question 1

Class 에는 상속이라는 개념이 있다.

특정 Class를 상속받아 부모 Class의 모든 기능을 사용할 수 있다.

코드에는 `FileManager` 클래스를 `CSVManager` 클래스가 상속받고 있다.

`CSVManager` 클래스의 `printBeautify` 함수는 CSV 파일의 내용을 보기 쉽게 화면에 출력해주는 함수이다.

`printBeautify` 함수는 화면에 정보를 print 할 때 cell의 너비를 조절할 수 있는 기능을 가지고 있다.

`printBeautify` 함수의 cell 너비를 20으로 설정해 보시오.



## Question 2

`FileManager` 는 파일을 읽고 쓰는데 사용되는 기본적인 기능을 담은 클래스 이다.

`FileManager` 의 `readLine`, `writeLine` 메소드는 각각 한 줄씩 읽고 쓰는데 사용된다.

`readLine`과 `writeLine` 메소드에 각각 적합한 모드가 아닌 경우 모드를 변경하는 기능을 넣고
`main.py` 파일에서 `csvManager.changeMode("r")` 내용을 지우고 잘 동작하는지 확인하시오.

