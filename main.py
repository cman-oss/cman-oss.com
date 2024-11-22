from flask import Flask

app = Flask(__name__)


@app.route('/')
def test():
   return 'Hello from Flask!'

app.run(port=5000, debug=True)

