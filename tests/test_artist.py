from lib.artist import Artist

"""
When I create an artist
It has id, name and genre
"""

def test_construct_artist():
    artist = Artist(1, 'Pixies', 'Rock')
    assert artist.id == 1
    assert artist.name == 'Pixies'
    assert artist.genre == 'Rock'

"""
When I constrcut an artist
I expect it to be nicely formated
"""
def test_artist_nicely_formated():
    artist = Artist(1, 'Pixies', 'Rock')
    assert str(artist) == "Artist(1, Pixies, Rock)"

"""
When I compare two identical artists
They are the same
"""

def test_two_identical_artists():
    artist_1 = Artist(1, 'Pixies', 'Rock')
    artist_2 = Artist(1, 'Pixies', 'Rock')
    assert artist_1 == artist_2