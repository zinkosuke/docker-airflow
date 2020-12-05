#!/usr/bin/env python
# https://airflow.apache.org/docs/apache-airflow/stable/security.html#web-authentication
from argparse import ArgumentParser

from airflow import models
from airflow import settings
from airflow.contrib.auth.backends.password_auth import PasswordUser


def main(args):
    user = PasswordUser(models.User())
    user.username = args.username
    user.email = args.email
    user.password = args.password
    user.superuser = True
    session = settings.Session()
    try:
        session.add(user)
        session.commit()
    finally:
        session.close()


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("username")
    parser.add_argument("email")
    parser.add_argument("password")
    args = parser.parse_args()
    main(args)
