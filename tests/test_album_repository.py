from lib.album_repository import AlbumRepository
from lib.album import Album




"""
 when I call all(), I get all the artists back from the database
"""

def test_get_all_albums(db_connection):
 db_connection.seed('seeds/albums_table.sql')
 repo = AlbumRepository(db_connection)
 assert repo.all() == [Album(1, 'Album Title 1', 1994, 1), Album(2, 'Album Title 2',2000, 2), Album(3, 'Album Title 3', 2003, 3), Album(4, 'Album Title 4', 1998, 3), Album(5, 'Album Title 5', 1989, 1)]