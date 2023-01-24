#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    if sentence == "":
        first_chr = None
    else:
        first_chr = sentence[0]
    return(str_len, first_chr)
