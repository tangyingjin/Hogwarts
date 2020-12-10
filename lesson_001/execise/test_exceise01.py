# ecoding=utf-8
from collections import deque
import math

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.append('bestraway')
fruits.count('apple')
fruits.extend('abc')
# fruits.pop()
fruits.sort()
print(fruits)
# 队列
que = deque(["Eric", "John", "Michael"])
deque.popleft(que)
deque.appendleft(que, 'Bob')
que.append('Alan')
print(que)
# 列表创建
seq = []
for x in range(10):
    seq.append(x)

# 列表创建
seq1 = [x for x in range(10)]
seq2 = list(map(lambda x: x * 3, range(10)))
# 列表推导式
var = [(x, y) for x in [1, 2, 3] for y in [4, 5, 6] if x != y]
lst = []
for x in [1, 2, 3]:
    for y in [4, 5, 6]:
        if x != y:
            lst.append((x, y))

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[element.strip() for element in freshfruit]

vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
var = [y for x in vec for y in x]
print(var)

list = []
for num in vec:
    for i in num:
        list.append(i)
print(list)

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print("what is your {0},it is {1}".format(q, a))
    print(f'what is your {q},it is {a}')

var = [i for i in reversed(range(1, 10, 2))]
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
# sort原列表排序
basket.sort()
print(basket)
# set去除重复项
var1 = set(basket)
print(var1)
# sorted生成一个新对象，原对象不变
var = sorted(basket)
print(var)
var = [var for var in sorted(set(basket))]
print(var)
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
new_list = []
for i in raw_data:
    if not math.isnan(i):
        new_list.append(i)
print(new_list)


# 函数
def fun(b, a=1, *c, **d):
    print(f'a={a}\n', f'b={b}\n', f'c={c}\n', f'd={d}')


fun(1, 2, 2, 3, name='abc')


def x(a, b=1, *c, **d):
    print(f'a={a}\n', f'b={b}\n', f'c={c}\n', f'd={d}\n')


x(1, 2, 3, 3, x=1, y=2)
