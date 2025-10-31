from lib.artist_repository import ArtistRepository
from lib.artist import Artist

"""
When I call #all
I get a list of artists back from the database
"""

def test_get_all_artists(db_connection):
    db_connection.seed('seeds/albums_table.sql')
    repo = ArtistRepository(db_connection)
    assert repo.all() == [
        Artist(1, 'Pixies', 'Rock'),
        Artist(2, 'ABBA', 'Pop'),
        Artist(3, 'Taylor Swift', 'Pop'),
        Artist(4, 'Nina Simone', 'Jazz'),
        Artist(5, 'Beyonce', 'Pop')
    ]