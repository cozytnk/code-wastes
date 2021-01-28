

class verbose:

    def __init__(self, iterable, interval=None, fmt=None):
        """

        Parameters
        ----------
        iterable: iterable object to be wrapped
        interval: int or None, verbosing interval in loop count
        fmt: str or None, fstring for verbosing.
            bar: str, progress bar
            percent: float, progress [%]
        """
        self.count = 0
        self.iterable = iterable

        if interval is None:
            self.interval = len(self.iterable) // 20
        else:
            self.interval = int(interval)

        self.fmt = fmt or '[{bar}] {percent: >3.1f}%'

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= len(self.iterable):
            print(f'\r{self._progressbar(progress=1.0)}')
            raise StopIteration
        ret = self.iterable[self.count]

        if self.count % self.interval == 0:
            # print(f'{self.count} {q} {ret} aaa')
            progress = self.count / len(self.iterable)
            print(f'\r{self._progressbar(progress=progress)}', end='')
        self.count += 1
        return ret

    def _progressbar(self, progress: float) -> str:
        bar_length = 10
        progressbar_count = int(bar_length * progress)
        bar = '>' * progressbar_count + ' ' * (bar_length - progressbar_count)
        return self.fmt.format(bar=bar, percent=progress*100)


if __name__ == '__main__':

    from time import sleep

    print('test start')
    for i in verbose(range(1000), interval=123):
        sleep(0.01)
        # print(i)
    print('test end')
