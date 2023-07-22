
from datetime import datetime

now = datetime.now()
print("start =", now)

import os
os.system('cat Badges.xml | python3 mapper/mapper.py | sort -k1,1 | python3 reducer/reducer.py')

now = datetime.now()
print("stop =", now)
