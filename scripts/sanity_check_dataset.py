from pathlib import Path

def main():
    candidates = [
        Path("data/30Columnists/raw_texts"),
        Path("../data/30Columnists/raw_texts"),
    ]
    base = next((c for c in candidates if c.exists()), None)
    if not base:
        raise SystemExit("Dataset not found. Expected data/30Columnists/raw_texts")
    authors = [p for p in base.iterdir() if p.is_dir()]
    n_files = sum(1 for _ in base.rglob("*.txt"))
    print(f"Authors: {len(authors)}")
    print(f"Text files: {n_files}")

if __name__ == "__main__":
    main()
