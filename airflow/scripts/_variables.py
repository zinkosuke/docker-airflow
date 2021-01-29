#!/usr/bin/env python
from airflow.models import Variable


def main():
    Variable.set(key="test", value="test")
    Variable.set(key="test2", value="test2")


if __name__ == "__main__":
    main()
