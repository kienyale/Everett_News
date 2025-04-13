from flask import render_template

@app.route('/')
def index():
    context = {
        'meeting_date': 'March 10, 2024',
        'video_url': 'https://videoplayer.telvue.com/player/cT30AQ_xtOBQF0oJM2gIVCDX9kjgfWZb/media/926767?autostart=false&showtabssearch=true',
        'issues': [
            {'date': 'Feb 1st 2025', 'title': 'Example Issue 1', 'status': 'Approved'},
            # Add more issues...
        ],
        'summary_text': 'Meeting summary will be generated here.',
        'councilors': [
            {
                'name': 'Wayne Matewsky',
                'position': 'Ward 1',
                'photo': 'path_to_photo',
                'opinion': 'Opinion text'
            },
            # Add more councilors...
        ]
    }
    return render_template('index.html', **context) 