from flask import Flask

app = Flask(__name__)

USERS = []  # list of all users in runtime
POSTS = []  # list of all posts

from app import views
from app import models
