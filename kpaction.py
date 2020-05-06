from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session

# Configure application
app = Flask(__name__)

db = SQL("sqlite:///action.db")

@app.route("/action", methods=["GET", "POST"])
def action():
    
    # if data is going to change
    if request.method == "POST":
        
        # look for the specified phrase that is asked from the user
        first = request.form.get("firstname")
        last = request.form.get("lastname")
        subject = request.form.get("subject")

        # if the given name or subject doesn't exist, tell user
        if first == None:
            return "Need a First Name"
        if last == None:
            return "Need a Last Name"
        if subject == None:
            return "Write a Comment"

        # insert new information into the table
        db.execute("INSERT INTO action (first, last, subject) VALUES (:first, :last, :subject)", first = request.form.get("firstname"), last = request.form.get("lastname"), subject = request.form.get("subject"))
        
        
        return redirect("page5.html")

    # if no changes return to the html without submitting changes
    else:
        return redirect("page5.html")
