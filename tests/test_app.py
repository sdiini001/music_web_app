# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"


def test_get_albums(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') ==  "" \
    "Album(1, Album Title 1, 1994, 1)\n" \
    "Album(2, Album Title 2, 2000, 2)\n" \
    "Album(3, Album Title 3, 2003, 3)\n" \
    "Album(4, Album Title 4, 1998, 3)\n" \
    "Album(5, Album Title 5, 1989, 1)"
    


def test_post_albums(db_connection, web_client):
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.post('/albums', data={'title': 'Album Title 6', 'release_year': '1956' , 'artist_id': '2'})
    assert response.status_code == 201
    assert response.data.decode('utf-8') == ''
    get_response = web_client.get('/albums')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
    "Album(1, Album Title 1, 1994, 1)\n" \
    "Album(2, Album Title 2, 2000, 2)\n" \
    "Album(3, Album Title 3, 2003, 3)\n" \
    "Album(4, Album Title 4, 1998, 3)\n" \
    "Album(5, Album Title 5, 1989, 1)\n" \
    "Album(6, Album Title 6, 1956, 2)"

def test_get_artists(web_client, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Artist(1, Pixies, Rock)\n" \
        "Artist(2, ABBA, Pop)\n" \
        "Artist(3, Taylor Swift, Pop)\n" \
        "Artist(4, Nina Simone, Jazz)\n" \
        "Artist(5, Beyonce, Pop)"
        
def test_post_artists(web_client, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.post('/artists', data={'name': 'Greenday', 'genre': 'Rock'})
    assert response.status_code == 201
    assert response.data.decode('utf-8') == ""
    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Artist(1, Pixies, Rock)\n" \
        "Artist(2, ABBA, Pop)\n" \
        "Artist(3, Taylor Swift, Pop)\n" \
        "Artist(4, Nina Simone, Jazz)\n" \
        "Artist(5, Beyonce, Pop)\n" \
        "Artist(6, Greenday, Rock)"


def test_post_artists_with_no_params(web_client, db_connection):
    db_connection.seed("seeds/albums_table.sql")
    response = web_client.post('/artists')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Please provide a name and a genre for your artist"
    get_response = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Artist(1, Pixies, Rock)\n" \
        "Artist(2, ABBA, Pop)\n" \
        "Artist(3, Taylor Swift, Pop)\n" \
        "Artist(4, Nina Simone, Jazz)\n" \
        "Artist(5, Beyonce, Pop)"