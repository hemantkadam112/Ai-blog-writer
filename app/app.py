from flask import Flask, render_template, request
import openai
import os

# Set up OpenAI API credentials
openai.api_key = "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"


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('main.html')


@app.route('/limitations')
def limit():
    return render_template('limitations.html')


@app.route('/paraphrase', methods=['GET', 'POST'])
def paraphrase():
    if request.method == 'POST':
        original_text = request.form['original_text']
        # Paraphrase Engine
        model_engine = "text-davinci-002"
        completions = openai.Completion.create(
            engine=model_engine,
            prompt="paraphrase"+original_text,
            max_tokens=100,
        )

        # Get the response
        message = completions.choices[0].text.strip()

        paraphrase_text = message
        return render_template('paraphrase.html', paraphrase_text=paraphrase_text)
    else:
        return render_template('paraphrase.html')


@app.route('/summarize', methods=['GET', 'POST'])
def summarize():
    if request.method == 'POST':
        original_text = request.form['original_text']
        custom_input =""+original_text
       
        # Use AI model to summarize text
        model_engine = "text-davinci-002"
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=custom_input,
            max_tokens=100,
        )

        # Get the response
        message = completions.choices[0].text.strip()

        summarized_text = message
        return render_template('summarize.html', summarized_text=summarized_text)
    else:
        return render_template('summarize.html')


@app.route('/write_content', methods=['GET', 'POST'])
def write_content():
    if request.method == 'POST':
        topic = request.form['topic']
        unique_prompt =(
    "In your own words, describe a story about below topic . Please make it engaging and detailed, as if you are narrating it to a friend. Include emotions, sensory details, and any relevant background information. Be creative and feel free. The goal is to make it sound authentic and human-like. Take your time and craft the narrative thoughtfully.")

       # Create a custom prompt by combining topic and unique_prompt
        custom_prompt = topic+unique_prompt

        # Use the gpt-3.5-turbo-0613 engine to generate new content based on the custom prompt
        model_engine = "text-davinci-003"  # Update the engine to gpt-3.5-turbo-0613
        completions = openai.Completion.create(
            engine=model_engine,
            prompt=custom_prompt,
            max_tokens=100,
        )

        # Get the response
        generated_content = completions.choices[0].text.strip()

        return render_template('write_content.html', generated_content=generated_content)
    else:
        return render_template('write_content.html')

if __name__ == '__main__':
    app.run(debug=True)