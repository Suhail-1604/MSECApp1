from flask import Blueprint
from auth import hod_required

bp = Blueprint('hod', __name__, url_prefix='/hod')


@bp.get('/')
@hod_required
def check():
    return 'success!'