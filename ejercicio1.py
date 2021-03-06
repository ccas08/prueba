DATA = [
    {
        "name": "Facundo",
        "age": 72,
        "organization": "Microsoft",
        "language": "python",
    },
    {
        "name": "Luisana",
        "age": 33,
        "organization": "Google",
        "language": "javascript",
    },
    {
        "name": "Héctor",
        "age": 19,
        "organization": "Microsoft",
        "language": "ruby",
    },
    {
        "name": "Gabriel",
        "age": 20,
        "organization": "IBM",
        "language": "javascript",
    },
    {
        "name": "Isabella",
        "age": 30,
        "organization": "IBM",
        "language": "java",
    },
    {
        "name": "Karo",
        "age": 23,
        "organization": "Everis",
        "language": "python",
    },
    {
        "name": "Ariel",
        "age": 32,
        "organization": "Rappi",
        "language": "",
    },
    {
        "name": "Juan",
        "age": 17,
        "organization": "",
        "language": "go",
    },
    {
        "name": "Pablo",
        "age": 32,
        "organization": "Master",
        "language": "python",
    },
    {
        "name": "Lorena",
        "age": 56,
        "organization": "Accenture",
        "language": "python",
    },
]


def run():
    personas = [worker["name"] for worker in DATA if worker["language"] == "python"]
    print(personas)


if __name__ == "__main__":
    run()
