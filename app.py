import openai
from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/prompts", methods=["GET", "POST"])
def prompts():
    result = ""
    if request.method == "POST":
        input1 = request.form.get("topic")
        input2 = request.form.get("wtype")
        result = openai.Completion.create(
            model = "text-davinci-003",
            prompt = "Create a writing prompt for an " + input2.lower() + " about " + input1,
            temperature = 0,
            max_tokens = 256,
            top_p = 1,
            frequency_penalty = 2,
            presence_penalty = 2
        )
        result = json.loads(str(result))["choices"][0]["text"]

    return render_template("prompts.html", output=result, textin=input1)

@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    result = ""
    if request.method == "POST":
        input1 = request.form.get("input")
        input2 = request.form.get("type")
        result = openai.Completion.create(
            model = "text-davinci-003",
            prompt = "Person 1: Here is my " + type.lower() + ". Can I have feedback on this?\n" + input1 + "Person 2: Here is my lengthy response, not referring to person 1 at all, not using 2nd person, and providing constructive criticism about the writing:",
            temperature = 0,
            max_tokens = 1000,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0
        )
        result = json.loads(str(result))["choices"][0]["text"]
        return render_template("feedback.html", output=result, textin=input1)

@app.route("/write")
def write():
    return render_template("write.html")

if __name__ == '__main__':
    app.run()
