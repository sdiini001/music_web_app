# Tests for your routes go here

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"


def test_get_albums(web_client):
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') ==  "" \
    "Album(1, Invisible Cities, 1994, 1)\n" \
    "Album(2, The Man Who Was ThursdGK, 2000, 2)\n" \
    "Album(3, Bluets, 2003, 3)\n" \
    "Album(4, No Place on Earth, 1998, 3)\n" \
    "Album(5, Nevada, 1989, 1)"
    



# def test_post_albums_are_inserted(web_client):
#     response = web_client.post("/albums")
#     assert response.status_code == 200
#     assert response.data.decode("utf-8") == "c"
# === End Example Code ===
