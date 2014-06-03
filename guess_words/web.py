from flask import Flask, render_template, request

from guess_words import search


app = Flask(__name__)

searcher = None  # to make flake8 happy


@app.before_first_request
def prepare_searcher():
    global searcher
    with open('/usr/share/dict/words') as fp:
        searcher = search.Searcher(fp)


@app.route('/')
def index():

    error = answers = None  # for easy render()

    n_letters = request.args.get('n-letters')
    if n_letters is not None:
        try:
            n_letters = int(n_letters)
        except ValueError:
            error = "Invalid input"

    letters = request.args.get('letters')
    if n_letters and letters:
        answers = searcher.lookup(letters, n_letters)

    return render_template(
        'template.html',
        letters=letters,
        n_letters=n_letters,
        error=error,
        answers=answers)


if __name__ == '__main__':
    app.run(debug=True)
