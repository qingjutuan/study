tem =input()
if tem[-1] in ['c','C']:
    F=float(tem[:-1])*1.8+32
    print("{:.2f}F".format(F))
elif  tem[-1] in ['f','F']:
    C=(float(tem[:-1])-32)/1.8
    print("{:.2f}C".format(C))
else:
    print("输入格式错误")
