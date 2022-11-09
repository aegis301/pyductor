import pytest
from controller.Interface import MusicInterface


class TestMusicInterface:
    i = MusicInterface()

    def test_interface_build(self):
        assert self.i.controller is not None, "No controller"
