from flask import Flask, render_template, request, jsonify

import openai

openai.api_key = "YOUR_API_KEY"


app = Flask(__name__)

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    chat_messages = [{'role': 'system', 'content': 'You are a helpful assistant.'}, {'role': 'user', 'content': input}]
    return get_openai_response(chat_messages)

def get_openai_response(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages,
        max_tokens=100,
    )
    return response['choices'][0]['message']['content']



if __name__ == '__main__':
    app.run()
