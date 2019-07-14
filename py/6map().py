#map
def rel(el):
    return el ** 2
lst = [1,2,3,4]
s = map(rel,lst)
for  i in s:
    print(i)


lst = [1,2,3,4]
s = map(lambda el : el ** 2,lst)
for  i in s:
    print(i)

#有多个参数时，
lst1 = [1,2,3,4]
lst2 = [5,6,7,8]
t = map(lambda x,y: x + y ,lst1,lst2)
print(list(t))

