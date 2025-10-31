
# {{ NAME }} Route Design Recipe

# Request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone


# Request:
POST /artists

# With body parameters:
name=Wild nothing
genre=Indie

# Expected response (200 OK)
(No content)

# Then subsequent request:
GET /artists

# Expected response (200 OK)
Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing


## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Artists route
GET /artists

# Create artist route
POST /artists
  name: string
  genre: string
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# GET /artists
#  Expected response (200 OK):
"""
Artist('Pixies', 'Rock')
Artist('ABBA', 'Pop')
Artist('Taylor Swift', 'Pop') 
Artist('Nina Simone', 'Jazz')
Artist('Beyonce', 'Pop')
"""

# POST /artists
#  Parameters:
#    name: Greenday
#    genre: Rock
#  Expected response (201 Created):
"""

"""

# POST /artists
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a name and a genre for your artist
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /artists
  Expected response (200 OK):
  Expect the responsa data to include the artists
"""
def test_get_artists(web_client):
    response = web_client.get('/artists')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Artist(1, 'Pixies', 'Rock')\n" \
        "Artist(2, 'ABBA', 'Pop')\n" \
        "Artist(3, 'Taylor Swift', 'Pop')\n" \
        "Artist(4, 'Nina Simone', 'Jazz')\n" \
        "Artist(5, 'Beyonce', 'Pop')"
"""

POST /artists
  Parameters:
    name: Greenday
    genre: Rock
  Expected response (201 Created):

"""
def test_post_submit(web_client):
    response = web_client.post('/artists', data={'name': 'Greenday', 'genre': 'Rock'})
    assert response.status_code == 201
    assert response.data.decode('utf-8') == ""
    get_respose = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Artist(1, 'Pixies', 'Rock')\n" \
        "Artist(2, 'ABBA', 'Pop')\n" \
        "Artist(3, 'Taylor Swift', 'Pop')\n" \
        "Artist(4, 'Nina Simone', 'Jazz')\n" \
        "Artist(5, 'Beyonce', 'Pop')\n" \
        "Artist(6, 'Greenday', 'Rock')"

"""
# POST /artists
#  Parameters: none
#  Expected response (400 Bad Request):
#  Please provide a name and a genre for your artist
"""
def test_post_submit_with_no_params(web_client):
response = web_client.post('/artists')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "Please provide a name and a genre for your artist"
    get_respose = web_client.get('/artists')
    assert get_response.status_code == 200
    assert get_response.data.decode('utf-8') == "" \
        "Artist(1, 'Pixies', 'Rock')\n" \
        "Artist(2, 'ABBA', 'Pop')\n" \
        "Artist(3, 'Taylor Swift', 'Pop')\n" \
        "Artist(4, 'Nina Simone', 'Jazz')\n" \
        "Artist(5, 'Beyonce', 'Pop')"
"""
```

