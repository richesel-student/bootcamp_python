import re
import sys
text = sys.stdin.read()
text = text.split('\n')
def func(text):
    for i in range(len(text)):
        if(len(text) == 3 and len(text[0]) == 5 and len(text[1]) == 5 and len(text[2]) == 5):
            p1 = r"^\*[\w][^*\s][\w]\*$"
            p2 = r"^\**[^*\s]{1}\**$"
            p3 = r"^\*[^*\s]{1}\*[^*\s]{1}\*$"
            match1 = re.findall(p1, text[0])
            match2 = re.findall(p2, text[1])
            match3 = re.findall(p3, text[2])
            if(match1  and match2 and match3):
                return True
            else:
                return False
        else:
            return 'Error'
print(func(text))