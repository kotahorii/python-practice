import random
import time
from typing import Union


class Queue:
    def __init__(self) -> None:
        self.items: list[Union[str, int]] = []

    def is_empty(self) -> bool:
        return not self.items

    def enqueue(self, item: Union[str, int]) -> None:
        self.items.insert(0, item)

    def dequeue(self) -> Union[str, int]:
        return self.items.pop()

    def size(self) -> int:
        return len(self.items)


def simulate_line(till_show: int, max_time: int):
    pq: Queue = Queue()
    tix_sold: list[Union[str, int]] = []

    for i in range(100):
        pq.enqueue("person" + str(i))

    t_end: float = time.time() + till_show
    now: float = time.time()
    while now < t_end and not pq.is_empty():
        now = time.time()
        r: float = random.randint(0, max_time)
        time.sleep(r)
        person: Union[str, int] = pq.dequeue()
        print(person)
        tix_sold.append(person)

    return tix_sold


sold: list[Union[str, int]] = simulate_line(10, 1)
print(sold)
