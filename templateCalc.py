from flask import Flask, render_template
app = Flask(__name__) 


@app.route('/<int:num1>')
def home(num1):
    return render_template('index.html',n1=num1)
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

#app.add_url_rule('/home',None,home())

if __name__ == '__main__':
    app.run(debug=True)



 