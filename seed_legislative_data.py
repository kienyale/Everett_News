from app import create_app, db
from app.models.legislation import Legislation
from app.models.councilor import Councilor
from app.models.vote import Vote
from app.models.meeting import Meeting
from datetime import datetime, timedelta
import random

def seed_legislative_data():
    app = create_app()
    with app.app_context():
        # First, create all tables
        db.create_all()
        
        # Check if we already have data
        if Councilor.query.first() is None:
            print("Seeding councilor data...")
            # Create dummy councilors
            councilors = [
                {
                    'name': 'John Smith',
                    'photo_url': '/static/images/councilor1.jpg',
                    'email': 'john.smith@everettcity.gov',
                    'position': 'Council President',
                    'bio': 'John has served on the council for 8 years and focuses on sustainable development.',
                    'committees': 'Budget, Planning',
                    'term_start': datetime(2022, 1, 1),
                    'term_end': datetime(2026, 12, 31),
                    'phone': '555-123-4567',
                    'website': 'https://johnsmith.org'
                },
                {
                    'name': 'Maria Rodriguez',
                    'photo_url': '/static/images/councilor2.jpg',
                    'email': 'maria.rodriguez@everettcity.gov',
                    'position': 'Vice President',
                    'bio': 'Maria is committed to improving public transportation and accessibility.',
                    'committees': 'Transportation, Public Safety',
                    'term_start': datetime(2020, 1, 1),
                    'term_end': datetime(2024, 12, 31),
                    'phone': '555-234-5678',
                    'website': 'https://mariarodriguez.org'
                },
                {
                    'name': 'David Johnson',
                    'photo_url': '/static/images/councilor3.jpg',
                    'email': 'david.johnson@everettcity.gov',
                    'position': 'Council Member',
                    'bio': 'David is focused on addressing housing affordability and homelessness.',
                    'committees': 'Housing, Health',
                    'term_start': datetime(2022, 1, 1),
                    'term_end': datetime(2026, 12, 31),
                    'phone': '555-345-6789',
                    'website': 'https://davidjohnson.org'
                },
                {
                    'name': 'Sarah Chen',
                    'photo_url': '/static/images/councilor4.jpg',
                    'email': 'sarah.chen@everettcity.gov',
                    'position': 'Council Member',
                    'bio': 'Sarah is dedicated to economic development and small business support.',
                    'committees': 'Economic Development, Education',
                    'term_start': datetime(2020, 1, 1),
                    'term_end': datetime(2024, 12, 31),
                    'phone': '555-456-7890',
                    'website': 'https://sarahchen.org'
                },
                {
                    'name': 'Michael Williams',
                    'photo_url': '/static/images/councilor5.jpg',
                    'email': 'michael.williams@everettcity.gov',
                    'position': 'Council Member',
                    'bio': 'Michael advocates for parks, recreation, and environmental initiatives.',
                    'committees': 'Environment, Parks',
                    'term_start': datetime(2022, 1, 1),
                    'term_end': datetime(2026, 12, 31),
                    'phone': '555-567-8901',
                    'website': 'https://michaelwilliams.org'
                }
            ]
            
            # Add each councilor to the database
            councilor_objects = []
            for councilor_data in councilors:
                councilor = Councilor(**councilor_data)
                db.session.add(councilor)
                councilor_objects.append(councilor)
            
            db.session.commit()
            print("Councilors added successfully!")
            
            # Create dummy legislation
            if Legislation.query.first() is None:
                print("Seeding legislation data...")
                legislations = [
                    {
                        'title': 'Downtown Revitalization Project',
                        'description': 'A comprehensive plan to revitalize the downtown area by creating more green spaces, improving pedestrian access, and developing affordable housing units.',
                        'type': 'ordinance',
                        'status': 'approved',
                        'introduction_date': datetime.now() - timedelta(days=30),
                        'vote_date': datetime.now() - timedelta(days=7),
                        'yes_votes': 4,
                        'no_votes': 1,
                        'abstain_votes': 0,
                        'document_url': '/documents/ord-2023-042.pdf'
                    },
                    {
                        'title': 'Public Transportation Expansion',
                        'description': 'Initiative to expand public transportation routes to underserved areas and increase service frequency during peak hours.',
                        'type': 'resolution',
                        'status': 'approved',
                        'introduction_date': datetime.now() - timedelta(days=45),
                        'vote_date': datetime.now() - timedelta(days=14),
                        'yes_votes': 5,
                        'no_votes': 0,
                        'abstain_votes': 0,
                        'document_url': '/documents/res-2023-015.pdf'
                    },
                    {
                        'title': 'Affordable Housing Requirements',
                        'description': 'Ordinance requiring new residential developments over 10 units to include at least 15% affordable housing units.',
                        'type': 'ordinance',
                        'status': 'pending',
                        'introduction_date': datetime.now() - timedelta(days=15),
                        'vote_date': None,
                        'yes_votes': 0,
                        'no_votes': 0,
                        'abstain_votes': 0,
                        'document_url': '/documents/ord-2023-057.pdf'
                    },
                    {
                        'title': 'Climate Action Plan',
                        'description': 'Comprehensive plan to reduce city carbon emissions by 50% by 2030 and achieve carbon neutrality by 2050.',
                        'type': 'resolution',
                        'status': 'deferred',
                        'introduction_date': datetime.now() - timedelta(days=60),
                        'vote_date': datetime.now() - timedelta(days=30),
                        'yes_votes': 2,
                        'no_votes': 1,
                        'abstain_votes': 2,
                        'document_url': '/documents/res-2023-022.pdf'
                    },
                    {
                        'title': 'Small Business Relief Program',
                        'description': 'Program providing grants and tax incentives to small businesses affected by economic downturns.',
                        'type': 'ordinance',
                        'status': 'approved',
                        'introduction_date': datetime.now() - timedelta(days=90),
                        'vote_date': datetime.now() - timedelta(days=60),
                        'yes_votes': 4,
                        'no_votes': 1,
                        'abstain_votes': 0,
                        'document_url': '/documents/ord-2023-039.pdf'
                    }
                ]
                
                # Add each legislation to the database
                legislation_objects = []
                for legislation_data in legislations:
                    legislation = Legislation(**legislation_data)
                    db.session.add(legislation)
                    legislation_objects.append(legislation)
                
                db.session.commit()
                print("Legislation added successfully!")
                
                # Create dummy votes for each legislation that has been voted on
                if Vote.query.first() is None:
                    print("Seeding vote data...")
                    for legislation in legislation_objects:
                        if legislation.vote_date:
                            # Get all councilors
                            all_councilors = Councilor.query.all()
                            
                            vote_options = ['yes', 'no', 'abstain']
                            vote_weights = [0.7, 0.2, 0.1]  # More likely to vote yes
                            
                            for councilor in all_councilors:
                                # For the climate action plan, make votes more divided
                                if 'Climate Action Plan' in legislation.title:
                                    vote_weights = [0.4, 0.3, 0.3]
                                
                                # For the small business relief, have specific voting patterns
                                if 'Small Business Relief' in legislation.title and councilor.name == 'David Johnson':
                                    vote_value = 'no'  # David always votes no on business relief
                                else:
                                    vote_value = random.choices(vote_options, weights=vote_weights)[0]
                                
                                vote = Vote(
                                    legislation_id=legislation.id,
                                    councilor_id=councilor.id,
                                    vote=vote_value,
                                    vote_date=legislation.vote_date,
                                    comments=f"Comments from {councilor.name} on {legislation.title}"
                                )
                                db.session.add(vote)
                    
                    db.session.commit()
                    print("Votes added successfully!")
                
                # Create dummy meetings
                if Meeting.query.first() is None:
                    print("Seeding meeting data...")
                    meetings = [
                        {
                            'title': 'Regular City Council Meeting',
                            'date': datetime.now() + timedelta(days=7),
                            'start_time': '18:00',
                            'end_time': '21:00',
                            'location': 'City Hall, Council Chambers',
                            'description': 'Regular biweekly meeting of the City Council.',
                            'agenda_url': '/documents/agenda-20230615.pdf',
                            'minutes_url': None,
                            'video_url': None,
                            'is_special': False,
                            'status': 'scheduled'
                        },
                        {
                            'title': 'Special Meeting: Budget Review',
                            'date': datetime.now() + timedelta(days=14),
                            'start_time': '17:00',
                            'end_time': '20:00',
                            'location': 'City Hall, Council Chambers',
                            'description': 'Special meeting to review the proposed budget for the upcoming fiscal year.',
                            'agenda_url': '/documents/agenda-20230622.pdf',
                            'minutes_url': None,
                            'video_url': None,
                            'is_special': True,
                            'status': 'scheduled'
                        },
                        {
                            'title': 'Regular City Council Meeting',
                            'date': datetime.now() - timedelta(days=7),
                            'start_time': '18:00',
                            'end_time': '21:30',
                            'location': 'City Hall, Council Chambers',
                            'description': 'Regular biweekly meeting of the City Council.',
                            'agenda_url': '/documents/agenda-20230601.pdf',
                            'minutes_url': '/documents/minutes-20230601.pdf',
                            'video_url': 'https://videoplayer.telvue.com/player/cT30AQ_xtOBQF0oJM2gIVCDX9kjgfWZb/media/926767',
                            'is_special': False,
                            'status': 'completed'
                        },
                        {
                            'title': 'Public Hearing: Downtown Revitalization',
                            'date': datetime.now() - timedelta(days=14),
                            'start_time': '18:00',
                            'end_time': '22:00',
                            'location': 'City Hall, Council Chambers',
                            'description': 'Public hearing to gather community input on the Downtown Revitalization Project.',
                            'agenda_url': '/documents/agenda-20230525.pdf',
                            'minutes_url': '/documents/minutes-20230525.pdf',
                            'video_url': 'https://videoplayer.telvue.com/player/cT30AQ_xtOBQF0oJM2gIVCDX9kjgfWZb/media/922456',
                            'is_special': True,
                            'status': 'completed'
                        },
                        {
                            'title': 'Regular City Council Meeting',
                            'date': datetime.now() - timedelta(days=21),
                            'start_time': '18:00',
                            'end_time': '20:30',
                            'location': 'City Hall, Council Chambers',
                            'description': 'Regular biweekly meeting of the City Council.',
                            'agenda_url': '/documents/agenda-20230518.pdf',
                            'minutes_url': '/documents/minutes-20230518.pdf',
                            'video_url': 'https://videoplayer.telvue.com/player/cT30AQ_xtOBQF0oJM2gIVCDX9kjgfWZb/media/918234',
                            'is_special': False,
                            'status': 'completed'
                        }
                    ]
                    
                    for meeting_data in meetings:
                        meeting = Meeting(**meeting_data)
                        db.session.add(meeting)
                    
                    db.session.commit()
                    print("Meetings added successfully!")
            
            print("All legislative data seeded successfully!")
        else:
            print("Database already contains council data!")

if __name__ == '__main__':
    seed_legislative_data() 