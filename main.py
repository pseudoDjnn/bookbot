import json
from flask import Flask, render_template, request

from analyzers import TextAnalyzer, WordCountAnalyzer, CharacterCountAnalyzer, CharacterFrequencyAnalyzer

app = Flask(__name__)

# Route for index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for text analysis
@app.route('/analyze/', methods=['POST'])
def analyze():
    text = request.form.get("text", "")
    analysis_type = request.form.get("analysis_type", "all")
    results = {}

    if analysis_type == "all":
        results = TextAnalyzer.analyze_all(
            text,
            [WordCountAnalyzer, CharacterCountAnalyzer, CharacterFrequencyAnalyzer]
        )
    elif analysis_type == "word_count":
        results = TextAnalyzer.analyze_all(
            text,
            [WordCountAnalyzer]
        )
    elif analysis_type == "char_count":
        results = TextAnalyzer.analyze_all(
            text,
            [CharacterCountAnalyzer]
        )
    elif analysis_type == "char_frequency":
        results = TextAnalyzer.analyze_all(
            text,
            [CharacterFrequencyAnalyzer]
        )
        
        
    json_results = json.dumps(results)
    
    print("Serialized Results (JSON):", json_results)

    return render_template('results.html', results=json_results, text=text)

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)