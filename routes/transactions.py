from flask import Blueprint, request, redirect, url_for, render_template

bp = Blueprint('transactions', __name__, url_prefix='/transactions')

@bp.route('/new', methods=['GET'])
def new():
    """
    顯示新增收支紀錄的表單。
    需提供可用的分類清單給下拉選單使用。
    """
    pass

@bp.route('/new', methods=['POST'])
def create():
    """
    接收新增收支表單資料並寫入資料庫。
    成功後重導向至首頁儀表板。
    """
    pass

@bp.route('/<int:id>/edit', methods=['GET'])
def edit(id):
    """
    顯示編輯收支紀錄的表單，並帶入該筆紀錄的原始資料。
    """
    pass

@bp.route('/<int:id>/edit', methods=['POST'])
def update(id):
    """
    接收編輯收支表單資料並更新資料庫中的對應紀錄。
    成功後重導向至首頁儀表板。
    """
    pass

@bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    """
    刪除指定的收支紀錄。
    成功後重導向至首頁儀表板。
    """
    pass
