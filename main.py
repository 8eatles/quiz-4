from CSVManager import CSVManager
from TextManager import TextManager

csvManager = CSVManager("test.csv", "w", ["이름", "나이", "주소"])
csvManager.writeLine(["홍길동", "20", "서울시"])
csvManager.writeLine(["김철수", "30", "경기도"])
csvManager.writeLine(["이순신", "40", "부산시"])
csvManager.changeMode("r")
csvManager.printBeautify(20)

