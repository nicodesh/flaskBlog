from flask import abort

class Post():

    POSTS = [
        {'id': 1, 'title': 'First post', 'content': 'This is my first post'},
        {'id': 2, 'title': 'Second post', 'content': 'This is my first post'},
        {'id': 3, 'title': 'Third post', 'content': 'This is my first post'},
    ]

    @classmethod
    def all(cls):
        """ Fetch all posts """
        return cls.POSTS

    @classmethod
    def find(cls, id):
        """ Fetch single post """
        try:
            return cls.POSTS[int(id) - 1]
        except IndexError:
            abort(404)