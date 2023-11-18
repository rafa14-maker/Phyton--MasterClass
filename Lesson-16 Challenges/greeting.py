import argparse

parser = argparse.ArgumentParser(description="Helps to greet")

parser.add_argument(
    "-n",
    "-name",
    metavar="name",
    required=True,
    dest="name",
    help="The name to greet.",
)

args = parser.parse_args()
msg = f"Hello {args.name}"


def GetName():
    return args.name
