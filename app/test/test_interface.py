import pytest
from controller.Interface import MusicInterface

args = ["list"]
cmd = "list"


class TestMusicInterface:
    i = MusicInterface(args, cmd)

    def test_interface_build(self):
        assert self.i.controller is not None, "No controller"

    def test_add_music(self):
        assert self.i.add_music() is None, "add_music() did not return None"

    def test_get_music(self):
        assert self.i.get_music() is not None, "get_music() did not return music"

    def test_update_music(self):
        assert self.i.update_music() is None, "update_music() did not return None"

    def test_list_music(self):
        assert self.i.list_music() is not None, "list_music() did not return music"
