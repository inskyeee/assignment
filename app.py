from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = "1234"

# Defining the form class
class QuestionnaireForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    student_number = StringField('Student Number', validators=[DataRequired()])
    email = StringField('Email Address', validators=[DataRequired()])
    grades = TextAreaField('Grades Obtained', validators=[DataRequired()])
    satisfaction = SelectField('Overall Satisfaction', choices=[('', 'Click to select'), ('very_satisfied', 'Very Satisfied'), ('satisfied', 'Satisfied'), ('neutral', 'Neutral'), ('dissatisfied', 'Dissatisfied'), ('very_dissatisfied', 'Very Dissatisfied')], default='')
    improvements = TextAreaField('Suggestions for Improvement')
    submit = SubmitField('Submit')

# Home route
@app.route('/')
@app.route('/welcome')
def home():
    return render_template('welcome.html')

# Information route
@app.route('/information')
def information():
    return render_template('information.html')

# Data collection route with form
@app.route('/data-collection', methods=['GET', 'POST'])
def data_collection():
    form = QuestionnaireForm()
    if form.validate_on_submit():
        # Save form data to a text file
        with open("student-data.txt", "a") as file:
            file.write(f"{form.name.data}, {form.student_number.data}, {form.email.data}, {form.grades.data}, {form.satisfaction.data}, {form.improvements.data}\n")
        return redirect(url_for('thank_you'))
    return render_template('data-collection.html', form=form)

# Thank you route
@app.route('/thankyou')
def thank_you():
    return render_template('thankyou.html')

if __name__ == '__main__':
    app.run(debug=True)
