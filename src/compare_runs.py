"""Compare paired algorithm timing runs with clear input checks."""

def speedup(baseline_seconds, candidate_seconds):
    if baseline_seconds <= 0 or candidate_seconds <= 0:
        raise ValueError('timings must be positive')
    return baseline_seconds / candidate_seconds

def relative_change_percent(reference, candidate):
    if reference == 0:
        raise ValueError('reference must be non-zero')
    return 100.0 * (candidate - reference) / abs(reference)
