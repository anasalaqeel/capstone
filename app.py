from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from database.models import setup_db, Movies, Actors
import sys

app = Flask(__name__)
setup_db(app)


# movies
#------------------------------------------------------------
@app.route("/movies")
def index():
    get_movies = Movies.query.all()
    print(get_movies)
    return 'Hello World'

@app.route("/movies/create", methods=["POST"])
def create_movie():
    error = False
    title = request.get_json()['title']
    release_date = request.get_json()['releaseDate']
    try:
        added_movie = Movies(
            title=title,
            release_date=release_date
        )
        Movies.insert(added_movie)
    except:
        error = True
        print(sys.exc_info())
    finally:
        if error:
            abort (422)
        else:
            return jsonify({'success': True})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
