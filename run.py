from app import create_app

app = create_app()
app.jinja_env.auto_reload = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', use_reloader=True) 