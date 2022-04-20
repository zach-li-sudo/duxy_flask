from flask import Flask, render_template
from data_extract import fetchAll

app = Flask(__name__)

@app.route("/")
def hello_world():
    # return "<p>Hello world</p>"
    return render_template('lookup.html')


@app.route("/results")
def get_results():
    data = fetchAll()
    return render_template('results.html', data_html=data.to_html())




if __name__ == "__main__":
    app.run()