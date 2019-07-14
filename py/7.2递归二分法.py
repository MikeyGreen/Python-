# lst = [1,3,56,342,566,567,568,3434,535345,423423425]
# left = 0
# right = len(lst) -1
# n = 568
# def finding(ls,left,right):
#     global n
#     mid = (right + left) // 2
#     if left <= right:
#         if  n < ls[mid]:
#             right = mid-1
#             return finding(ls,left,right)
#         elif n > ls[mid]:
#             left = mid + 1
#             return finding(ls,left,right)
#         elif n ==ls[mid]:
#             print("找到了")
#             return mid
#     else:
#         print("没有找到")
#         return -1
#
# a = finding(lst,0,len(lst)-1)
# print(a)



#复习
#查找某个数是否存在，用二分法 时间复杂度为O(log2 n)
#留着以后再看
row = [1,2,3,4,6,10,13,16,22,34,56,78,98]
left = 0
right = len(row) -1
n = 17
while left <= right:
    mid = (left + right) // 2
    if n < row[mid]:
        right = mid -1
        print("1",left,right)
    elif n > row[mid]:
        left = mid + 1
        print("2", left, right)
    elif n == row[mid]:      #不可能再有else
        print("找到%d了,索引为%d"%(n,mid))
        break
else:
    print("没找到")



