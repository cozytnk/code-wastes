
import json
import matplotlib.pyplot as plt
import mpld3
from flask import Flask, render_template, request


app = Flask(__name__, template_folder='.')

@app.route('/')
def hello():
    return render_template(
        'index.html',
        fig=mpld3.fig_to_html(fig=plt.gcf(), template_type='simple'),
    )

@app.route('/new-title', methods=['GET','POST'])
def good():
    title = request.form['title']
    plt.gca().set_title(title)
    return render_template('index.html', title=title, fig=mpld3.fig_to_html(fig=plt.gcf(), template_type='simple'))



if __name__ == '__main__':

    plt.plot(range(100))

    app.run(debug=True)
