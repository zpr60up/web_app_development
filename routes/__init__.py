from .dashboard import bp as dashboard_bp
from .transactions import bp as transactions_bp
from .reports import bp as reports_bp
from .settings import bp as settings_bp

__all__ = ['dashboard_bp', 'transactions_bp', 'reports_bp', 'settings_bp']
