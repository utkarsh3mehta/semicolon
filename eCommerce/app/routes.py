from app import app, db
@app.route('/')
def index():
    return "This is Semicolon eCommerce API"
