while "Y":
    content = input("请输入你要反转的字符串：")
    def reverse(s):
        if len(s) == 1:    #s[1] == '':
            return s
        else:
            return reverse(s[1:]) + s[0]
    print(reverse(content))
