# capstone

## Capstone Project for Udacity's Full Stack Developer Nanodegree
Heroku Link: https://my-udacity-capstone-project.herokuapp.com

While running locally: http://localhost:5000

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python).

#### Virtual Enviornment

Recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

## Running the server

Before running the application locally, make the following changes in the `app.py` file in root directory:
- uncomment the line `db_drop_and_create_all()` on the initial run to setup the required tables in the database.

To run the server, execute:

```bash
export DATABASE_URL=<database-connection-url>
export FLASK_APP=app.py
flask run --reload
```

Setting the `FLASK_APP` variable to `app.py` directs flask to use the `app.py` file to find the application. 

Using the `--reload` flag will detect file changes and restart the server automatically.

## API Reference

## Getting Started
Base URL: This application can be run locally. The hosted version is at `https://my-udacity-capstone-project.herokuapp.com/`.

Authentication: This application requires authentication to perform various actions. All the endpoints require
various permissions, except the root endpoint, that are passed via the `Bearer` token.

The application has three different types of roles:
- Assistant
  - can only view the list of actors and movies.
  - has `view:actors, view:movies` permissions.
- Director
  - can perform all the actions that `Assistant` can.
  - can only create an actor and also update respective information.
  - has `add:actors, delete:actors, edit:actors, edit:movies, view:actors, view:movies` permissions.
- Producer
  - can perform all the actions that `Director` can.
  - can also add an actor or a movie, edit and delete any actor or movie.
  - has `add:actors, add:movies, delete:actors, delete:movies, edit:actors, edit:movies, get:movies, view:actors, view:movies` permissions.

## Error Handling
Errors are returned as JSON objects in the following format:
```
{
    "success": false,
    "error": 404,
    "message": "resource not found"
}
```

The API will return the following errors based on how the request fails:
 - 401: Unauthorized
 - 404: Not Found
 - 422: Unprocessable Entity
 - 500: Internal Server Error

## Endpoints

#### GET /
 - General
   - root endpoint
   - can also work to check if the api is up and running
   - is a public endpoint, requires no authentication
 
 - Sample Request
   - `https://my-udacity-capstone-project.herokuapp.com`

<details>
<summary>Sample Response</summary>

```
{
    "Status": "yay its work well"
}
```

</details>

#### GET /actors
 - General
   - gets the list of all the actors
   - requires `view:actors` permission
 
 - Sample Request
   - `https://my-udacity-capstone-project.herokuapp.com/actors`

<details>
<summary>Sample Response</summary>

```
{
    "actors": [
        {
            "age": 30,
            "id": 1,
            "name": "Hey its my name!"
        }
    ]
}
```

</details>

#### POST /actors
 - General
   - creates a new actor.
   - requires `add:actors` permission.
 
 - Request Body
   - name: string, required.
   - age: Integer, required.
 
 - Sample Request
   - `https://my-udacity-capstone-project.herokuapp.com/actors/create`
   - Request Body
     ```
        {
        "name": "Hey its my name!",
        "age": 30
        }
     ```

<details>
<summary>Sample Response</summary>

```
{
    "success": true
}
```
  
</details>

#### PATCH /actors/{actor_id}
 - General
   - updates the info for an actor
   - requires `edit:actors` permission
 
 - Request Body (at least one of the following fields required)
   - name: string, optional.
   - age: Integer, required.
 
 - Sample Request
   - `https://my-udacity-capstone-project.herokuapp.com/actors/1`
   - Request Body
     ```
       {
            "age": 32
       }
     ```

<details>
<summary>Sample Response</summary>

```
{
    "success": true,
    "id": 1
}
```
  
</details>

#### DELETE /actors/{actor_id}
 - General
   - deletes an actor
   - requires `delete:actors` permission
 
 - Sample Request
   - `https://my-udacity-capstone-project.herokuapp.com/actors/1`

<details>
<summary>Sample Response</summary>

```
{
    "success": true,
    "id": 1
}
```
  
</details>

#### GET /movies
 - General
   - gets the list of all the movies
   - requires `view:movies` permission
 
 - Sample Request
   - `https://my-udacity-capstone-project.herokuapp.com/movies`

<details>
<summary>Sample Response</summary>

```
{
    "movies": [
        {
            "id": 1,
            "releaseDate": "08/02/2019",
            "title": "movie title example"
        },
        {
            "id": 2,
            "releaseDate": "10/02/2019",
            "title": "another movie title example"
        }
    ]
}
```

</details>

#### POST /movies
 - General
   - creates a new movie.
   - requires `add:movies` permission.
 
 - Request Body
   - title: string, required.
   - releaseDate: integer, required.
 
 - Sample Request
   - `https://my-udacity-capstone-project.herokuapp.com/movies/create`
   - Request Body
     ```
        {
            "title": "Spider Man",
            "releaseDate": 2019,
        }
     ```

<details>
<summary>Sample Response</summary>

```
{
    "success": true
}
```
  
</details>

#### PATCH /movie/{movie_id}
 - General
   - updates the info for a movie
   - requires `edit:movies` permission
 
 - Request Body (at least one of the following fields required)
   - title: string, optional
   - releaseDate: integer, optional
 
 - Sample Request
   - `https://my-udacity-capstone-project.herokuapp.com/movies/3`
   - Request Body
     ```
       {
            "releaseDate": 2017
       }
     ```

<details>
<summary>Sample Response</summary>

```
{
    "success": true,
    "id": 3
}
```
  
</details>

#### DELETE /movies/{movie_id}
 - General
   - deletes a movie
   - requires `delete:movies` permission
 
 - Sample Request
   - `https://my-udacity-capstone-project.herokuapp.com/movies/3`

<details>
<summary>Sample Response</summary>

```
{
    "success": true,
    "id": 3
}
```
  
</details>

## Testing

### For MAC OS
For testing the backend, run the following commands (in the exact order):
```
dropdb capstone_test
createdb capstone_test
psql capstone_test < capstone.pgsql
python test.py
```
### For Windows OS
For testing the backend, run the following commands (in the exact order):
```
dropdb -U <DATABASE USER> capstone_test
createdb -U <DATABASE USER> capstone_test
psql -U <DATABASE USER> capstone_test < capstone.pgsql
py test.py
```

Alternate way: Create the db `capstone_test` using PgAdmin and copy the contents of casting.pgsql and paste them
in Query tool in PgAdmin and create the db table with records. Then, run the command for MAC OS `python test.py` or `py test.py` for Windows OS.