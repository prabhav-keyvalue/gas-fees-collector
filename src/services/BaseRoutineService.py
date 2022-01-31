from abc import ABC, abstractmethod
import sched
import time


class BaseRoutineService(ABC):

    def __init__(self, name, interval = 5, priority = 1):
        self.name = name
        self.scheduler = sched.scheduler(time.time, time.sleep)
        self.interval = interval
        self.priority = priority

    @abstractmethod
    def task(self):
        pass

    def _run_task(self):
        print(f'Running routine task of {self.name} at interval - {self.interval}s')
        self.task()
        self.scheduler.enter(self.interval, self.priority, self._run_task)
    
    def start(self):
        print(f'Starting routine service {self.name} at interval - {self.interval}s')
        self.scheduler.enter(self.interval, self.priority, self._run_task)
        self.scheduler.run()
