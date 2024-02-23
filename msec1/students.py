from flask import Blueprint, request, url_for, redirect, jsonify


bp = Blueprint('students', __name__, url_prefix='/students')


@bp.get('/')
def get_students():
    ...