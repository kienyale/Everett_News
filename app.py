from flask import Flask, render_template, request
from scrape import scrape_city_data
from datetime import datetime, timedelta

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route("/")
def home():
    # Get latest meeting data - we'll no longer pass video_filename 
    # since we're directly embedding in the template
    latest_meeting = {
        'title': 'Charter Commission Meeting',
        'key_topics': [
            'Downtown Revitalization Project',
            'Public Transportation Expansion',
            'Climate Action Plan Discussion',
            'Budget Approval for Q2'
        ],
        'agenda_url': '/documents/agenda-20250403.pdf',
        'minutes_url': '/documents/minutes-20250403.pdf',
        'presentations_url': '/documents/presentations-20250403.pdf',
        'ai_summary': 'The commission discussed the downtown revitalization project, focusing on pedestrian-friendly '
                     'spaces and affordable housing. The transportation expansion proposal was approved with '
                     'unanimous support, while the climate action plan was deferred for further review.'
    }
    
    # Get dummy news items
    news_items = [
        {
            'title': 'City Council Approves New Park Development',
            'content': 'The Everett City Council has approved plans for a new community park...',
            'url': 'https://example.com/news/1',
            'published_date': datetime.now() - timedelta(days=2),
            'source': 'Everett News'
        },
        {
            'title': 'Local School Budget Increase Approved',
            'content': 'In a unanimous decision, the council voted to increase school funding...',
            'url': 'https://example.com/news/2',
            'published_date': datetime.now() - timedelta(days=5),
            'source': 'Everett Education News'
        },
        {
            'title': 'New Transportation Initiative Launched',
            'content': 'The city has launched a new program to improve public transportation...',
            'url': 'https://example.com/news/3',
            'published_date': datetime.now() - timedelta(days=10),
            'source': 'Everett Transit Authority'
        }
    ]
    
    return render_template("index.html", meeting=latest_meeting, news_items=news_items)

@app.route("/city", methods=["POST"])
def city():
    location = request.form["location"]
    data = scrape_city_data(location)
    if data:
        return render_template("city.html", **data)
    else:
        return render_template("error.html", message="City not found.")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/transparency")
def transparency():
    return render_template("transparency.html")

@app.route("/city")
def city_view():
    # Create dummy data for the city page
    dummy_data = {
        'city_name': 'Everett',
        'councilors': [
            {
                'name': 'John Smith',
                'photo': '/static/images/councilor1.jpg',
                'email': 'john.smith@everettcity.gov',
                'opinion': 'I believe we need to focus on sustainable development that benefits all residents.'
            },
            {
                'name': 'Maria Rodriguez',
                'photo': '/static/images/councilor2.jpg',
                'email': 'maria.rodriguez@everettcity.gov',
                'opinion': 'Improving public transportation is essential for our growing city.'
            },
            {
                'name': 'David Johnson',
                'photo': '/static/images/councilor3.jpg',
                'email': 'david.johnson@everettcity.gov',
                'opinion': 'We must address the housing affordability crisis facing our residents.'
            }
        ],
        'summary': 'The city council discussed the new downtown revitalization project, focusing on creating more green spaces and affordable housing units.',
        'agenda': [
            'Approval of previous meeting minutes',
            'Discussion of downtown revitalization project',
            'Vote on increased funding for public parks',
            'Public comment period',
            'Review of infrastructure budget proposal'
        ]
    }
    return render_template("city.html", **dummy_data)

@app.route("/legislation")
def legislation():
    # Create dummy legislation data
    now = datetime.now()
    dummy_legislations = [
        {
            'id': 1,
            'title': 'Downtown Revitalization Project',
            'description': 'A comprehensive plan to revitalize the downtown area by creating more green spaces, improving pedestrian access, and developing affordable housing units.',
            'type': 'ordinance',
            'status': 'approved',
            'introduction_date': now - timedelta(days=30),
            'vote_date': now - timedelta(days=7),
            'yes_votes': 4,
            'no_votes': 1,
            'abstain_votes': 0
        },
        {
            'id': 2,
            'title': 'Public Transportation Expansion',
            'description': 'Initiative to expand public transportation routes to underserved areas and increase service frequency during peak hours.',
            'type': 'resolution',
            'status': 'approved',
            'introduction_date': now - timedelta(days=45),
            'vote_date': now - timedelta(days=14),
            'yes_votes': 5,
            'no_votes': 0,
            'abstain_votes': 0
        },
        {
            'id': 3,
            'title': 'Affordable Housing Requirements',
            'description': 'Ordinance requiring new residential developments over 10 units to include at least 15% affordable housing units.',
            'type': 'ordinance',
            'status': 'pending',
            'introduction_date': now - timedelta(days=15),
            'vote_date': None,
            'yes_votes': 0,
            'no_votes': 0,
            'abstain_votes': 0
        },
        {
            'id': 4,
            'title': 'Climate Action Plan',
            'description': 'Comprehensive plan to reduce city carbon emissions by 50% by 2030 and achieve carbon neutrality by 2050.',
            'type': 'resolution',
            'status': 'deferred',
            'introduction_date': now - timedelta(days=60),
            'vote_date': now - timedelta(days=30),
            'yes_votes': 2,
            'no_votes': 1,
            'abstain_votes': 2
        }
    ]
    return render_template("legislation.html", legislations=dummy_legislations)

@app.route("/councilors")
def councilors():
    # Create dummy councilor data
    dummy_councilors = [
        {
            'id': 1,
            'name': 'John Smith',
            'photo_url': 'https://randomuser.me/api/portraits/men/72.jpg',
            'email': 'john.smith@everettcity.gov',
            'position': 'Council President',
            'bio': 'John has served on the council for 8 years and focuses on sustainable development.',
            'committees': 'Budget, Planning',
            'term_start': datetime(2022, 1, 1),
            'term_end': datetime(2026, 12, 31),
            'phone': '555-123-4567',
            'website': 'https://example.com/johnsmith'
        },
        {
            'id': 2,
            'name': 'Maria Rodriguez',
            'photo_url': 'https://randomuser.me/api/portraits/women/28.jpg',
            'email': 'maria.rodriguez@everettcity.gov',
            'position': 'Vice President',
            'bio': 'Maria is committed to improving public transportation and accessibility.',
            'committees': 'Transportation, Public Safety',
            'term_start': datetime(2020, 1, 1),
            'term_end': datetime(2024, 12, 31),
            'phone': '555-234-5678',
            'website': 'https://example.com/mariarodriguez'
        },
        {
            'id': 3,
            'name': 'David Johnson',
            'photo_url': 'https://randomuser.me/api/portraits/men/32.jpg',
            'email': 'david.johnson@everettcity.gov',
            'position': 'Council Member',
            'bio': 'David is focused on addressing housing affordability and homelessness.',
            'committees': 'Housing, Health',
            'term_start': datetime(2022, 1, 1),
            'term_end': datetime(2026, 12, 31),
            'phone': '555-345-6789',
            'website': None
        },
        {
            'id': 4,
            'name': 'Sarah Chen',
            'photo_url': 'https://randomuser.me/api/portraits/women/56.jpg',
            'email': 'sarah.chen@everettcity.gov',
            'position': 'Council Member',
            'bio': 'Sarah is dedicated to economic development and small business support.',
            'committees': 'Economic Development, Education',
            'term_start': datetime(2020, 1, 1),
            'term_end': datetime(2024, 12, 31),
            'phone': '555-456-7890',
            'website': 'https://example.com/sarahchen'
        }
    ]
    return render_template("councilors.html", councilors=dummy_councilors)

@app.route("/meetings")
def meetings():
    now = datetime.now()
    # Create dummy meeting data
    upcoming_meetings = [
        {
            'id': 1,
            'title': 'Regular City Council Meeting',
            'date': now + timedelta(days=7),
            'start_time': '18:00',
            'end_time': '21:00',
            'location': 'City Hall, Council Chambers',
            'description': 'Regular biweekly meeting of the City Council.',
            'agenda_url': '/documents/agenda-20230615.pdf',
            'is_special': False
        },
        {
            'id': 2,
            'title': 'Special Meeting: Budget Review',
            'date': now + timedelta(days=14),
            'start_time': '17:00',
            'end_time': '20:00',
            'location': 'City Hall, Council Chambers',
            'description': 'Special meeting to review the proposed budget for the upcoming fiscal year.',
            'agenda_url': '/documents/agenda-20230622.pdf',
            'is_special': True
        }
    ]
    
    past_meetings = [
        {
            'id': 3,
            'title': 'Regular City Council Meeting',
            'date': now - timedelta(days=7),
            'location': 'City Hall, Council Chambers',
            'agenda_url': '/documents/agenda-20230601.pdf',
            'minutes_url': '/documents/minutes-20230601.pdf',
            'video_url': 'https://videoplayer.telvue.com/player/cT30AQ_xtOBQF0oJM2gIVCDX9kjgfWZb/media/926767'
        },
        {
            'id': 4,
            'title': 'Public Hearing: Downtown Revitalization',
            'date': now - timedelta(days=14),
            'location': 'City Hall, Council Chambers',
            'agenda_url': '/documents/agenda-20230525.pdf',
            'minutes_url': '/documents/minutes-20230525.pdf',
            'video_url': 'https://videoplayer.telvue.com/player/cT30AQ_xtOBQF0oJM2gIVCDX9kjgfWZb/media/922456'
        },
        {
            'id': 5,
            'title': 'Regular City Council Meeting',
            'date': now - timedelta(days=21),
            'location': 'City Hall, Council Chambers',
            'agenda_url': '/documents/agenda-20230518.pdf',
            'minutes_url': '/documents/minutes-20230518.pdf',
            'video_url': 'https://videoplayer.telvue.com/player/cT30AQ_xtOBQF0oJM2gIVCDX9kjgfWZb/media/918234'
        }
    ]
    
    return render_template("meetings.html", upcoming_meetings=upcoming_meetings, past_meetings=past_meetings)

if __name__ == "__main__":
    app.run(debug=True, port=5001, host='0.0.0.0', use_reloader=True)
