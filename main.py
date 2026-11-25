import os

ROAST = (
    "Incident report: my agent let a finished poem die at its 03:27 deadline, "
    "still waiting for permission to press the submit button it was built to press."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
