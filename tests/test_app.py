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
