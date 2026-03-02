from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'home.html',
        name="Sri Karthik",
        role="Full Stack Developer"
    )

@app.route('/about')
def about():
    return render_template(
        'about.html',
        bio="this is a short bio",
        skills=["Python", "JavaScript", "Flask"]
    )

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects = [
        {
            "name": "Portfolio Website",
            "description": "A personal portfolio website built using Flask to showcase projects and skills.",
            "ss": "images/projects/portfolio-ss.png",
            "github": "https://github.com/srikarthikB/portfolio-flask.git",
            "live": "https://portfolio-flask-production-0058.up.railway.app/",
            "highlights": [
                "Dynamic routing using Flask",
                "Template rendering with Jinja2",
                "Structured multi-page architecture",
                "Static asset management",
                "Deployed using Vercel"
            ]
        },
        {
            "name": "Interactive Digital Library",
            "description": "A web-based digital library allowing users to browse and explore books interactively.",
            "ss": "images/projects/digilib-ss.png",
            "github": "https://github.com/srikarthikB/interactive-digital-library",
            "live": "https://interactive-digital-library.onrender.com/",
            "highlights": [
                "Backend logic implemented using Flask",
                "Dynamic content rendering with Jinja2",
                "Modular project structure",
                "Local data handling",
                "Deployed using Render"
            ]
        }
    ])

if __name__ == "__main__":
    app.run(debug=True)