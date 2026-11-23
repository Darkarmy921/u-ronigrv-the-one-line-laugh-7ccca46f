import os

# One funny line, written exactly as-is: a single sentence, no trailing
# newline, so the output file holds only the line itself.
LINE = "I finally organized my passwords, so now I forget them in alphabetical order."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
