import argparse

from controller.Controller import MusicController
from controller.Interface import MusicInterface


def main():
    choices = ["add", "get", "update", "delete", "list", "recommend"]

    parser = argparse.ArgumentParser(
        prog="Pyductor",
        description="Generating music to help you choose what to play",
        epilog="Enjoy your music!",
    )
    parser.add_argument(
        "-c",
        "--command",
        required=False,
        help="The command to be executed, choices are: add, get, update, delete, list",
        metavar="command",
        type=str,
        choices=choices,
    )
    args = parser.parse_args()

    cmd = args.command

    interface = MusicInterface(args, cmd)

    while cmd not in choices:
        cmd = input(f"Enter a valid command ({choices}): ")
    if cmd == "add":
        interface.add_music()
    elif cmd == "get":
        interface.get_music()
    elif cmd == "update":
        interface.update_music()
    elif cmd == "delete":
        interface.delete_music()
    elif cmd == "list":
        interface.list_music()
    elif cmd == "recommend":
        interface.recommend_music()


if __name__ == "__main__":
    main()
