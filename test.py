import os
import unittest
import json
from flask import request
from flask_sqlalchemy import SQLAlchemy
from app import create_app
from database.models import setup_db, Movies, Actors



class CapstoneTestCase(unittest.TestCase):
    """This class represents the capstone test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.user_token = f"Bearer {os.environ['TESTS_TOKEN']}"
        self.database_name = "capstone_test"
        self.database_path = "postgresql://{}/{}".format('postgres:1234@localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
            self.all_movies = Movies.query.all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_200_index(self):
        res = self.client().get('/')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
    def test_404_index(self):
        res = self.client().get('/sdetrgwsedwsqbgfn')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    def test_get_movies(self):
        res = self.client().get('/movies', headers={'Authorization': self.user_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['movies'])        
    def test_401_unauthorize_movies_request(self):
        res = self.client().get('/movies', headers={'Authorization': 'edgfpfedogjk'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header must start with "Bearer".')
        
    def test_get_actors(self):
        res = self.client().get('/actors', headers={'Authorization': self.user_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['actors'])
    def test_401_unauthorize_actors_request(self):
        res = self.client().get('/actors', headers={'Authorization': 'edgfpfedogjk'})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Authorization header must start with "Bearer".')

    def test_200_add_movie(self):
        movies_before = Movies.query.all()
        movie = {"title": "test movie title example","releaseDate": "05/08/2020"}
        res = self.client().post('/movies/create', json=movie, headers={'Authorization': self.user_token})
        data = json.loads(res.data)
        movies_after = Movies.query.all()
        self.assertTrue(len(movies_after) - len(movies_before) == 1)
        self.assertEqual(res.status_code, 200)
    def test_422_add_movie(self):
        movies_before = Movies.query.all()
        movie = {"title": None,"releaseDate": "05/08/2020"}
        res = self.client().post('/movies/create', json=movie, headers={'Authorization': self.user_token})
        data = json.loads(res.data)
        movies_after = Movies.query.all()
        self.assertTrue(len(movies_after) - len(movies_before) == 0)
        self.assertEqual(res.status_code, 422)

    def test_200_add_actor(self):
        actors_before = Actors.query.all()
        actor = {"name": "test Hey its my name!","age": 99}
        res = self.client().post('/actors/create', json=actor, headers={'Authorization': self.user_token})
        data = json.loads(res.data)
        actors_after = Actors.query.all()
        self.assertTrue(len(actors_after) - len(actors_before) == 1)
        self.assertEqual(res.status_code, 200)
    def test_422_add_actor(self):
        actors_before = Actors.query.all()
        actor = {"name": None,"age": 99}
        res = self.client().post('/actors/create', json=actor, headers={'Authorization': self.user_token})
        data = json.loads(res.data)
        actors_after = Actors.query.all()
        self.assertTrue(len(actors_after) - len(actors_before) == 0)
        self.assertEqual(res.status_code, 422)

    def test_200_edit_movie(self):
        movie = {"title": "test movie edit title example","releaseDate": "05/10/2020"}
        res = self.client().patch('/movies/1', json=movie, headers={'Authorization': self.user_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
    def test_422_edit_movie(self):
        movie = {"title": None,"releaseDate": "05/10/2020"}
        res = self.client().patch('/movies/1', json=movie, headers={'Authorization': self.user_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
    
    def test_200_edit_actor(self):
        actor = {"name": "test edited Hey its my name!","age": 33}
        res = self.client().patch('/actors/1', json=actor, headers={'Authorization': self.user_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
    def test_422_edit_actor(self):
        actor = {"name": None,"age": 59}
        res = self.client().patch('/actors/1', json=actor, headers={'Authorization': self.user_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)

    def test_200_delete_movie(self):
        res = self.client().delete('/movies/2', headers={'Authorization': self.user_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
    def test_404_delete_movie(self):
        res = self.client().delete('/movies/999999', headers={'Authorization': self.user_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

    def test_200_delete_actor(self):
        res = self.client().delete('/actors/2', headers={'Authorization': self.user_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
    def test_404_delete_actor(self):
        res = self.client().delete('/actors/999999', headers={'Authorization': self.user_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()