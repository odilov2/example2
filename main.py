import classes


def main():
    name = input("name: ")

    data = {
        "name": name,
    }

    print(classes.City.insert_into(data))


if __name__ == "__main__":
    main()
