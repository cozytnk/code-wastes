"""

REF:[giampaolo/psutil](https://github.com/giampaolo/psutil)
    [ArgumentParserの使い方を簡単にまとめた - Qiita](https://qiita.com/kzkadc/items/e4fc7bc9c003de1eb6d0)
    [Pythonの文字列フォーマット（formatメソッドの使い方） | ガンマソフト株式会社](https://gammasoft.jp/blog/python-string-format/)


cpu[%]  mem[%]  (= [GB] / [GB])
------  -----------------------
***5.8  **10.0  (= *4.1 / 11.1)
**10.2
*100.0

cpu[%]  mem[%]  mem.used[GB]  mem.total[GB]
------  -----------------------------------
***5.8  **10.0  ********4.11  ********11.12

hhmmss  cpu[%]  mem[%]  mem.used[GB]  mem.total[GB]
------  ------  -----------------------------------
hhmmss  ***5.8  **10.0  ********4.11  ********11.12

cpu: ***.*, mem.percent: ***.*, mem.total: **.**, mem.used: **.**, mem.free: **.**
{ "cpu": x, "mem": { "percent": x, "total": x, "used": x, "free": x } }
"""

import psutil
import json
from datetime import datetime

if __name__ == '__main__':

    from argparse import ArgumentParser
    parser = ArgumentParser()
    parser.add_argument('--json', action='store_true')
    parser.add_argument('--cpu', action='store_true')
    # parser.add_argument('--interactive', action='store_true', default=False)
    parser.add_argument('--interval-seconds', type=float, default=2.0)
    args = parser.parse_args()

    vmem = psutil.virtual_memory()

    info = {
        "cpu": psutil.cpu_percent(),
        "mem": {
            "total": vmem.total,
            "percent": vmem.percent,
            "used": vmem.used,
            "free": vmem.free,
        }
    }

    print(psutil.cpu_percent())
    print(vmem.used, 'Bits')
    print(vmem.used / 1024, 'Bytes')
    print(vmem.used / 1024 / 1024, 'MB')
    print(vmem.used / 1024 / 1024 / 1024, 'GB')
    print(vmem.total / 1024 / 1024 / 1024, 'GB')

    [
        { "cpu[%]": 10.0, "mem[%]": 20.0, "mem used/total": "" }
    ]

    from time import sleep
    print(f'  cpu    mem')
    print(f'------------')
    while True:
        vmem = psutil.virtual_memory()
        # print(f'{psutil.cpu_percent(): >5.1f}  {vmem.percent: >5.1f} ')
        print(f'\r{psutil.cpu_percent():> 5.1f}  {vmem.percent: >5.1f} ', end='')
        sleep(2)
