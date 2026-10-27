from flask import Flask, render_template
from flask_bootstrap import Bootstrap5

# create an instance of Flask
app = Flask(__name__)
bootstrap = Bootstrap5(app)

# route decorator binds a function to a URL
@app.route('/')
def hello():
    return '<p>Rishabh P: POS (Point Of Sale)</p>' + \
            '<p>Ethan A: GGWP (Good Game, Well Played)</p>' + \
            '<p>Alan: LMAO (Laughing My Ass Off)</p>'

@app.route('/daniel')
def daniel():
    return render_template('template.html', message='Daniel: LOL (Laughing Out Loud)')

@app.route('/image')
def image():
    return render_template('image.html')