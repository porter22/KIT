from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def graph():
    return render_template('graph.html')

#set FLASK_APP=app.py in cmd
#python -m flask run

@app.route('/about')
def about():
    return 'Visualisation for KIT'

if __name__ == "__main__":
    print('server is running on localhost')
    app.run(host='0.0.0.0', threaded=True, debug=True)