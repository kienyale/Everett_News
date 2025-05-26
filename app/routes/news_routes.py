from flask import Blueprint, render_template, redirect, url_for
from app.models.news import News
from app.services.scraper import NewsScraper
from datetime import datetime
from app.models.meeting import Meeting
from app import db
import json

bp = Blueprint('news', __name__)

@bp.route('/')
def index():
    try:
        news_items = News.query.order_by(News.published_date.desc()).all()
        meeting = Meeting.query.order_by(Meeting.date.desc()).first()  # Get the latest meeting
        
        if meeting and meeting.key_topics:
            # If meeting exists and has key_topics, use them
            meeting_data = meeting
        else:
            # If no meeting exists or no key_topics, create a default dictionary
            meeting_data = {
                'key_topics': ['Budget Review', 'Infrastructure Projects', 'Community Events'],
                'date': datetime.now().strftime('%Y-%m-%d'),
                'time': '14:00',
                'location': 'City Hall',
                'agenda_url': None,
                'minutes_url': None,
                'presentations_url': None,
                'ai_summary': 'No summary available for this meeting.'
            }
    except Exception as e:
        print(f"Error: {str(e)}")
        news_items = []
        meeting_data = {
            'key_topics': ['Budget Review', 'Infrastructure Projects', 'Community Events'],
            'date': datetime.now().strftime('%Y-%m-%d'),
            'time': '14:00',
            'location': 'City Hall',
            'agenda_url': None,
            'minutes_url': None,
            'presentations_url': None,
            'ai_summary': 'No summary available for this meeting.'
        }
    
    return render_template('index.html', news_items=news_items, meeting=meeting_data)

@bp.route('/refresh')
def refresh():
    scraper = NewsScraper()
    scraper.scrape_all()
    return redirect(url_for('news.index')) 