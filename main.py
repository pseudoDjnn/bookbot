from flask import Flask, render_template, request, jsonify

from analyzers import TextAnalyzer

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the html form
    return render_template('index.html')  # HTML file in templates foler

@app.route('/analyze/', methods=['POST'])
def main():
    # Get text from form submission
    text = request.form.get("text", "")
    
    # Pass text to the TextAnalyzer
    analyzer = TextAnalyzer(text)
    
    # Get analysis results
    word_count = analyzer.get_word_count()
    char_count = analyzer.get_char_count()
    char_frequency = analyzer.get_char_frequency()
    
    # Return results as JSON
    return jsonify({
        'word_count': word_count,
        'char_count occurs': char_count,
        'char_frequency': char_frequency
    })
    
if __name__ == '__main__':
    app.run(debug=True)
    main()