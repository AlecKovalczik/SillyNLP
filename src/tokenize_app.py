"""
Tokenization related CLI commands.

When calling commands from this module, all commands are prefaced with "tokenize"

Command List: 
    :func:`word`: Tokenize the passed string based on words and symbols.
    :func:`sentence`: Tokenize the passed string based on the sentences.
    :func:`regex`: Tokenize the passed string based on the regular expression passed after the sentence.
"""

import typer
from typing import List
from rich import print
from nltk.tokenize import word_tokenize, sent_tokenize, regexp_tokenize
from nltk.corpus import stopwords

tokenize_app = typer.Typer(name="tokenize")

@tokenize_app.command()
def word(text:str) -> None:
    """
    Tokenize the passed string based on words and symbols then return the result to stdout.

    The resulting tokens are filtered based on a common set of stop words from nltk.
    
    Args:
        text (str): Text you want tokenized.
    """
    words = word_tokenize(text)

    # Note: stopwords includes the word "not" which we don't really want.
    stop_words = set(stopwords.words("english"))
    filtered_list = [
        word for word in words if word.casefold() not in stop_words
    ]

    print(filtered_list)

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