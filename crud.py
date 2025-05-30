"""CRUD operations."""

from model import db, User, Movie, Rating, connect_to_db


def create_user(email, password):
    """Create and return a new user."""

    user = User(email= email, password= password)

    return user

def get_users():
    """Get ALL Users"""

    return User.query.all()

def get_user_by_id(user_id):

    return User.query.get(user_id)

def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def create_movie(title, overview, release_date, poster_path):
    """Create and return a new movie"""

    movie = Movie(title=title, overview=overview, release_date=release_date, poster_path=poster_path)

    return movie

def get_movies():
    """Get All Movies"""

    return Movie.query.all()

def get_movie_by_id(movie_id):

    return Movie.query.get(movie_id)
    




def create_rating(user, movie, score):
    """Create and return a new rating"""

    rating = Rating(user=user, movie=movie, score=score)

    return rating


# new_user = create_user('test@t.com', 'pass123')
# new_movie = create_movie(...)

# db.session.add(new_user)
# db.session.add(new_movie)
# db.session.commit()

# new_rating = create_rating(new_user, new_movie, 4)
















if __name__=='__main__':
    from server import app
    connect_to_db(app)
    