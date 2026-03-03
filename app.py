from flask import Flask, render_template, redirect, request, flash
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

app = Flask(__name__)
app.secret_key = "supersecretkey"


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            name = request.form['name']
            email = request.form['email']
            message = request.form['message']

            sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))

            email_message = Mail(
                from_email='sri2006karthik@gmail.com',  # verified sender
                to_emails='sri2006karthik@gmail.com',
                subject=f'Portfolio Contact from {name}',
                plain_text_content=f"""
Name: {name}
Email: {email}

Message:
{message}
"""
            )

            sg.send(email_message)

            flash("Message sent successfully!")
            return redirect('/contact')

        except Exception as e:
            print(e)
            return "Email failed. Check logs."

    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)