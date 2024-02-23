from flask import Blueprint, request, url_for, redirect, jsonify, make_response
from Models import Hod
from flask_jwt_extended import JWTManager, current_user, jwt_required, set_access_cookies

bp = Blueprint('auth', __name__)


    
def hod_required():
    def decorator(f):
        @jwt_required
        def wraps(*args, **kwargs):
            if current_user.__table_name__ != 'hod':
                return redirect('unauthorized')
            return f(*args, **kwargs)
        return wraps
    return decorator

def student_required():
    
    def decorator(f):
        @jwt_required
        def wraps(*args, **kwargs):
            if current_user.role != 'student':
                return redirect('unauthorized')
            return f(*args, **kwargs)
        return wraps
    return decorator

@bp.post('/hod/login')
def login():
    data = request.get_json()
    
    if user and user.password == data.get('password'):
        return jsonify(error = 'invalid credential'), 400
    user = Hod.query.filter_by(username = data.get('username'))
    if 'username' and 'password' not in data:
        res = make_response(redirect(url_for('hod.dashboard')))
        set_access_cookies(res)
        return res
    return jsonify(error = 'User or Password Not Found')

    
@bp.post('/student/login')
def login():
    data = request.get_json()
    if data == None:
        return 'invalid credentials', 400
    
    return redirect('/students/')