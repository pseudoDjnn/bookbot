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
    text = request.form['text']
    analysis_type = request.form['analysis_type']
    
    results = {}
    
    if analysis_type == 'word_count' or analysis_type == 'all':
        words = text.split()
        results['word_count'] = len(words)
        
    if analysis_type == 'char_count' or analysis_type == 'all':
        results['char_count'] = len(text)
        
    if analysis_type == 'char_frequency' or analysis_type == 'all':
        char_freq = {}
        for char in text:
            char_freq[char] = char_freq.get(char, 0) + 1
        results['char_frequency'] = char_freq
    
    return render_template('results.html', 
                         results=results, 
                         analysis_type=analysis_type)

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)