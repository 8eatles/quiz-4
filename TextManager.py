import os.path


class TextManager:
    def __init__(self, filepath, mode):
        _, ext = os.path.splitext(filepath)

        if ext != ".txt":
            raise Exception(f"파일의 확장자가 txt가 아닙니다. ({ext})")

        if mode != "r" and mode != "w" and mode != "a":
            raise Exception(f"지원하는 모드(r,w,a)가 아닙니다. ({mode})")

        self.mode = mode

        # create directory if not exists
        if not os.path.exists("data"):
            os.makedirs("data")

        self.file = open(f"data/{filepath}", mode)

    def writeLine(self, text):
        if self.mode == "r":
            raise Exception("읽기 모드에서는 write를 할 수 없습니다.")

        self.file.write(text + "\n")

    def readLine(self):
        if self.mode == "w" or self.mode == "a":
            raise Exception("쓰기 모드에서는 read를 할 수 없습니다.")

        return self.file.readline()

    def __del__(self):
        self.file.close()
