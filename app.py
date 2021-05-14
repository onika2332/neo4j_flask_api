from flask import *

app = Flask(__name__, template_folder='static')

@app.route('/')
def index(link=None):

    return render_template('/html/index.html')

#@app.route('/add')

#@app.route('/update')

#@app.route('/search')

#@app.route('/delete')

if __name__ == '__main__':
    app.run(debug=False)