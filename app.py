from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/start')
def start():
    return render_template('start.html', num_players = 0)



if __name__ == '__main__':
    app.run(debug=True)
