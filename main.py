from flask import Flask, render_template, request

from analyzers import  WordCountAnalyzer, CharacterCountAnalyzer, CharacterFrequencyAnalyzer

app = Flask(__name__)

# Route for index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for text analysis
@app.route('/analyze/', methods=['POST'])
def analyze():
    text = request.form['text']
    analysis_type = request.form['analysis_type']
    
    results = {}
    
    if analysis_type == 'word_count' or analysis_type == 'all':
        # Use the class instead of duplicating logic
        word_analyzer = WordCountAnalyzer(text)
        word_count = word_analyzer.analyze()
        results['word_count'] = word_count
        print(f"Word count results: {results}")
    
    return render_template('results.html', 
                         results=results, 
                         analysis_type=analysis_type)

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)