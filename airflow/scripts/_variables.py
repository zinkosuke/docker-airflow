#!/usr/bin/env python
from airflow.models import Variable
from airflow.utils.session import provide_session

variables = [
    {"key": "test_1", "value": "1"},
    {"key": "test_2", "value": "2"},
]


@provide_session
def main(session=None):
    print("Variables ********************")
    created_variables = set()
    for variable in variables:
        key = variable["key"]
        print(f"Create: {key}")
        Variable.set(**variable)
        created_variables.add(key)
    for variable in session.query(Variable).all():
        key = variable.key
        if key in created_variables:
            continue
        if key not in created_variables:
            print(f"Delete: {key}")
            Variable.delete(key)
    return


if __name__ == "__main__":
    main()
