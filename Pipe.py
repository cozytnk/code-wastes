# -*- coding: utf-8 -*-
"""
[Python: 関数合成できる API を作ってみる](https://blog.amedama.jp/entry/2019/11/25/225309)
"""

from copy import deepcopy

class Pipe:
    """
    """

    def __init__(self, func):
        """Initializer

        Parameters
        ----------
        func: function
        """
        self._func = func
        self._pipes = []

    def __rshift__(self, other):
        """self >> other
        """
        copied_self = deepcopy(self)
        copied_self._pipes.append(other)
        return copied_self

    def __rrshift__(self, other):
        """other >> self
        """
        result = self._func(other)
        for pipe in self._pipes:
            result = pipe.__rrshift__(result)
        return result

    def __call__(self, *args, **kwargs):
        """
        """
        return Pipe(lambda x: self._func(x, *args, **kwargs))


#%%
if __name__ == '__main__':

    add_one = Pipe(lambda x: x + 1)

    @Pipe
    def square(x):
        return x ** 0.5

    @Pipe
    def add(x, y):
        return x + y

    add_one_then_square = add_one >> square

    print(1 >> add_one >> square)
    print(1 >> add_one_then_square)
    print(1 >> add(1) >> square)


