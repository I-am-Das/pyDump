import pytz
from datetime import datetime
a=pytz.timezone('Asia/kolkata')
b=datetime.now(a)
print(b)
