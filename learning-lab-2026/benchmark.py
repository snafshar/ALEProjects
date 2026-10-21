import random
import time
from merge_sort import merge_sort

def benchmark(size=10_000, seed=7):
    rng = random.Random(seed)
    data = [rng.randrange(size * 10) for _ in range(size)]
    start = time.perf_counter()
    result = merge_sort(data)
    elapsed = time.perf_counter() - start
    assert result == sorted(data)
    return {"size": size, "seconds": elapsed, "seed": seed}

if __name__ == "__main__":
    print(benchmark())