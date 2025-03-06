from flask import Flask 
app = Flask(__name__)
@app.route('/')


@app.route('/secondpage')


@app.route('/third')


@app.route('/fourth/<string:id>')


if __name__ == '__main__':

     # app.run(debug=True)
     app.run(host= '0.0.0.0', port=80)