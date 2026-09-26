from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return "Hello World!"

@app.route('/about')
def about():
    return "This is the wbsite for building skills."

@app.route('/data')
def data():
    r_data={"Name":"Ajay","Age":22}
    return r_data
if __name__=='__main__':
    app.run()
