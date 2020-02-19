from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Creating the routes
@app.route('/') # [decorator] this create the home route
def home():
    techs = ['HTML', 'CSS', 'Flask', 'Python']
    name = '30 days of Python programming'
    # return '<h1>Welcome to my website</h1>'
    return render_template('home.html', techs = techs, name = name, title = 'Home')

@app.route('/about') #this creates the about us page
def about_us():
    name = '30 days of Python programming'
    # return '<h2>About Us'
    return render_template('aboutus.html', name = name, title = 'About Us')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/post', methods = ['GET', 'POST'])
def post():
    name = 'Text Analyzer'
    if request.methods == 'GET':
        return render_template('post.html', name = name, title = name)
    if request.methods == 'POST':
        content = request.form['content']
        print(content)
        return redirect(url_for('result'))

if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
