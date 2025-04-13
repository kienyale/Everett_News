from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config.settings import Config

db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__,
                template_folder='../templates',
                static_folder='../static')
    
    app.config.from_object(config_class)
    
    db.init_app(app)
    
    from app.routes import news_routes
    app.register_blueprint(news_routes.bp)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    
    return app 