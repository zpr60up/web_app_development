from flask import Blueprint, request, redirect, url_for, render_template, flash
from models.setting import Setting
from models.category import Category

bp = Blueprint('settings', __name__, url_prefix='/settings')

@bp.route('/', methods=['GET'])
def index():
    month_start_day = Setting.get('month_start_day', '1')
    categories = Category.get_all()
    return render_template('settings/index.html', month_start_day=month_start_day, categories=categories)

@bp.route('/update', methods=['POST'])
def update():
    day = request.form.get('month_start_day', '1')
    try:
        day_int = int(day)
        if 1 <= day_int <= 28:
            Setting.set('month_start_day', str(day_int))
            flash('設定更新成功', 'success')
        else:
            flash('請輸入 1 到 28 之間的數字', 'danger')
    except ValueError:
        flash('無效的輸入', 'danger')
    return redirect(url_for('settings.index'))

@bp.route('/categories', methods=['POST'])
def create_category():
    name = request.form.get('name')
    cat_type = request.form.get('type')
    if not name or cat_type not in ['income', 'expense']:
        flash('無效的分類資料', 'danger')
        return redirect(url_for('settings.index'))
    Category.create({'name': name, 'type': cat_type})
    flash('分類新增成功', 'success')
    return redirect(url_for('settings.index'))

@bp.route('/categories/<int:id>/delete', methods=['POST'])
def delete_category(id):
    if Category.delete(id):
        flash('分類刪除成功', 'success')
    else:
        flash('無法刪除預設分類', 'danger')
    return redirect(url_for('settings.index'))
