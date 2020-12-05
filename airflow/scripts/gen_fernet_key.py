#!/usr/bin/env python
# https://airflow.readthedocs.io/en/stable/howto/secure-connections.html
from cryptography.fernet import Fernet


def main():
    print(Fernet.generate_key().decode())


if __name__ == "__main__":
    main()
