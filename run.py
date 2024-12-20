from app import create_app, db
import os
import logging
import argparse

# Set up argument parser
parser = argparse.ArgumentParser(description='Run the Flask application.')
parser.add_argument('--env', default='development', help='The environment to run the app in (development, testing, production)')
args = parser.parse_args()

# Create app with the specified environment
app = create_app(args.env)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Check if the database file exists, if not, create it
if not os.path.exists('app.db'):
    with app.app_context():
        db.create_all()
        logger.info("Database created!")

if __name__ == '__main__':
    logger.info(f"Starting app in {args.env} mode")
    app.run(debug=(args.env == 'development'))
