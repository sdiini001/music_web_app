import os
from flask import Flask, request
from lib.database_connection import get_flask_database_connection
from example_routes import apply_example_routes
from lib.album import Album
from lib.album_repository import AlbumRepository
from lib.artist_repository import ArtistRepository
# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# == Example Code Below ==
# apply_example_routes(app)

# GET /emoji
# Returns a emojiy face
# Try it:
#   ; curl http://127.0.0.1:5001/emoji
@app.route('/emoji', methods=['GET'])
def get_emoji():
    return ":)"

@app.route('/albums', methods=['GET'])
def get_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    return "\n".join(f'{album}' for album in repository.all())
    
        
@app.route('/albums', methods=["POST"])
def post_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = Album(None, request.form['title'],  request.form['release_year'],  request.form['artist_id'])
    repository.create(album)
    return "", 201

@app.route('/artists', methods=['GET'])
def get_artists():
    connection = get_flask_database_connection(app)
    repository = ArtistRepository(connection)
    return "\n".join(f'{artist}' for artist in repository.all())

# @app.route('/albums', methods=['POST'])
# def post_albums(id):
#     albums = [{'title': 'Voyage', 'release_year':'2022','artist_id': '2'}]




# This imports some more example routes for you to see how they work
# You can delete these lines if you don't need them.
from example_routes import apply_example_routes
apply_example_routes(app)

# == End Example Code ==

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

