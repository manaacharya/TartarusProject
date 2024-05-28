from flask import Flask, render_template, request, redirect, url_for, session
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Replace with a random secret key for session management

# Load the quiz data
def load_quiz(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

quiz_data = load_quiz('quiz.json')

@app.route('/')
def index():
    session.clear()  # Clear the session data
    session['current_node'] = 'start'
    return render_template('index.html')

@app.route('/question', methods=['GET', 'POST'])
def question():
    if request.method == 'POST':
        choice = request.form['choice']
        current_node = session['current_node']
        next_node_key = quiz_data['quiz'][current_node]['options'][choice]['next']
        session['current_node'] = next_node_key
        return redirect(url_for('question'))

    current_node = session['current_node']
    node_data = quiz_data['quiz'][current_node]
    if not node_data['options']:
        return render_template('end.html', message=node_data['question'])

    return render_template('question.html', question=node_data['question'], options=node_data['options'])

if __name__ == '__main__':
    app.run(debug=True)
