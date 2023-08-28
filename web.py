from flask import*

app = Flask(__name__)

# By using route we can visit any pages without going to the homepage
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/helpline')
def help():
    return render_template("help.html")


if __name__ == '__main__':
    # Debug is used to save automatically
    app.run(debug=True)
