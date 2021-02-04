
def main(arg1):
    for i in range(0,int(len(arg1)/2)):
        if arg1[i] == arg1[len(arg1)-i-1]:
            print("True")
s = 'ccaack'
main(s)

