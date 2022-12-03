import os.path


class FileManager:
    def __init__(self, filepath, mode, defaultExt=None, defaultPath="data", autoOpenClose=True):
        self.defaultPath = defaultPath
        self.filepath = filepath
        self.mode = mode

        self.options = {
            "ext": defaultExt,
            "path": defaultPath,
            "autoOpenClose": autoOpenClose,
        }

        _, ext = os.path.splitext(filepath)

        if defaultExt is not None and ext != f".{defaultExt}":
            raise Exception(f"파일의 확장자가 {defaultExt}가 아닙니다. ({ext})")

        if mode != "r" and mode != "w" and mode != "a":
            raise Exception(f"지원하는 모드(r,w,a)가 아닙니다. ({mode})")

        # create directory if not exists
        if not os.path.exists(defaultPath):
            os.makedirs(defaultPath)

        if self.options["autoOpenClose"]:
            self._open()

    def __del__(self):
        if self.options["autoOpenClose"]:
            self._close()

    def _open(self, mode=None):
        self.file = open(f"{self.defaultPath}/{self.filepath}", self.mode if mode is None else mode)

    def _close(self):
        self.file.close()

    def changeMode(self, mode):
        if mode != "r" and mode != "w" and mode != "a":
            raise Exception(f"지원하는 모드(r,w,a)가 아닙니다. ({mode})")

        if self.mode == mode:
            return

        self._close()
        self.mode = mode
        self._open()

    def writeLine(self, text, mode="w"):
        self.changeMode(mode)
        self.file.write(text + "\n")

    def readLine(self):
        self.changeMode('r')
        return self.file.readline().rstrip()
