from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("index.html", blog_data = data)

@app.route('/post/<int:post_id>')
def read(post_id):
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    data = response.json()
    return render_template("post.html", blog_data_1 = data, blog_id = post_id)

if __name__ == "__main__":
    app.run(debug=True)