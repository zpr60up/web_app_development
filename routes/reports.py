from flask import Blueprint, render_template

bp = Blueprint('reports', __name__, url_prefix='/reports')

@bp.route('/')
def index():
    """
    顯示歷史月份報表。
    可依據月份篩選，並整理資料供前端 Chart.js 繪製圖表。
    """
    pass
