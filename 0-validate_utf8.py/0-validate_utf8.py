#!/usr/bin/python3
"""utf8 validation"""


def validUTF8(data):
    """utf8 validation"""
    for i in data:
        if(i > 127):
            return False

    return True
