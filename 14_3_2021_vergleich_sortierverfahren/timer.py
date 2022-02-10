from time import *

class timer:
    start_time = 0
    end_time = 0

    def start(self):
        self.start_time = time()

    def stop(self):
        self.end_time = time()
        return self.end_time - self.start_time
