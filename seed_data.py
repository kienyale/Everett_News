from app import create_app, db
from app.models.news import News
from datetime import datetime

def seed_database():
    app = create_app()
    with app.app_context():
        # First, create all tables
        db.create_all()
        
        # Check if we already have data
        if News.query.first() is None:
            # Create dummy news items
            dummy_news = [
                {
                    'title': 'City Council Approves New Park Development',
                    'content': 'The Everett City Council has approved plans for a new community park...',
                    'url': 'https://example.com/news/1',
                    'published_date': datetime(2024, 3, 1),
                    'source': 'Everett News'
                },
                {
                    'title': 'Local School Budget Increase Approved',
                    'content': 'In a unanimous decision, the council voted to increase school funding...',
                    'url': 'https://example.com/news/2',
                    'published_date': datetime(2024, 3, 5),
                    'source': 'Everett Education News'
                },
                {
                    'title': 'New Transportation Initiative Launched',
                    'content': 'The city has launched a new program to improve public transportation...',
                    'url': 'https://example.com/news/3',
                    'published_date': datetime(2024, 3, 10),
                    'source': 'Everett Transit Authority'
                }
            ]
            
            # Add each news item to the database
            for news_data in dummy_news:
                news = News(
                    title=news_data['title'],
                    content=news_data['content'],
                    url=news_data['url'],
                    published_date=news_data['published_date'],
                    source=news_data['source']
                )
                db.session.add(news)
            
            # Commit the changes
            db.session.commit()
            print("Dummy data has been added to the database!")
        else:
            print("Database already contains data!")

if __name__ == '__main__':
    seed_database() 