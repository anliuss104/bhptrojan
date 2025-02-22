import os

def run(**args):
    print("[*] Nel module dirlister.")
    files = os.listdir(".")
    return str(files)