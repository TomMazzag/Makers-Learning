import os
from flask import Flask, request, render_template, redirect, url_for
from lib.database_connection import get_flask_database_connection
from lib.user import User
from lib.user_repository import UserRepository
from lib.post import Post
from lib.post_repository import PostRepository

# Create a new Flask app
app = Flask(__name__)

@app.route('/chitter')
def get_menu():
    return render_template('index.html')


@app.route('/chitter/post/new')
def new_post():
    return render_template('new_post.html')

@app.route('/chitter', methods = ['POST'])
def add_new_post():
    connection = get_flask_database_connection(app)
    repo = PostRepository(connection)
    content = request.form['content']
    user_id = request.form['user_id']
    post = Post(None,
                content,
                user_id)
    repo.create(post)
    return redirect('/chitter')

@app.route('/chitter/login')
def get_user():
    return render_template('login.html')

@app.route('/chitter/signup')
def add_user():
    return render_template('signup.html')

#Only runs if ran through terminal on port 5001
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

