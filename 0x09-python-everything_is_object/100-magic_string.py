#!/usr/bin/python3
def magic_string():
    setattr(magic_string, 'count', getattr(magic_string, 'count', 0) + 1)
    return ", ".join(["Holberton"] * magic_string.count)
