"""https://flask.palletsprojects.com/en/1.0.x/config/#SECRET_KEY
"""
import os


def main():
    print(os.urandom(16))


if __name__ == "__main__":
    main()
