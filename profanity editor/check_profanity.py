import urllib.request
import urllib
from urllib.parse import quote
import logging

logging.basicConfig(level=logging.DEBUG)

def read_text():
    """
    to read text from file.
    :return none:
    """
    file=open("movie_quotes.txt")
    contents=file.read()
    file.close() #fix for issue https://github.com/sk41/py-practice/issues/1
    logging.debug(contents)
    profanity_check(contents)

def profanity_check(text_to_check):
    """
    To check for curse words
    :param text_to_check:
    :return:
    """
    text_to_check = quote(text_to_check)
    s= urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+"text_to_check")
    output=s.read()

    if True in output:
       print("Profanity alert!!!")
    else:
       print("This document has no curse words.")

def main():
    read_text()

if __name__ == '__main__':
    main()