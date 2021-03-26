from datetime import datetime
timestamp = datetime.fromtimestamp(1614727221417//1000)
print(timestamp.strftime('%Y-%m-%d %H:%M:%S'))