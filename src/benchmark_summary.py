"""Summarise benchmark timings without external dependencies."""
from statistics import mean, median


def summarise(times_seconds):
    values = list(times_seconds)
    if not values or any(t <= 0 for t in values):
        raise ValueError("provide positive timing samples")
    return {"runs": len(values), "mean_s": mean(values),
            "median_s": median(values), "best_s": min(values)}
