from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests
import os

app = Flask(__name__)
# if "RuntimeError: Working outside of application context.", add the line below:
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///movies-collection.db"
# Optional: But it will silence the deprecation warning in the console.
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SECRET_KEY'] = os.environ["secret_key"]
Bootstrap(app)


# create table
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float())
    ranking = db.Column(db.Integer)
    review = db.Column(db.String(250))
    img_url = db.Column(db.String(250), nullable=False)


db.create_all()

# movie = Movie(
#     title="Blabla",
#     year=2001,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=8.3,
#     ranking=9,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(movie)
# db.session.commit()


class EditForm(FlaskForm):
    rating = FloatField(label="Your rating out of 10 e.g. 7.3", validators=[DataRequired()])
    review = StringField(label="Your review", validators=[DataRequired()])
    submit = SubmitField(label="Done")


class AddForm(FlaskForm):
    title = StringField(label="Movie Title", validators=[DataRequired()])
    submit = SubmitField(label="Add movie")


@app.route("/")
def home():
    # This line creates a list of all the movies sorted by rating
    all_movies = Movie.query.order_by(Movie.rating).all()

    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/edit/<int:id>", methods=["POST", "GET"])
def edit(id):
    movie_to_update = db.session.execute(db.select(Movie).filter_by(id=id)).scalar_one()
    edit_form = EditForm()
    if edit_form.validate_on_submit():
        movie_to_update.rating = edit_form.rating.data
        movie_to_update.review = edit_form.review.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit.html", movie=movie_to_update, form=edit_form)


@app.route("/delete/<int:id>", methods=['GET'])
def delete(id):
    if request.method == "GET":
        movie_to_delete = db.session.execute(db.select(Movie).filter_by(id=id)).scalar_one()
        db.session.delete(movie_to_delete)
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/add", methods=["POST", "GET"])
def add():
    add_form = AddForm()
    if add_form.validate_on_submit():
        title = add_form.title.data
        tmdb_url = "https://api.themoviedb.org/3/search/movie"
        params = {
            "api_key": os.environ["api_key"],
            "query": title
        }
        response = requests.get(tmdb_url, params=params)
        data = response.json()["results"]
        return render_template("select.html", options=data)
    return render_template("add.html", form=add_form)


@app.route("/find")
def find_movie():
    movie_api_id = request.args.get("id")
    if movie_api_id:
        movie_api_url = f"https://api.themoviedb.org/3/movie/{movie_api_id}"
        # The language parameter is optional, if you were making the website for a different audience
        # e.g. Hindi speakers then you might choose "hi-IN"
        response = requests.get(movie_api_url, params={"api_key": os.environ["api_key"], "language": "en-US"})
        data = response.json()
        new_movie = Movie(
            title=data["title"],
            # The data in release_date includes month and day, we will want to get rid of.
            year=data["release_date"].split("-")[0],
            img_url=f"https://image.tmdb.org/t/p/w500{data['poster_path']}",
            description=data["overview"]
        )
        db.session.add(new_movie)
        db.session.commit()
        return redirect(url_for("edit", id=new_movie.id))


if __name__ == '__main__':
    app.run(debug=True)
