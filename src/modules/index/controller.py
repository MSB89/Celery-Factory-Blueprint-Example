from flask import Blueprint

from src.modules.index.views.IndexView import IndexView

index_bp = Blueprint('index', __name__, template_folder='templates')

index_bp.add_url_rule('/', view_func=IndexView.as_view('index'))
