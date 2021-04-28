$env:FLASK_APP = "app.py"
# Run a "development" server, so it auto-reloads static HTML and JS files
$env:FLASK_ENV = "development"
flask run
