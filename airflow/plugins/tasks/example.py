from pprint import pprint


def task_sample(*args, **kwargs):
    print("args **************************************************")
    pprint(args)
    print("kwargs **************************************************")
    pprint(kwargs)
    return "sample"


def task_branch(*args, **kwargs):
    return kwargs["params"]["branches"]["A"]


def task_short(*args, **kwargs):
    return False
