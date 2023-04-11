from flask import Flask
app = Flask(__name__) 

@app.route('/<int:num1>') 
def home(num1):
  return "Square is {:15}".format(num1*num1) #This is 10 
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




 