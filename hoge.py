#! /usr/bin/env python3


def hogehoge(a, b):
    if a < b:
        return a + b
    else:
        return a - b


def pogepoge(a):
    return 2 * a


def mogemoge(a):
    return a + 5


if __name__ == "__main__":  # pragma: no cover
    print(hogehoge(5, 2))
    print(pogepoge(3))
    print(mogemoge(2))
