from flask import Flask, jsonify, render_template
app=Flask(__name__)
#@app.route('/')
#def home():
#    return "Hello World!"

@app.route('/about')
def about():
    return """<h1>This is a good website.</h1><break>
              <h2>This is for building skills.</h2><break>
              <h3>This is very useful website.</h3>"""

@app.route('/data')
def data():
    r_data={"Name":"Ajay","Age":22}
    return jsonify(r_data)
#@app.route('/')
#def new_home():
#    name="Ajay"
#    return render_template('index.html',name=name)

#@app.route('/', methods=['GET'])
#def home():
#    return "Hello World!"

@app.route('/', methods=['GET'])
def form():
    return render_template('form.html')

@app.route('/form' , methods=['POST'])
def welcome():
    return "Your information is successfully submitted."
if __name__=='__main__':
    app.run(debug=True)
