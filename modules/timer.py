import time

# this is 100% chatgpt

class Timer:
    def __init__(self) -> None:
        self._start_time = None
        self._end_time = None

    def start(self) -> None:
        self._start_time = time.perf_counter()
        self._end_time = None  # reset end time

    def stop(self) -> float:
        if self._start_time is None:
            raise RuntimeError("Timer was not started.")
        self._end_time = time.perf_counter()
        elapsed = self._end_time - self._start_time
        return elapsed
