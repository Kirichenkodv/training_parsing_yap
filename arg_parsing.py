import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Вежливый скрипт")
    parser.add_argument("name", help="Имя")
    parser.add_argument("-s", "--surname", help="Фамилия")
    # Новый аргумент.
    parser.add_argument(
        "-c",
        "--city",
        help="Город",
        choices=["Chekhov", "Dublin", "Minsk", "Simbirsk"],
    )
    args = parser.parse_args()
    parts = []
    parts.append(f"Hello, {args.name}")
    if args.surname is not None:
        parts.append(args.surname)
    # Новое условие для вывода города.
    if args.city is not None:
        parts.append(f"from {args.city}")
    print(*parts)
