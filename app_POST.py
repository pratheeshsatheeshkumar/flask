from flask import Flask, render_template, request
import os
app = Flask(__name__) 
app.config["UPLOAD_PATH"] = "static/images/"

@app.route('/home')
def home():
    return render_template("index.html")
@app.route('/upload',methods=["POST"])
def upload():
    file = request.files['file']
    file.save(os.path.join(app.config["UPLOAD_PATH"],file.filename))
    return "Uploaded Successfully"


@app.route('/register',methods=['POST'])
def register():
    name = request.form['name']
    number = request.form['number']
    email = request.form['email']
    return render_template("register.html",name=name,number=number,email=email)
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

app.add_url_rule('/',None,home)

if __name__ == '__main__':
   app.run(debug=True)



 