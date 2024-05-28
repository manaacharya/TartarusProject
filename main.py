import json

def load_quiz(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def run_quiz(quiz_data):
    current_node = quiz_data['quiz']['start']

    while True:
        print(current_node['question'])
        for option, details in current_node['options'].items():
            print(f"{option}: {details['text']}")

        if not current_node['options']:
            print("The adventure ends here. Thanks for playing.")
            break

        choice = input("Choose an option: ").upper()

        if choice in current_node['options']:
            next_node_key = current_node['options'][choice]['next']
            current_node = quiz_data['quiz'][next_node_key]
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    quiz_data = load_quiz('quiz.json')
    run_quiz(quiz_data)
