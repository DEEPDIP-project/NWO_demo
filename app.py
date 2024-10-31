from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="DeepDip", header="DeepDip", message="Example")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/videos')
def videos():
    return render_template('videos.html')


if __name__ == '__main__':
    app.run(debug=True)

