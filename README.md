# Everett News

A civic tech project focused on making local government more transparent and accessible to the community.

## Setup Guide

### Prerequisites
- Python 3.8+
- Git
- pip
- Virtual environment tool (venv)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/kienyale/Everett_News.git
   cd Everett_News
   ```

2. **Set up a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set environment variables**
   ```bash
   export FLASK_APP=run.py
   export FLASK_ENV=development
   # On Windows:
   # set FLASK_APP=run.py
   # set FLASK_ENV=development
   ```

### Running the Application

Start the Flask application:
```bash
flask run
```

The application will be available at `http://localhost:5000`.

## Frontend Setup

The frontend uses HTML/CSS with Tailwind CSS for styling.

### Tailwind CSS Setup (Optional)

If you need to modify the CSS:

1. **Install Node.js dependencies**
   ```bash
   npm install
   ```

2. **Run Tailwind CSS watcher**
   ```bash
   npx tailwindcss -i ./static/css/tailwind.css -o ./static/css/styles.css --watch
   ```

## Video Integration

The project embeds a video from TelVue. You have two options:

### Option 1: Embed the video from TelVue (Recommended)

This is already configured in the `templates/index.html` file using an iframe:

```html
<iframe 
    src="https://videoplayer.telvue.com/player/cT30AQ_xtOBQF0oJM2gIVCDX9kjgfWZb/media/943866?autostart=false&showtabssearch=true" 
    frameborder="0" 
    allowfullscreen>
</iframe>
```

### Option 2: Download and host the video locally

1. **Visit** the [TelVue video page](https://videoplayer.telvue.com/player/cT30AQ_xtOBQF0oJM2gIVCDX9kjgfWZb/media/943866?autostart=false&showtabssearch=true)

2. **Download the video**:
   - Use the download button if available on the player
   - Alternatively, use a browser extension or tool that can save embedded videos

3. **Save the video** to the `static/videos/` directory and name it appropriately (e.g., `Charter_Commission_Meeting_4.3.25_vod.mp4`)

4. **Update the HTML** in `templates/index.html` to use the local video:
   ```html
   <video width="100%" controls>
       <source src="{{ url_for('static', filename='videos/Charter_Commission_Meeting_4.3.25_vod.mp4') }}" type="video/mp4">
       Your browser does not support the video tag.
   </video>
   ```

5. **Add to .gitignore**
   The `.gitignore` file already contains patterns to ignore video files to avoid committing large files:
   ```
   *.mp4
   static/videos/
   ```

## Project Structure

```
Everett_News/
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── news.py
│   ├── routes/
│   │   ├── __init__.py
│   │   └── news_routes.py
│   └── utils/
│       └── __init__.py
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── styles.css
│   └── images/
├── templates/
│   ├── components/
│   │   ├── head.html
│   │   ├── nav.html
│   │   └── footer.html
│   ├── index.html
│   ├── about.html
│   └── transparency.html
├── requirements.txt
├── .gitignore
└── run.py
```

## Troubleshooting

### Missing Dependencies
If you encounter a `ModuleNotFoundError`, ensure all dependencies are installed:
```bash
pip install flask flask-sqlalchemy requests beautifulsoup4 python-dotenv
```

### Git Issues with Large Files
If you attempt to push large video files to GitHub and encounter errors, make sure:
1. The video files are properly ignored in `.gitignore`
2. If a large file was accidentally committed, use `git filter-branch` to remove it from history
