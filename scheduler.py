from queue import Queue
from threading import Thread

class Scheduler:
    def __init__(self, system):
        self._queue = Queue()
        self.system = system

    def add_tasks(self, tasks):
        for task in tasks:
            self._queue.put(task)

    def run_all_tasks(self):
        while not self._queue.empty():
            tasks = self._queue.get()
            threads = []
            for task in tasks:
                thread = Thread(target=task.pereform_task)
                threads.append(thread)

            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join()

    def print_tasks(self):
        while not self._queue.empty():
            tasks = self._queue.get()
            for task in tasks:
                if task.type == 'A':
                    print(task.type, task.i+1, task.k+1)
                else:
                    print(task.type, task.i+1, task.j+1, task.k+1)
            print('---------------------')