"""Fixtures module. """

import csv
import pathlib
import sqlite3

SAMPLE_DATA = [("Spawner service", 20220614, "v1.2.2"), ("Authentication service", 20220622, "v0.2.2."), ("DCAT service", 20220611, "v3.1.0")]
FILE = pathlib.Path(__file__)
DIR = FILE.parent
CSV_FILE = DIR / "services.csv"
SQLITE_FILE = DIR / "services.db"


def create_csv(services_data, path):
    with open(path, "w") as opened_file:
        writer = csv.writer(opened_file)
        for row in services_data:
            writer.writerow(row)


def create_sqlite(services_data, path):
    with sqlite3.connect(path) as db:
        db.execute("CREATE TABLE IF NOT EXISTS services (name text, timestamp int, version text)")
        db.execute("DELETE FROM services")
        db.executemany("INSERT INTO services VALUES (?,?,?)", services_data)


def main():
    create_csv(SAMPLE_DATA, CSV_FILE)
    create_sqlite(SAMPLE_DATA, SQLITE_FILE)
    print("All done. OK")


if __name__ == "__main__":
    main()
