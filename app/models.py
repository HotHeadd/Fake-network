"""All classes are here"""

import re


class User:
    # TODO: user class
    def __init__(self, first_name, last_name, email, his_id):
        self.id = his_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.total_reacions = 0
        self.posts = []

    @staticmethod
    def is_valid_email(email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)


class Post:
    # TODO: post class
    pass


class Reaction:
    # TODO: reaction class
    pass
