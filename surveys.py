class Question:
    """Question on a questionnaire."""

    def __init__(self, question, choices=None, allow_text=False):
        """Create question (assume Yes/No for choices."""

        if not choices:
            choices = ["Yes", "No"]

        self.question = question
        self.choices = choices
        self.allow_text = allow_text


class Survey:
    """Questionnaire."""

    def __init__(self, title, instructions, questions):
        """Create questionnaire."""

        self.title = title
        self.instructions = instructions
        self.questions = questions


satisfaction_survey = Survey(
    "25ID Leadership Satisfaction Survey",
    "Please fill out a survey about your experience with your 25ID leadership.",
    [
        Question("Are you in a combat arms MOS?"),
        Question("Are you satisfied with your Battalion's Command Team?"),
        Question("On average, how much do you spend a month on alcohol?",
                 ["Less than $300", "$300 or more"]),
        Question("Are you satisfied with your Brigade's Command Team?"),
        Question("Do you like to speak highly of your time at 25ID?"),
        Question("Would you like to comment about toxic leadership you've observed at 25ID?")
    ])

personality_quiz = Survey(
    "Rithm Personality Test",
    "Learn more about yourself with our personality quiz!",
    [
        Question("Do you ever dream about code?"),
        Question("Do you ever have nightmares about code?"),
        Question("Do you prefer porcupines or hedgehogs?",
                 ["Porcupines", "Hedgehogs"]),
        Question("Which is the worst function name, and why?",
                 ["do_stuff()", "run_me()", "wtf()"],
                 allow_text=True),
    ]
)

surveys = {
    "satisfaction": satisfaction_survey,
    "personality": personality_quiz,
}