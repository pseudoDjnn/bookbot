from flask import Flask, render_template, request

from analyzers import  WordCountAnalyzer, CharacterCountAnalyzer, CharacterFrequencyAnalyzer, SentenceCountAnalyzer,IndividualWordCountAnalzyer

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
    char_frequency = None
    sentence = None
    word_count_2 = None
    
    
    if analysis_type == 'word_count' or analysis_type == 'all':
        # Use the class instead of duplicating logic
        word_analyzer = WordCountAnalyzer(text)
        word_count = word_analyzer.analyze()
        
    if analysis_type == 'char_count' or analysis_type == 'all':
        char_count_analyzer = CharacterCountAnalyzer(text)
        char_count = char_count_analyzer.analyze()
        
    if analysis_type == 'char_frequency' or analysis_type == 'all':
        character_frequency_analyzer = CharacterFrequencyAnalyzer(text)
        char_frequency = character_frequency_analyzer.analyze()
        
    if analysis_type == 'sentence' or analysis_type == 'all':
        sentence_analyzer = SentenceCountAnalyzer(text)
        sentence = sentence_analyzer.analyze()
        
    if analysis_type == 'word_count_2' or analysis_type == 'all':
        words_in_sentence = IndividualWordCountAnalzyer(text)
        word_count_2 = words_in_sentence.analyze()
        # print(word_count_2)
        
        
    
    return render_template('results.html',
                         analysis_type=analysis_type,
                         word_count=word_count,
                         char_count=char_count,
                         char_frequency=char_frequency,
                         sentence=sentence,
                         word_count_2=word_count_2
                         )

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)