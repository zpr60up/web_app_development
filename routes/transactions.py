from flask import Blueprint, request, redirect, url_for, render_template, flash
from models.transaction import Transaction
from models.category import Category
from datetime import date

bp = Blueprint('transactions', __name__, url_prefix='/transactions')

@bp.route('/new', methods=['GET'])
def new():
    categories = Category.get_all()
    return render_template('transactions/form.html', categories=categories, tx=None, today=date.today().strftime('%Y-%m-%d'))

@bp.route('/new', methods=['POST'])
def create():
    amount = float(request.form.get('amount', 0))
    category_id = int(request.form.get('category_id'))
    date_str = request.form.get('date')
    note = request.form.get('note', '')
    
    cat = Category.get_by_id(category_id)
    if not cat:
        flash('分類不存在', 'danger')
        return redirect(url_for('transactions.new'))
        
    Transaction.create({
        'amount': amount,
        'type': cat.type,
        'category_id': category_id,
        'date': date_str,
        'note': note
    })
    flash('新增成功', 'success')
    return redirect(url_for('dashboard.index'))

@bp.route('/<int:id>/edit', methods=['GET'])
def edit(id):
    tx = Transaction.get_by_id(id)
    if not tx:
        flash('找不到紀錄', 'danger')
        return redirect(url_for('dashboard.index'))
    categories = Category.get_all()
    return render_template('transactions/form.html', categories=categories, tx=tx)

@bp.route('/<int:id>/edit', methods=['POST'])
def update(id):
    amount = float(request.form.get('amount', 0))
    category_id = int(request.form.get('category_id'))
    date_str = request.form.get('date')
    note = request.form.get('note', '')
    
    cat = Category.get_by_id(category_id)
    if not cat:
        flash('分類不存在', 'danger')
        return redirect(url_for('transactions.edit', id=id))
        
    Transaction.update(id, {
        'amount': amount,
        'type': cat.type,
        'category_id': category_id,
        'date': date_str,
        'note': note
    })
    flash('更新成功', 'success')
    return redirect(url_for('dashboard.index'))

@bp.route('/<int:id>/delete', methods=['POST'])
def delete(id):
    Transaction.delete(id)
    flash('刪除成功', 'success')
    return redirect(url_for('dashboard.index'))
