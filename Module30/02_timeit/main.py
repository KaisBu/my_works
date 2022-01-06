import timeit
import time
from typing import List

res: float = timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
print('Working hours for timeit:\t', res)

start_time_1 = time.time()
list_comp: List[str] = ["-".join(str(n) for n in range(100)) for _ in range(10000)]
end_time_1 = time.time() - start_time_1
print('Working hours for list comprehensions:\t', end_time_1)

start_time_2 = time.time()
res2 = map(lambda x: "-".join(str(n) for n in range(100)), [n for n in range(2)])
end_time_2 = time.time() - start_time_2
print('Working time for map:\t', end_time_2)
