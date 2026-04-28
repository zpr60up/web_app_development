from flask import Flask
from models.database import init_db
from routes import dashboard_bp, transactions_bp, reports_bp, settings_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'dev_secret_key_change_in_production'

    # 初始化資料庫
    with app.app_context():
        init_db()

    # 註冊 Blueprints
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(transactions_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(settings_bp)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, port=5000)
