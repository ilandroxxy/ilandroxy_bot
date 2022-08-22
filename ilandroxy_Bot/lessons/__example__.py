import time

while True:
    hour = time.strftime('%H')
    minutes = time.strftime('%M')
    if hour == '00' and minutes == '32':
        print(1231)
        time.sleep(1000)