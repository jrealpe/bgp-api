'''
BGP Routes
'''

import os

from flask import jsonify, request
from flask import Blueprint

from .models import BGP


bp = Blueprint('bgp', __name__, url_prefix='')


@bp.route('/', methods=['GET'])
def bgp_list(pk=None):
    q_ip = request.args.get('ip', None)

    response = []
    try:

    except:
        response = {
            'error': True,
            'msg': 'No se pudo consultar el bgp de la ip, intente nuevamente'
        }

    return jsonify(response)
