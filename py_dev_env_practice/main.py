import os


def get_current_working_directory():
    return os.getcwd()


def main():
    print(get_current_working_directory())
    print("I'm main function!")
