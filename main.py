from flask import Flask, render_template, request

from analyzers import WordCountAnalyzer, CharacterCountAnalyzer, CharacterFrequencyAnalyzer

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
    
        
    # Dictionary to store the selected results
    analysis_results = {}
    
    # Perform analysis based on user's selection
    if analysis_type == "word_count":
        word_analyzer = WordCountAnalyzer(text)
        analysis_results['Word Count'] = word_analyzer.get_word_count()
    elif analysis_type == "char_count":
        char_analyzer = CharacterCountAnalyzer(text)
        analysis_results['Character Count'] = char_analyzer.get_char_count()
    elif analysis_type == "char_frequency":
        freq_analyzer = CharacterFrequencyAnalyzer(text)
        analysis_results['Character Frequency'] = freq_analyzer.get_char_frequency()
    elif analysis_type == "all":
        # print("DEBUGGER IS WORKING")
        word_analyzer = WordCountAnalyzer(text)
        char_analyzer = CharacterCountAnalyzer(text)
        freq_analyzer = CharacterFrequencyAnalyzer(text)
        analysis_results['Word Count'] = word_analyzer.get_word_count()
        analysis_results['Character Count'] = char_analyzer.get_char_count()
        analysis_results['Character Frequency'] = freq_analyzer.get_char_frequency()
        # print("DEBUGGER IS WORKING")
    
    # Return results to the webpage
    return render_template('results.html', results=analysis_results, text=text)
    
if __name__ == '__main__':
    app.run(debug=True)
    main()