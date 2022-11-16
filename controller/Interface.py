from .Controller import MusicController


class MusicInterface(object):
    def __init__(self, args, cmd):
        self.controller = MusicController()
        self.args = args
        self.cmd = cmd

    def add_music(self):
        piece = {}

        piece["title"] = input("Enter the title of the piece: ")
        piece["musician"] = input("Enter the composer of the piece: ")
        piece["genre"] = input(
            "Enter the genre of the piece as a comma seperated list: "
        ).split()

        self.controller.add_music(piece)

    def get_music(self):
        name = input("Enter the name of the piece: ")
        piece = self.controller.get_music(name)
        print(piece)

    def update_music(self):
        pass

    def delete_music(self):
        pass

    def list_music(self):
        music = self.controller.list_music()
        print(music)
