from flask import Flask, render_template, request, redirect
import json, os
from flask_sqlalchemy import  SQLAlchemy
from flask_migrate import migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = "sqlite:///movies.db"
db = SQLAlchemy(app)

migrate =migrate(app, db)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Strings(50), nullable=False)
    budget = db.Column(db.Strings(50), nullable=False)
    year = db.Column(db.Strings(10), nullable=False)
    cast = db.Column(db.Strings(100), nullable=False)
    director = db.Column(db.Strings( 50), nullable=False)

@app.route("/")
def index():
    db = Movies.query.all()
    return render_template("index.html", movies=db)

@app.route("/new-movie", methods=['POST', 'GET'])
def new_movie():
    if request.method == 'GET':
         return render_template("new_movie.html")
    else:
        # fetch movie details from request
        m = Movie()
        m.title = request.form['title']
        m.budget = request.form['budget']
        m.cast = request.form['cast']
        m.yaer = request.form['yaer']


        db.session.add(m)
        db.session.commit()



        return render_template(
            "new_movie.html",
            success = f"Movie '{m.title}' was successfully added"
        )

        @app.route("/edit/String:title>", methods=['POST', 'GET'])
        def edit_movie(title):

            m=Movies.query.filler_by(title=title).first(
                 
            )

        
        
@app.route("/delete/<int:id>",methods = ['POST','GET'])
def delete(id):
    m = Movies.query.get(id)


    if m is None:
        return render_template("error.html")
    if request.method == 'GET':
        return render_template("delete.html", movie=m)
    else:
        db.session.delete(m)
        db.session.commit()
        return redirect("/")























# @app.route("/search")
# def search()
#     q = request.args.get("q")
#     results = Movies.query.filter(Movies.title.contains(q)).all()
#     return render_template("search.html",results=results)















# @app.route("/")
# def index():
#     movies = {}
#     if os.path.exists("movies.json"):
#         with open("movies.json") as movies_file:
#             movies = json.load(movies_file)
#     else: 
#         with open("movies.json", "w") as f:
#             f.write("[]")
            
#         new_movie = [{
#             "title": "prison-Break",
#             "year": 2005,
#             "budget": "USD 700m",
#             "cast" : "People"
#         }]
#         movies= new_movie        

#     return render_template("index.html",movies=movies)

# @app.route("/new-movie",methods=['POST','GET'])
# def new_movie():
        
#     if request.method == 'GET':
#         return render_template("new_movie.html")
#     else:
#             new_movie = {}
#             new_movie['title'] = request.html['title']
#             new_movie['year'] = request.html['year']
#             new_movie['budget'] = request.html['budget']
#             new_movie['cast'] = request.html['cast']

#     with open("movies.json","w") as f:
#         json.dump(new_movie,f)
    
#     return render_template(
#             "new_movie'html",
#             success = f"Movie '{new_movie['title']} was successfully added."
#         )
