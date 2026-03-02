class Counter:
    def __init__(self):
        self._strokes = ""
        self._limit = 0

    def reset(self):
        self._strokes = ""

    def click(self):
        self._strokes = self._strokes + '|'
        if len(self._strokes) > self._limit and self._limit != 0:
            print("Limit Exceeded")

    def getValue(self):
        return self._strokes

    def setLimit(self, maximum):
        self._limit = maximum



