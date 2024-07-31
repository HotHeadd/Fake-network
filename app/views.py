from app import app, USERS, POSTS, models
from flask import request, Response
import json
from http import HTTPStatus


@app.post("/users/create")
def new_user():
    global current_id
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
            json.dumps(
                {
                    "id": user.id,
                    "first_name": user.first_name,
                    "last_name": user.last_name,
                    "email": user.email,
                    "total_reactions": user.total_reacions,
                    "posts": [],
                }
            ),
            status=HTTPStatus.CREATED,
            mimetype="application/json",
        )
    return response


# TODO: get user info by user id
# TODO: create post (by user id)
# TODO: get post info by its id
# TODO: add a reaction to a post (by a post id)
# TODO: get all user post sorted by amount of reaction (by user id)
# TODO: get all users sorted by amount of reactions
# TODO: get graph of users sorted by
