from modules.RandomFunctions import word_gen
import random
import string
import math

"""
Line 2990 pcre:"/\)\r\nHost\x3a\x20[\d\x2e]{7,15}\r\nConnection\x3a\x20Keep\x2dAlive\r\n\r\n$/" 
Line 3029 pcre:"/\)\r\nHost\x3a\x20[a-z\d\x2e\x2d]{6,32}\r\nCache\x2dControl\x3a\x20no\x2dcache\r\n\r\n$/" 
Line 2589 pcre:"/\r\nHost\x3a\x20[a-z0-9\x2d\x2e]+\.com\x2d[a-z0-9\x2d\x2e]+(\x3a\d{1,5})?\r\n/i" 
Line 2696 pcre:"/\)\r\nHost\x3a\x20[a-z0-9\x2d\x2e]+\r\n(Cache\x2dControl|Pragma)\x3a\x20no-cache\r\n\r\n$/" 
"""


def generate_rand():
    return word_gen(3,5,"a-z")

def regex(rand_var):    
    base = r"\r\nHost\x3A\s+[^\r\n]*?[bcdfghjklmnpqrstvwxyz]{5,}[^\r\n]*?\x2E"
    base += rand_var
    base += r"\r\n"
    
    return base

def input(rand_var, error_num):
    content = word_gen(0, 20,"a-z A-Z 0-9")
    content += "|0D 0A|Host|3A|"
    error_num = math.fmod(error_num - 1, 3)

    if (error_num != 0):
        content += word_gen(1, 5, " /09")
    content += word_gen(0, 8, "a-zA-Z0-9")
    
    selection = "b-df-hj-np-tv-z"
    if (error_num == 1):
        selection = "a-zA-Z"

    if (error_num != 2):
        content += word_gen(5, 10, selection)
    
    content += word_gen(0, 8, "a-zA-Z0-9")
    content += "|2E|" + rand_var + "|0D 0A|"
    return content

def scale():
    return 2