from flask import Blueprint, jsonify, abort, request
from ..models import User, db, Tweet, likes_table
import hashlib
import secrets
import sqlalchemy


def scramble(password: str):
    """Hash and salt the given password"""
    salt = secrets.token_hex(16)
    return hashlib.sha512((password + salt).encode('utf-8')).hexdigest()


bp = Blueprint('users', __name__, url_prefix='/users')


@bp.route('', methods=['GET'])  # decorator takes path and list of HTTP verbs
def index():
    users = User.query.all()  # ORM performs SELECT query
    result = []
    for u in users:
        result.append(u.serialize())  # build list of Tweets as dictionaries
    return jsonify(result)  # return JSON response


@bp.route('/<int:id>', methods=['GET'])
def show(id: int):
    u = User.query.get_or_404(id)
    return jsonify(u.serialize())


@bp.route('', methods=['POST'])
def create():
    # req body must contain user_id and content
    if 'username' not in request.json or 'password' not in request.json:
        return abort(400)
    if len(request.json['username']) < 3 or len(request.json['password']) <= 8:
        return about(400)

    # construct User
    u = User(
        username=request.json['username'],
        content=scramble(request.json['password'])
    )

    db.session.add(u)  # prepare CREATE statement
    db.session.commit()  # execute CREATE statement

    return jsonify(u.serialize())


@bp.route('/<int:id>', methods=['DELETE'])
def delete(id: int):
    u = User.query.get_or_404(id)
    try:
        db.session.delete(u)  # prepare DELETE statement
        db.session.commit()  # execute DELETE statement
        return jsonify(True)
    except:
        # something went wrong :(
        return jsonify(False)


@bp.route('/<int:id>', methods=['PATCH', 'PUT'])
def update(id: int):
    u = User.query.get_or_404(id)
    if 'username' not in request.json and 'password' not in request.json:
        return abort(400)

    if 'username' in request.json:
        if len(request.json['username']) < 3:
            return abort(400)
        u.username = request.json['username']

    if 'password' in request.json:
        if len(request.json['password']) < 8:
            return abort(400)
        u.password = request.json['password']

    try:
        db.session.commit()
        return jsonify(u.serialize())

    except:
        return jsonify(False)


@bp.route('/<int:id>/liked_tweets', methods=['GET'])
def liked_tweets(id: int):
    u = User.query.get_or_404(id)
    results = []
    for t in u.liked_tweets:
        results.append(t.serialize())
    return jsonify(results)


@bp.route('/<int:user_id>/likes', methods=['POST'])
def like(user_id: int):
    body = request.json
    if 'tweet_id' not in body:
        return abort(400)

    user = User.query.get_or_404(user_id)
    tweet = Tweet.query.get_or_404(body['tweet_id'])
    try:
        insert_likes_query = likes_table.insert().values(user_id=user.id, tweet_id=tweet.id)
        db.session.execute(insert_likes_query)
        db.session.commit()
        return jsonify(True)
    except:
        return jsonify(False)


@bp.route('/<int:user_id>/likes/<int:tweet_id>', methods=['DELETE'])
def unlike(user_id: int, tweet_id: int):
    user = User.query.get_or_404(user_id)
    tweet = Tweet.query.get_or_404(tweet_id)
    delete_like = (
        likes_table.delete()
        .where(likes_table.c.user_id == user.id)
        .where(likes_table.c.tweet_id == tweet.id)
    )
    db.session.execute(delete_like)
    db.session.commit()
    return jsonify(delete_like.compile().params)
