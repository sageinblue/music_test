import json
import os

class Database:
    def __init__(self):
        self.albums = []
        self.tracks = []
        self._load_databases()

    def _load_databases(self):
        albums_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "data",
                                "albums.json")
        tracks_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                   "data",
                                   "tracks.json")
        with open(albums_file) as f:
            self.albums = json.load(f)
        with open(tracks_file) as f:
            self.tracks = json.load(f)
