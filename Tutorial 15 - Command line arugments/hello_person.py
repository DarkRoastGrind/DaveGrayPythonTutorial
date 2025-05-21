# Determine language, and output hello in the proper language.
def hello(name, lang):
    greetings = {
        "English": "Hello",
        "Spanish": "Hola",
        "German": "Hallo",
    }
    msg = f"{greetings[lang]} {name}!"
    print(msg)


# If this is the file called into main,
if __name__ == '__main__':
    # Part of python standard library.
    # Command line argument and parsing library.
    import argparse

    # Description of the argument parser.
    parser = argparse.ArgumentParser(
        description="Provides a personal greeting."
    )

    # Type py hello_person.py -h for a help message.
    parser.add_argument(
        "-n", "--name",
        metavar="name",
        required=True,
        help="The name of the person to greet."
    )

    parser.add_argument(
        "-l", "--lang",
        metavar="language",
        required=True,
        choices=["English", "Spanish", "German"],
        help="The language of the greeting."
    )

    args = parser.parse_args()
    # # Type py hello_person.py -n "name" to run.
    # msg = f"Hello {args.name}!"
    # print(msg)
    # Run the hello function.
    hello(args.name, args.lang)
