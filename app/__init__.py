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
            SELECT chores.name AS chore_name,
                   chores.priority,
                   chores.done,
                   persons.name AS person_name    

            FROM chores
            JOIN persons ON chores.person_id = persons.id
            ORDER BY chores.priority ASC
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
# @app.get("/choredetails")
# def show_choresdetails():
#     with connect_db() as db:
#         sql = """
#             SELECT id, chores.chore_name, person_name, priority, done
#             JOIN chores ON chores.name = persons.chores_name
#             ORDER BY chore_name, person_name DESC
#         """
#         params = ()
#         chores = db.execute(sql, params).fetchall()

#        # flash("Test message")
#        # flash("Test SUCCESS message", "success")
#         #flash("Test INFO message", "info")
#         #flash("Test WARNING message", "warning")
#         #flash("Test ERROR message", "error")

#         return render_template("pages/choredetail.jinja", chores=chores)

#-----------------------------------------------------------
# Form page - make a chore
#-----------------------------------------------------------
@app.get("/chore/new")
def show_chore_form():
    return render_template("pages/chore_form.jinja")

#-----------------------------------------------------------
# Handel the chore form
#-----------------------------------------------------------
@app.post("/chore/new")
def process_chore_form():
    with connect_db() as db:

        chores.chore_name = request.form.get("name", "unknown").strip() #Default value if no chores
        chores.person_name = request.form.get("person", "unknown").strip()
        chores.priority = request.form.get("priority", "unknown").strip()
        chores.done = request.form.get("done", "unknown").strip()



    #connect to the DB
        with connect_db() as db:
            sql = """
                
                INSERT INTO chores (chores.chore_name, chore.person_name, priority, done)
                VALUES (?, ?, ?, ?)
            """
            params = (chores.chore_name, chore.person_name, chores.priority, chores.done)

            #run qeury
            db.execute(sql, params)

            flash(f"Chore {chores.chore_name} added successfully")

            #done, return to list
            return redirect("/")

#-----------------------------------------------------------
# Chore deletion
#-----------------------------------------------------------
@app.get("/chore/<int:id>/delete")
def delete_a_chore(id):
    with connect_db() as db:
        ##delete chore using its id
        sql = """
            DELETE FROM chores
            WHERE id=?
        """
        params = (id,)
        db.execute(sql, params)


        flash("Chore deleted", "success")
##back to list
        return redirect("/")    
#-----------------------------------------------------------
# check the box 
#-----------------------------------------------------------
@app.get("/chore/<int:id>/incomplete")
def show_box_ticked(id):
    with connect_db() as db:
        sql = """
            UPDATE chores SET complete = 0 WHERE id = ?
        """
        params = (id,)
        db.execute(sql, params)

        return redirect("/")
#-----------------------------------------------------------
# uncheck the box 
#-----------------------------------------------------------
@app.get("/chore/<int:id>/complete")
def show_box_unticked(id):
    with connect_db() as db:
        sql = """
            UPDATE chores SET complete = 1 WHERE id = ?
        """
        params = (id,)
        db.execute(sql, params)

        return redirect("/")
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

