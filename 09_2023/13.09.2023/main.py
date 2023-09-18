from flask import Flask, render_template

app = Flask(__name__)
menu = [{}]


@app.route('/', methods=['GET', 'POST'])
def ind():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/skating')
def skating():
    return render_template('skating.html')


if __name__ == '__main__':
    app.run()

