"""All classes are here"""

import re


class User:
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

    def get_info(self):
        return {
            "id": self.id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "email": self.email,
            "total_reactions": self.total_reacions,
            "posts": [post.id for post in self.posts],
        }


class Post:
    def __init__(self, author_id, text, post_id):
        self.id = post_id
        self.author_id = author_id
        self.text = text
        self.reactions = []

    def get_info(self):
        return {
            "id": self.id,
            "author_id": self.author_id,
            "text": self.text,
            "reactions": [reaction.reaction for reaction in self.reactions],
        }


class Reaction:
    def __init__(self, user_id, reaction):
        self.reaction = reaction
        self.user_id = user_id
