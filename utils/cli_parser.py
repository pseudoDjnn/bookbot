import argparse


def setup_text_analyzer_cli():
  # Parser code
    parse = argparse.ArgumentParser(
        description='A BookBot: A professional text analysis tool'
    )

    # Required argument
    parse.add_argument(
        'book',
        help='Path to the book file to analyze'
    )
    
    # Optional arguements that show utility
    parse.add_argument(
        '--output', 
        help='Write report to a file instead of the console',
        type=str,
        metavar='FILE',
    )
    
    analysis_group = parse.add_mutually_exclusive_group()
    analysis_group.add_argument(
        '--words-only',
        action='store_true',
        help='Show only word count analysis',
        dest='words_only',
    )
        
    analysis_group.add_argument(
        '--chars-only',
        action='store_true',
        help='Show only character frequency analysis',
        dest='chars_only',
    )
    
    return parse.parse_args()