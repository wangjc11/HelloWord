tne_things = "apple orange crow telephone light sugar"

print("wait a moument")

stuff = tne_things.split(' ')  #  .split分开字符串，需要添加引号，如果只有一个完整的字符串， .append使用不了
more_stuff = ["day","night","song","frisbee","corn","banana","girl","boy"]

for x in (6,7,8,9):        #  for循环的循环次数看的是Y列表中的个数  [] ()无所谓
    next_one = more_stuff.pop()
    print(next_one)
    stuff.append(next_one)
    print("now there are {} items".format(len(stuff)))

print(stuff)

print(stuff[1])
print(stuff[-1])
print(stuff.pop())  # .pop()默认选取最后一个元素
print(' '.join(stuff))
print("*".join(stuff))
