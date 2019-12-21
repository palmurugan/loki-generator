import functools


def compose(*functions):
    return functools.reduce(__internal_compose, functions, lambda x: x)


def __internal_compose(f, g):
    return lambda x: f(g(x))
