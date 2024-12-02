from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

GITHUB_TOKEN = "your_github_token"

@app.route('/webhook', methods=['POST'])
def webhook():
    payload = request.json
    # Handle only pull_request events
    if payload['action'] in ['opened', 'synchronize']:
        pr_number = payload['number']
        repo = payload['repository']['full_name']

        # Get the diff using GitHub API
        diff_url = payload['pull_request']['diff_url']
        headers = {"Authorization": f"token {GITHUB_TOKEN}"}
        diff_response = requests.get(diff_url, headers=headers)
        diff = diff_response.text

        # Process diff with AI model (e.g., CodeT5, GPT, etc.)
        commit_message = generate_commit_message(diff)

        # Post a comment with the suggested commit message
        comment_url = f"https://api.github.com/repos/{repo}/issues/{pr_number}/comments"
        comment = {"body": f"Suggested Commit Message:\n\n{commit_message}"}
        requests.post(comment_url, json=comment, headers=headers)

    return jsonify({"status": "ok"})

def generate_commit_message(diff):
    # Replace with your AI model integration
    return "Example commit message summarizing the diff."

if __name__ == "__main__":
    app.run(port=5000)
