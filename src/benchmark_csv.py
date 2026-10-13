"""Write benchmark observations to CSV for later analysis."""
import csv

FIELDS = ["algorithm", "input_size", "elapsed_ms", "operations", "notes"]


def write_results(path, rows):
    with open(path, "w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=FIELDS, extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in FIELDS})
