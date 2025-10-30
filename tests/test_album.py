from lib.album import Album


"""
 when I create an album it has id, title, release_year and artist_id
 
"""
def test_construct_album():
 album = Album(1, 'Invisible Cities', 1994, 1)
 assert album.id == 1
 assert album.title =='Invisible Cities'
 assert album.release_year ==1994
 assert album.artist_id == 1
 
def test_two_identical_albums():
 album1 = Album(1, 'Invisible Cities', 1994, 1)
 album2 = Album(1, 'Invisible Cities', 1994, 1)
 assert album1 == album2
 
 """
 When we construct an artist, we expect it to be nicely formatted.
 """
def test_album_nicely_formatted():
 album1 = Album(1, 'Invisible Cities', 1994, 1)
 assert str(album1) == "Album(1, Invisible Cities, 1994, 1)"