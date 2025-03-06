class TextAnalyzer:
    def __init__(self, text):
        if not isinstance(text, str):
            raise ValueError("TextAnalyzer requires a string input")
        self.text = text
    
    """

    Based method placeholder for child classe.
    This shold be overridden by soecific analyzers.
    
    """
    def analyze(self):
        raise NotImplementedError("Child classes must implement the `analyze` method")
    
    
    @staticmethod
    def analyze_all(text, analyzers):
        """

        Runs analysis from multiple analyzers and combines results 
        into one dictionary.
        
        """
                
        results = {}
        for analyze in analyzers:
            analyzer = analyze(text)
            results.update(analyzer.analyze())
        return {
            "Results": results
        }