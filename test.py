from datetime import datetime

from config import DATETIME_FMT

a = datetime.strptime('2021-01-30 06:06:37.387748+0000', DATETIME_FMT)
b = datetime.strptime('2021-02-15 06:06:37.387748+0000', DATETIME_FMT)
c = datetime.strptime('2021-02-28 06:06:37.387748+0000', DATETIME_FMT)
print(a.month - b.month)
print(abs(a - b).month)
