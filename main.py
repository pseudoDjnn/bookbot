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
    analysis_type = request.form.get("analysis_type", "all")
    
    # Pass text to the TextAnalyzer
    analyzer = TextAnalyzer(text)
    
    # Dictionary to store the selected results
    analysis_results = {}
    
    # Perform analysis based on user's selection
    if analysis_type == "word_count":
        analysis_results['Word Count'] = analyzer.get_word_count()
    elif analysis_type == "char_count":
        analysis_results['Character Count'] = analyzer.get_char_count()
    elif analysis_type == "char_frequency":
        analysis_results['Character Frequency'] = analyzer.get_char_frequency()
    elif analysis_results == "all":
        analysis_results['Word Count'] = analyzer.get_word_count()
        analysis_results['Character Count'] = analyzer.get_char_count()
        analysis_results['Character Frequency'] = analyzer.get_char_frequency()
    
    # Return results to the webpage
    return render_template('results.html', results=analysis_results, text=text)
    
if __name__ == '__main__':
    app.run(debug=True)
    main()