from flask import Flask
app = Flask(__name__)

# Link we are using for this project http://localhost:5000/

@app.route('/')
@app.route('/hello')
def HelloWorld():
    return "Hello World"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)