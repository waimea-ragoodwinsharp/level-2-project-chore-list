#===========================================================
# Choresorter
# By Rose Goodwin-Sharp
#===========================================================

from flask import Flask, request, session, render_template, flash, redirect, send_file, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from dotenv import load_dotenv
from os import getenv
from io import BytesIO
import html
from app.helpers import *


# Create the app
app = Flask(__name__)


#===========================================================
# App Routes Handlers
#===========================================================

#-----------------------------------------------------------
# Home page - Show all chores
#-----------------------------------------------------------
@app.get("/")
def show_chores():
    with connect_db() as db:
        sql = """
            SELECT id, name 
            FROM chore
            ORDER BY pinned DESC, created DESC
        """
        params = ()
        chores = db.execute(sql, params).fetchall()

        flash("Test message")
        flash("Test SUCCESS message", "success")
        flash("Test INFO message", "info")
        flash("Test WARNING message", "warning")
        flash("Test ERROR message", "error")

        return render_template("pages/chore_list.jinja", chores=chores)


#-----------------------------------------------------------
# details page - Show all chores in detail
#-----------------------------------------------------------
@app.get("/choredetails")
def show_choresdetails():
    with connect_db() as db:
        sql = """
            SELECT id, name, person_id, priority, done
            FROM chore
            ORDER BY pinned DESC, created DESC
        """
        params = ()
        chores = db.execute(sql, params).fetchall()

        flash("Test message")
        flash("Test SUCCESS message", "success")
        flash("Test INFO message", "info")
        flash("Test WARNING message", "warning")
        flash("Test ERROR message", "error")

        return render_template("pages/chore_list.jinja", chores=chores)



#===========================================================
# Configure the app
#===========================================================
load_dotenv()
app.config.from_prefixed_env()
init_logging(app)
init_text_filters(app)
init_date_filters(app)
init_error_handlers(app)
init_database()
register_commands(app)

