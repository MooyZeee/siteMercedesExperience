from flask import Flask, render_template, redirect, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/reg', methods=['POST'])

def register():
    print(request.form)
    return redirect("/")


if __name__ == '__main__':
    app.run(debug=True)