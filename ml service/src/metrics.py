import time


class SearchMetrics:

    def __init__(self):
        self.start = None

    def start_timer(self):
        self.start = time.time()

    def stop_timer(self):
        return round((time.time() - self.start) * 1000, 2)