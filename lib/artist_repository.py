from lib.artist import Artist

class ArtistRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM artists")
        print("!!!!!!!!!")
        print(rows)
        print("!!!!!!!!!")
        artists = []
        for row in rows:
            artist = Artist(row['id'], row['name'], row['genre'])
            artists.append(artist)
        print("*******")
        print(artists)
        print("*******")
        return artists