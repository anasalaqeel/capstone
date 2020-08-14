from flask import Flask, request, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from database.models import setup_db, Movies, Actors
import sys

app = Flask(__name__)
setup_db(app)


# movies
#------------------------------------------------------------
@app.route("/movies")
def movies():
    get_movies = Movies.query.all()
    movies = []
    for movie in get_movies:
      movies.append({
        "title": movie.title,
        "releaseDate": movie.release_date
      })

    return jsonify({"movies": movies})

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

@app.route("/movies/<movie_id>", methods=["PATCH"])
def movie_edit(movie_id):
  error = False
  get_movie = Movies.query.filter_by(id=movie_id).first()
  title = request.get_json()['title']
  release_date = request.get_json()['releaseDate']
  try:
        get_movie.title=title
        get_movie.release_date=release_date
        get_movie.update()
  except:
      erroe = True
      print(sys.exc_info())
  finally:
      if error:
          abort (422)
      else:
          return jsonify({"success": True, "id": get_movie.id})

# actors
#------------------------------------------------------------



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
