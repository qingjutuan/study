tem =input()
if tem[0] in ['R','r']:
    F=float(tem[3:])/6.78
    print("USD{:.2f}".format(F))
elif  tem[0] in ['U','u']:
    C=float(tem[3:])*6.78
    print("RMB{:.2f}".format(C))
