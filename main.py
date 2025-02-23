from flask import Flask, render_template, request,send_from_directory

from analyzers import TextAnalyzer, WordCountAnalyzer, CharacterCountAnalyzer, CharacterFrequencyAnalyzer

app = Flask(__name__)

# Home route
@app.route('/')
def index():
    # Render your `index.html` template
    return render_template('index.html')

@app.route('/analyze/', methods=['POST'])
def main():
    # Get text from form submission
    text = request.form.get("text", "")
    analysis_type = request.form.get("analysis_type", "all")
    
        
    # Dictionary to store the selected results
    analysis_results = {}
    
        # Perform analysis based on user's selection and `analyze_all`
    if analysis_type == "all":
        analysis_results = TextAnalyzer.analyze_all(
            text,
            [WordCountAnalyzer, CharacterCountAnalyzer, CharacterFrequencyAnalyzer]
        )
    elif analysis_type == "word_count":
        analysis_results = TextAnalyzer.analyze_all(text, [WordCountAnalyzer])
    elif analysis_type == "char_count":
        analysis_results = TextAnalyzer.analyze_all(text, [CharacterCountAnalyzer])
    elif analysis_type == "char_frequency":
        analysis_results = TextAnalyzer.analyze_all(text, [CharacterFrequencyAnalyzer])
    
    # Return results to the webpage
    return render_template('results.html', results=analysis_results, text=text)
    
if __name__ == '__main__':
    app.run(debug=True)
    main()