import os


def full_path(file_name):
    now_path = os.getcwd()
    print now_path
    path = os.path.abspath(file_name)
    return path


print full_path('servr.py')