from flask import Flask, render_template, request

from analyzers import TextAnalyzer, WordCountAnalyzer, CharacterCountAnalyzer, CharacterDisplayFormatter, SentenceCountAnalyzer, WordFrequencyAnalyzer

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
    
    word_count = None
    char_count = None
    formatted_char_count = None
    sentence_count = None
    word_count_2 = None
    
    
    if analysis_type == 'word_count' or analysis_type == 'all':
        # Use the class instead of duplicating logic
        word_analyzer = WordCountAnalyzer(text)
        word_count = word_analyzer.analyze()
        
    if analysis_type == 'char_count' or analysis_type == 'all':
        char_count_analyzer = CharacterCountAnalyzer(text)
        char_count = char_count_analyzer.analyze()
        # print(char_count)
        
    if analysis_type == 'formatted_char_count' or analysis_type == 'all':
        character_frequency_analyzer = CharacterDisplayFormatter(text)
        formatted_char_count = character_frequency_analyzer.analyze()
        # print(formatted_char_count)
        
    if analysis_type == 'sentence_count' or analysis_type == 'all':
        sentence_analyzer = SentenceCountAnalyzer(text)
        sentence_count = sentence_analyzer.analyze()
        
    if analysis_type == 'word_count_2' or analysis_type == 'all':
        words_in_sentence = WordFrequencyAnalyzer(text)
        word_count_2 = words_in_sentence.analyze()
        
        
    
    return render_template('results.html',
                         analysis_type=analysis_type,
                         word_count=word_count,
                         char_count=char_count,
                         formatted_char_count=formatted_char_count,
                         sentence_count=sentence_count,
                         word_count_2=word_count_2
                         )

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)