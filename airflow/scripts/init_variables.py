#!/usr/bin/env python
from airflow.models import Variable

Variable.set(key="test", value="test")
Variable.set(key="test2", value="test2")
