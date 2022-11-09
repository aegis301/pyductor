import pytest
from controller.Controller import MusicController, PieceNotFoundException


class TestController:
    c = MusicController()

    def test_populator_build(self):
        assert self.c.music_path == "data/music.csv", "music_path is not correct"
        assert self.c.music is not None, "No music file"

    def test_add_music(self):
        assert (
            self.c.add_music(
                {
                    "id": 1,
                    "name": "test",
                    "composer": "test",
                    "genre": "test",
                    "year": 2020,
                    "duration": 1,
                    "path": "test",
                }
            )
            is None
        ), "add_music() did not return None"

    def test_get_music(self):
        assert self.c.get_music(1) is not None, "get_music() did not return music"
        with pytest.raises(PieceNotFoundException):
            self.c.get_music("A")

    def test_list_music(self):
        assert self.c.list_music() is not None, "list_music() did not return music"

    def test_get_recommendation(self):
        assert (
            self.c.get_recommendation() is not None
        ), "get_recommendation() did not return music"
