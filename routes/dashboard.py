from flask import Blueprint, render_template

bp = Blueprint('dashboard', __name__)

@bp.route('/')
def index():
    """
    顯示首頁儀表板。
    取得目前的自訂財務月份起訖日期，並列出該區間的收支總結與明細。
    """
    pass
