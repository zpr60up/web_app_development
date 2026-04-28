from flask import Blueprint, request, redirect, url_for, render_template

bp = Blueprint('settings', __name__, url_prefix='/settings')

@bp.route('/', methods=['GET'])
def index():
    """
    顯示全域設定與自訂分類管理頁面。
    包含自訂起始日設定表單與現有分類清單。
    """
    pass

@bp.route('/update', methods=['POST'])
def update():
    """
    更新系統全域設定 (例如：自訂月起始日)。
    成功後重導向至設定頁面。
    """
    pass

@bp.route('/categories', methods=['POST'])
def create_category():
    """
    建立新的自訂收支分類。
    成功後重導向至設定頁面。
    """
    pass

@bp.route('/categories/<int:id>/delete', methods=['POST'])
def delete_category(id):
    """
    刪除指定的自訂分類。
    若為系統預設分類則拒絕刪除。成功後重導向至設定頁面。
    """
    pass
