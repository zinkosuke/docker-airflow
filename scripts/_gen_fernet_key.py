#!/usr/bin/env python
# https://airflow.apache.org/docs/apache-airflow/2.0.0/security/secrets/fernet.html
from cryptography.fernet import Fernet


def main():
    print(Fernet.generate_key().decode())


if __name__ == "__main__":
    main()
