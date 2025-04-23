from flask import Flask,jsonify
import datetime
app=Flask(__name__)
@app.route('/')
def index():
    return 'Hello, I am alive!'

@app.route("/api/v1/details")
def details():
    return jsonify({'message':'hello world','time':datetime.datetime.now().strftime("%I:%M%p on %B %d,%Y")})
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5000)

@app.route("api/v1/test")
def test():
    return jsonify({'test':'test'})