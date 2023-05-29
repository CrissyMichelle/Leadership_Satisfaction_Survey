from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension
from surveys import satisfaction_survey as survey

app = Flask(__name__)
app.config['SECRET_KEY'] = "shh"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

# responses = []
"""Keys names will store responses. (Not the commented out simple list above.) The responses are declared here as a constant to ensure consistent spelling.
"""
RESPONSES_KEY = "responses"

# question = survey.questions[0]

@app.route('/')
def show_survey_start():
    """Shows Select a Survey page"""
    return render_template('survey_start.html', survey=survey)

@app.route('/begin', methods=["POST"])
def start_survey():
    """Cler the session of responses."""
    session[RESPONSES_KEY] = []
    """Shows form for the Numbered question"""
    return redirect("/questions/0")

@app.route('/answer', methods=["POST"])
def handle_question():
    """Gets user response and
    redirects to next question"""
    choice = request.form['answer']

    responses = session[RESPONSES_KEY]
    responses.append(choice)
    session[RESPONSES_KEY] = responses
    
    if(len(responses) == len(survey.questions)):
        #User completed the survey.  We thank them for their service
        return redirect('/complete')
    else:
        return redirect(f"/questions/{len(responses)}")

@app.route('/questions/<int:qid>')
def show_question(qid):
    """Displays current question."""
    responses = session.get(RESPONSES_KEY)

    if(responses is None):
        #Trying to skip question 0?? Denied!
        return redirect("/")
    if(len(responses) != qid):
        #Trying to jump around out of order? Nope!
        flash(f"Invalid query: ?{qid}.")
        return redirect(f'/questions/{len(responses)}')
        
    question = survey.questions[qid]
    return render_template(
        "question.html", question_num = qid, question = question)
        
@app.route("/complete")
def complete():
    """Survey complete. Show thank you page."""
    return render_template("completion.html")
