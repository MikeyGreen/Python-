while (True):
    content = str(input('请输入当前温度：'))
    if content[-1] in ["c","C"]:
        huashi = int(content[:-1]) * 1.8 + 32
        print("当前温度为摄氏度{a},转化为华氏度{b}".format(a = content,b = str(huashi) + 'F'))
    elif content[-1] in ['f','F']:
        sheshi = (int(content[:-1])- 32) / 1.8
        print('当前温度为华氏度{0}，转化为摄氏度{1}'.format(content,str(sheshi) + 'C'))
    else:
        print('输入有误')
