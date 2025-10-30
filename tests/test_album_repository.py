from lib.album_repository import AlbumRepository
from lib.album import Album




"""
 when I call all(), I get all the artists back from the database
"""

def test_get_all_albums(db_connection):
 db_connection.seed('seeds/albums_table.sql')
 repo = AlbumRepository(db_connection)
 assert repo.all() == [Album(1, 'Invisible Cities', 1994, 1), Album(2, 'The Man Who Was ThursdGK',2000, 2), Album(3, 'Bluets', 2003, 3), Album(4, 'No Place on Earth', 1998, 3), Album(5, 'Nevada', 1989, 1)]