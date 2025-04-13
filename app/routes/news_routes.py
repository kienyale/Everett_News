from flask import Blueprint, render_template, redirect, url_for
from app.models.news import News
from app.services.scraper import NewsScraper
from datetime import datetime

bp = Blueprint('news', __name__)

@bp.route('/')
def index():
    try:
        news_items = News.query.order_by(News.published_date.desc()).all()
    except:
        news_items = []
    return render_template('index.html', news_items=news_items)

@bp.route('/refresh')
def refresh():
    scraper = NewsScraper()
    scraper.scrape_all()
    return redirect(url_for('news.index')) 