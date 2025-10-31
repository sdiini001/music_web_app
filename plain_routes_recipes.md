
# {{ NAME }} Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# EXAMPLE

# Home route
GET /albums



# Submit message route
POST /albums
  title: string
  release_year: string (number)
  artist_id: string (number)
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# EXAMPLE

# GET /albums
#  Expected response (200 OK):
"""
Album(1, 'Album Title 1',2000, 2)
Album(2, 'Album Title 2', 2003, 3)
Album(3, 'Album Title 3', 1998, 3)
Album(4, 'Album Title 4', 1989, 1)
"""


# POST /albums
#  Parameters:
#    title: 'Album Title 5'
#    release_year: 1956
#    artist_id: 2
#  Expected response (201 Created):
"""

"""

# POST /albums
#  Parameters: none
#  Expected response (400 Bad Request):
"""
Please provide a title, release_year and artist_id
"""
```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /albums
  Expected response (200 OK):
  
"""
def test_get_albums(web_client):
    response = web_client.get('/albums')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == '

Album(1, 'Album Title 1',2000, 2)
Album(2, 'Album Title 2', 2003, 3)
Album(3, 'Album Title 3', 1998, 3)
Album(4, 'Album Title 4', 1989, 1)

"""
POST /albums
  Parameters:
   title: 'Album Title 5'
   release_year: 1956
   artist_id: 2
   Expected response (201 Created):
"""
def test_post_albums(web_client):
    response = web_client.post('/albums', data={'title': 'Album Title 5', 'release_year': '1956' , 'artist_id': '2'})
    assert response.status_code == 201
    assert response.data.decode('utf-8') == ''
    get_response = web_client.get('/albums')
    assert get_response.status code == 200
    assert get_response.data.decode('utf-8') == 'Album(1, 'Album Title 1', 1994, 1)
Album(1, 'Album Title 1',2000, 2)
Album(2, 'Album Title 2', 2003, 3)
Album(3, 'Album Title 3', 1998, 3)
Album(4, 'Album Title 4', 1989, 1)
Album(5, 'Album Title 5', 1956, 2)



"""
POST /albums
  Parameters:
  no parameters given
   Expected response (400 Bad request):
"""
def test_post_albums_no_data_params(web_client):
    response = web_client.post('/albums')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'Please provide an album with a title, release_year and artist_id!'

```


