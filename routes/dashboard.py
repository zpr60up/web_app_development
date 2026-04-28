from flask import Blueprint, render_template
from models.setting import Setting
from models.transaction import Transaction
from services.finance import FinanceService
from datetime import date

bp = Blueprint('dashboard', __name__)

@bp.route('/')
def index():
    start_day = int(Setting.get('month_start_day', '1'))
    today = date.today()
    start_date, end_date = FinanceService.calculate_custom_month_range(today, start_day)
    
    transactions = Transaction.get_by_date_range(start_date, end_date)
    
    total_income = sum(t.amount for t in transactions if t.type == 'income')
    total_expense = sum(t.amount for t in transactions if t.type == 'expense')
    balance = total_income - total_expense
    
    return render_template('dashboard/index.html', 
                           transactions=transactions,
                           total_income=total_income,
                           total_expense=total_expense,
                           balance=balance,
                           start_date=start_date,
                           end_date=end_date)
