from flask import Flask
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object("app.config.Config")  # Make sure your config.py has MAIL settings

# Define the Mail instance here
mail = Mail(app)

# Optional: import your routes if any
# from app import routes
