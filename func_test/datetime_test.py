from datetime import datetime

now_date = datetime.now()
fmt_date = now_date.strftime("%Y-%m-%d")
print(fmt_date)