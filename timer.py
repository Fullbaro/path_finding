import time

class Timer:

    def __init__(self):
        self.st = round(time.time() * 1000)

    def stop(self, msg=""):
        print(f"{msg} took {round((round(time.time() * 1000) - self.st) / 1000, 3)} sec")