def cal():
    '''
    输入1到7，然后打印出分别对应的星期一到星期日
    '''
    for i in range(20):
        content = "星期一星期二星期三星期四星期五星期六星期日"
        a = int(input('请输入星期几，输入用1到7数字代表：'))
        if a in list(range(1,8)):
            index = a * 3
            output = content[index-3:index]
            print(output)
        else:
            print("请重新输入")
            continue
if __name__ == '__main__':
    cal()

