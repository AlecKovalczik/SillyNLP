"""
Tokenization related CLI commands.

When calling commands from this module, all commands are prefaced with "tokenize"

Command List: 
    :func:`word`: Tokenize the passed string based on words and symbols.
    :func:`sentence`: Tokenize the passed string based on the sentences.
    :func:`regex`: Tokenize the passed string based on the regular expression passed after the sentence.
"""

import typer
from rich import print
from nltk.tokenize import word_tokenize, sent_tokenize, regexp_tokenize

tokenize_app = typer.Typer(name="tokenize")

@tokenize_app.command()
def word(text):
    """
    Tokenize the passed string based on words and symbols then return the result to stdout.
    
    Args:
        text (str): Text you want tokenized.
    """
    print(word_tokenize(text))

@tokenize_app.command()
def sentence(text):
    """
    Tokenize the passed string based on the sentences then return the result to stdout.
    
    Args:
        text (str): Text you want tokenized.
    """
    print(sent_tokenize(text))

@tokenize_app.command()
def regex(text, pattern):
    """
    Tokenize the passed string based on the regular expression passed after the sentence then return the result to stdout.
    
    Args:
        text (str): Text you want tokenized.
        pattern (str): Regular expression to tokenize text with.
    """
    print(regexp_tokenize(text, pattern))