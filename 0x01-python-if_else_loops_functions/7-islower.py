import string

def islower(c):
    if c in list(string.ascii_uppercase):
        return True
    elif c in range (64, 91):
        return False
