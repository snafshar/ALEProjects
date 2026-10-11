/** Immutable result record for algorithm experiments. */
public record BenchmarkResult(String algorithm, int inputSize, long elapsedNanos, long operations) {
    public BenchmarkResult {
        if (algorithm == null || algorithm.isBlank()) throw new IllegalArgumentException("algorithm is required");
        if (inputSize < 0 || elapsedNanos < 0 || operations < 0) throw new IllegalArgumentException("metrics cannot be negative");
    }

    public double milliseconds() {
        return elapsedNanos / 1_000_000.0;
    }

    public double operationsPerSecond() {
        return elapsedNanos == 0 ? 0.0 : operations * 1_000_000_000.0 / elapsedNanos;
    }
}
