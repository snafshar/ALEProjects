import random

def make_integer_input(size: int, seed: int = 0, low: int = 0, high: int = 1_000_000) -> list[int]:
    if size < 0 or low > high:
        raise ValueError("invalid size or range")
    rng = random.Random(seed)
    return [rng.randint(low, high) for _ in range(size)]

if __name__ == "__main__":
    print(make_integer_input(10, seed=42))