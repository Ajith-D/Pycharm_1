from flask import*
import requests
app = Flask(__name__)

# By using route we can visit any pages without going to the homepage
@app.route('/')
def home():
    return render_template("home.html")

@app.route('/helpline')
def help():
    return render_template('help.html')

@app.route('/track', methods=['POST'])
def track():
    if request.method == 'POST':
        url = request.form['user_url']
        resp = requests.get(url)
        redirect_url = resp.history
        return render_template('track.html', endurl=resp, redirect=redirect_url)


if __name__ == '__main__':
    # Debug is used to save automatically
    app.run(debug=True)
