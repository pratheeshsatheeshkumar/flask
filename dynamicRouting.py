from flask import Flask
app = Flask(__name__) 

@app.route('/<name>')
def home(name):
  return "This is {:15}".format(name)  
@app.route('/about')
def about():
    return "This is about page"

@app.route('/product')
def product():
    return "This is product page"

@app.route('/product/laptop')
def laptop():
    return "This is product laptop page"        

@app.route('/contact')
def contact():
    return "This is contact page"


if __name__ == '__main__':
    app.run(debug=True)




 