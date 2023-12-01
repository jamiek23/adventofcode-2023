import importlib


def main():
    # Run for each day
    for d in range(1, 25):
        try:
            day = importlib.import_module(f".day{d}", __name__)
            print(f"-> Running day {d}")
            day.main()
        except ImportError:
            # Ignore missing modules
            pass