import os
import random
import json


class PieceNotFoundException(Exception):
    """Raised when a piece is not found in the database"""

    pass


class MusicController:
    def __init__(self):
        self.music_path = os.path.relpath("data/music.csv")
        # open file
        try:
            with open("data/music.json", "r") as music_file:
                self.music = json.load(music_file)
        # if file doesn't exist, create it, write headers and open it
        except FileNotFoundError:
            filename = "data/music.json"
            with open(filename, "w") as music_file:
                json.dump([], music_file)
                music_file.close()
            with open("data/music.json") as music_file:
                self.music = json.load(music_file)

    def add_music(self, piece):
        """
        Adds music to the music file

        Is called by the Populator class when the user wants to add new music to the file via the command line.

        Parameters
        ----------
        music : Dict
            Dictionary of the music to be added to the file
        """
        self.music.append(piece)
        with open("data/music.json", "w") as music_file:
            json.dump(self.music, music_file)

    def get_music(self, name):
        """
        Returns the music with the given id

        Parameters
        ----------
        id : int
            The id of the music to be returned

        Returns
        -------
        Dict
            The music with the given id
        """
        for piece in self.music:
            if piece["title"].lower() == name.lower():
                return piece
        raise PieceNotFoundException("Piece {} not found".format(id))

    def list_music(self):
        """
        Returns all music

        Returns
        -------
        List
            List of all music
        """
        return self.music

    def get_recommendation(self):
        """
        Returns a random piece of music

        Returns
        -------
        Dict
            A random piece of music
        """
        return random.choice(self.music)

    def delete_music(self, name):
        """
        Deletes the music with the given id

        Parameters
        ----------
        id : int
            The id of the music to be deleted
        """
        for piece in self.music:
            if piece["title"] == name:
                self.music.remove(piece)
                with open("data/music.json", "w") as music_file:
                    json.dump(self.music, music_file)
                return
        raise PieceNotFoundException("Piece {} not found".format(id))

    def update_music(self, piece):
        """
        Updates the music with the given id

        Parameters
        ----------
        id : int
            The id of the music to be updated
        music : Dict
            The music to be updated
        """
        for i, p in enumerate(self.music):
            if p["title"] == piece["title"]:
                self.music[i] = piece
                with open("data/music.json", "w") as music_file:
                    json.dump(self.music, music_file)
                return
        raise PieceNotFoundException("Piece {} not found".format(id))


if __name__ == "__main__":
    c = MusicController()
    print(c.music)
