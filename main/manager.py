from main import app, db
from flask_migrate import Migrate

# Initialize Flask-Migrate
migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Listen on all network interfaces for Docker