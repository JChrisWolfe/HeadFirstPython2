from flask import Flask, render_template, request
from vsearch import search4letters

# __name__ is maintained by the Python Interpreter, is set to 
#  the current active module.The Flask class need to know the
#  the current value of __name__ when creating a new Flask class. 
app = Flask(__name__) 


@app.route('/search4', methods=['POST'])
def do_search() -> str:
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = 'Here are your results: '
    results = str(search4letters(phrase, letters))
    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=results)

# @app is called a 'decorator'. 
# A function decorator, which is what we have in this code, adjusts the behavior
# of an existing function without you having to change that function’s code (that
# is, the function being decorated).

# In essence, decorators allow you to take some existing code and augment
# it with additional behavior as needed. Although decorators can also be
# applied to classes as well as functions, they are mainly applied to functions,
# which results in most Python programmers referring to them as function
# decorators.
@app.route('/')
# Flask’s route decorator is available to your webapp’s code via the app
# variable, which was created on the previous line of code.
# The route decorator lets you associate a URL web path with an existing
# Python function.
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')

if __name__ == '__main__':
    app.run(debug=True) # Ask the app to start running.
