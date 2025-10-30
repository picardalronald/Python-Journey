# print out current unix timestamp in seconds and milliseconds using built in functions if available

import time

while True:
    
 timestam = time.time()

 timesec = int(timestam * 1000 )

 print(f"Seconds: {timestam: .6f} | Milliseconds: {timesec}")
 time.sleep(0.5)


