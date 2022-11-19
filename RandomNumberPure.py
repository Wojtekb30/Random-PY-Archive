import time
milliseconds = int(round(time.time() * 1000))
print(milliseconds)
minl = 0
maxl = 30
while not (milliseconds >minl and milliseconds <maxl):
    if milliseconds%2==0:
        milliseconds = milliseconds/2
    elif milliseconds%3==0:
        milliseconds = milliseconds/3
    elif milliseconds%5==0:
        milliseconds = milliseconds/5
    elif milliseconds%7==0:
        milliseconds = milliseconds/7
    elif milliseconds%11==0:
        milliseconds = milliseconds/11
    elif milliseconds%13==0:
        milliseconds = milliseconds/13
    else:
        milliseconds = milliseconds/3
print(int(milliseconds))