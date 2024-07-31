from app import app, USERS, POSTS, models
from flask import request, Response
import json
import re
from http import HTTPStatus

current_id = 1


@app.post("/users/create")
def new_user():
    global current_id
    data = request.get_json()
    first_name = data["first_name"]
    last_name = data["last_name"]
    email = data["email"]
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        response = Response(
            json.dumps({"message": "wrong email format!"}),
            status=HTTPStatus.IM_A_TEAPOT,
            mimetype="application/json",
        )
    else:
        user = models.User(first_name, last_name, email, current_id)
        USERS.append(user)
        current_id += 1
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
