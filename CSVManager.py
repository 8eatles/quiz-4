import os.path

from FileManager import FileManager


class CSVManager(FileManager):
    def __init__(self, filepath, mode, columnHeaders=None):
        super().__init__(filepath, mode, "csv")

        if mode == "w":
            if columnHeaders is None:
                raise Exception("쓰기 모드에서는 columnHeaders가 필요합니다.")
            self.file.write(",".join(columnHeaders) + "\n")
            self.columnHeaders = columnHeaders

        elif mode == "a":
            if columnHeaders is not None:
                raise Exception("추가 모드에서는 columnHeaders가 필요하지 않습니다.")
            self.changeMode("r")
            self.columnHeaders = self.readLine()
            self.changeMode("a")
            self.file.seek(0, os.SEEK_END)

        elif mode == "r":
            self._open()
            self.columnHeaders = self.file.readline().rstrip().split(",")

        else:
            raise Exception(f"지원하는 모드(r,w,a)가 아닙니다. ({mode})")

        self.columnCount = len(self.columnHeaders)

    def changeMode(self, mode):
        if mode != "r" and mode != "w" and mode != "a":
            raise Exception(f"지원하는 모드(r,w,a)가 아닙니다. ({mode})")

        if self.mode == mode:
            return

        self._close()
        self.mode = mode
        self._open()

    def writeLine(self, cellTexts):
        if self.mode == "r":
            raise Exception("읽기 모드에서는 write를 할 수 없습니다.")

        if cellTexts is None or len(cellTexts) != self.columnCount:
            raise Exception("셀의 개수가 일치하지 않습니다.")

        super().writeLine(",".join(cellTexts))

    def readLine(self):
        if self.mode == "w" or self.mode == "a":
            raise Exception("쓰기 모드에서는 read를 할 수 없습니다.")

        row = super().readLine()

        return row.split(",") if row else None

    def printBeautify(self, cellWidth=10):
        headers = self.readLine()
        headerString = "|".join([f"{header:^{cellWidth}}" for header in headers])
        print(headerString)
        print("-" * len(headerString))

        while True:
            row = self.readLine()
            if not row:
                break
            print("|".join([f"{cell:^{cellWidth}}" for cell in row]))
