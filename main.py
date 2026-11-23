import os

JOKE = "Our fridge is covered in magnets the kids made at school. My wife keeps saying we should take a few down, but I can't. I find them too attractive."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
