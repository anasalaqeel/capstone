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
        "id": movie.id,
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
            return jsonify({'success': False})
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
        error = True
        print(sys.exc_info())
    finally:
        if error:
            abort (422)
        else:
            return jsonify({"success": True, "id": get_movie.id})

@app.route("/movies/<movie_id>", methods=["DELETE"])
def movie_delete(movie_id):
    try:
        get_movie = Movies.query.filter_by(id=movie_id).first()
        Movies.delete(get_movie)
    except:
        erroe = True
        print(sys.exc_info())
    finally:
        if error:
            abort (404)
        else:
            return jsonify({'success': True, "id": get_movie.id})

# actors
#------------------------------------------------------------
@app.route("/actors")
def actors():
    get_actors = Actors.query.all()
    actors = []
    for actor in get_actors:
      actors.append({
        "id": actor.id,
        "name": actor.name,
        "age": actor.age
      })

    return jsonify({"actors": actors})

@app.route("/actors/create", methods=["POST"])
def create_actor():
    error = False
    name = request.get_json()['name']
    age = request.get_json()['age']
    try:
        added_actor = Actors(
            name=name,
            age=age
        )
        Actors.insert(added_actor)
    except:
        error = True
        print(sys.exc_info())
    finally:
        if error:
            abort (422)
            return jsonify({'success': False})
        else:
            return jsonify({'success': True})

@app.route("/actors/<actor_id>", methods=["PATCH"])
def actor_edit(actor_id):
    error = False
    get_actor = Actors.query.filter_by(id=actor_id).first()
    name = request.get_json()['name']
    age = request.get_json()['age']
    try:
        get_actor.name=name
        get_actor.age=age
        get_actor.update()
    except:
        error = True
        print(sys.exc_info())
    finally:
        if error:
            abort (422)
        else:
            return jsonify({"success": True, "id": get_actor.id})

@app.route("/actors/<actor_id>", methods=["DELETE"])
def actor_delete(actor_id):
    error = False
    try:
        get_actor = Actors.query.filter_by(id=actor_id).first()
        Actors.delete(get_actor)
    except:
        erroe = True
        print(sys.exc_info())
    finally:
        if error:
            abort (404)
        else:
            return jsonify({'success': True, "id": get_actor.id})

@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
                    "success": False, 
                    "error": 422,
                    "message": "unprocessable"
                    }), 422

@app.errorhandler(404)
def not_found(error):
    return jsonify({
                    "success": False, 
                    "error": 404,
                    "message": "resource not found"
                    }), 404


@app.errorhandler(401)
def unauthorized(error):
    return jsonify({
                    "success": False, 
                    "error": 401,
                    "message": "Unauthorized"
                    }), 401
    
@app.errorhandler(500)
def server_error(error):
  return jsonify({
    "success": False,
    "error": 500,
    "message": "Internal Server Error"
  }), 500

@app.errorhandler(AuthError)
def auth_error(error):
    return jsonify({
        "success": False,
        "error": error.status_code,
        "message": error.error['description']
    }), error.status_code


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
