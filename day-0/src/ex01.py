import  sys

if len(sys.argv) < 2 or sys.argv[1].strip() == "":
    print("Input is empty")
else:
    text = sys.argv[1].split(' ')
    for i in range(len(text)):
        for j in range(len(text)):
            if(j == 0):
                print(text[i][j], end= "")
    # print()
