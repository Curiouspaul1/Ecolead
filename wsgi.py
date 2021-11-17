from main import create_app
from dotenv import load_dotenv
from models import *
import os

load_dotenv()

app = create_app(os.getenv('FlASK_CONFIG') or "default")

@app.shell_context_processor
def make_shell_context():
    return dict(app=app, donor=Donor)
