import sys
import re

count = 0
p1 = r"00000[1-9]{1}[0-9a-zA-Z]{26}"
for line in sys.stdin:
    count +=1
    if 1 <= count <= int(sys.argv[1]):
        line = re.findall(p1, line)
        if(line):
            print(*line)



