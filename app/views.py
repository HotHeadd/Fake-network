from app import app, USERS, POSTS, models
from flask import request, Response
import json
from http import HTTPStatus


@app.post("/users/create")
def new_user():
    data = request.get_json()
    first_name = data["first_name"]
    last_name = data["last_name"]
    email = data["email"]
    if not models.User.is_valid_email(email):
        response = Response(
            json.dumps({"message": "wrong email format!"}),
            status=HTTPStatus.BAD_REQUEST,
        )
    else:
        user = models.User(first_name, last_name, email, len(USERS))
        USERS.append(user)
        response = Response(
            json.dumps(user.get_info()),
            status=HTTPStatus.CREATED,
            mimetype="application/json",
        )
    return response


@app.get("/users/<int:user_id>")
def get_user(user_id):
    if user_id < 0 or user_id >= len(USERS):
        response = Response(status=HTTPStatus.BAD_REQUEST)
    else:
        user = USERS[user_id]
        response = Response(
            json.dumps(user.get_info()),
            status=HTTPStatus.OK,
            mimetype="application/json",
        )
    return response


@app.post("/posts/create")
def new_post():
    data = request.get_json()
    author_id = data["author_id"]
    text = data["text"]
    if author_id < 0 or author_id >= len(USERS):
        response = Response(status=HTTPStatus.BAD_REQUEST)
    else:
        post = models.Post(author_id, text, len(POSTS))
        POSTS.append(post)
        author = USERS[author_id]
        author.add_post(post)
        response = Response(
            json.dumps(post.get_info()),
            status=HTTPStatus.CREATED,
            mimetype="application/json",
        )
    return response


@app.get("/posts/<int:post_id>")
def get_post(post_id):
    if post_id < 0 or post_id >= len(POSTS):
        response = Response(status=HTTPStatus.BAD_REQUEST)
    else:
        post = POSTS[post_id]
        response = Response(
            json.dumps(post.get_info()),
            status=HTTPStatus.OK,
            mimetype="application/json",
        )
    return response


@app.post("/posts/<int:post_id>/reaction")
def add_reaction(post_id):
    if post_id < 0 or post_id >= len(POSTS):
        response = Response(status=HTTPStatus.BAD_REQUEST)
    else:
        post = POSTS[post_id]
        data = request.get_json()
        user_id = data["user_id"]
        reaction = data["reaction"]
        if user_id < 0 or user_id >= len(USERS):
            return Response(status=HTTPStatus.BAD_REQUEST)
        post.add_reaction(user_id, models.Reaction(user_id, reaction))
        response = Response(
            status=HTTPStatus.OK,
        )
    return response


# TODO: get all user post sorted by amount of reaction (by user id)
# TODO: get all users sorted by amount of reactions
# TODO: get graph of users sorted by
