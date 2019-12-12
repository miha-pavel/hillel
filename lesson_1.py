import time, random
# def get_list():
#     print("get_lest")
#     lst=[]
#     for i in range(11):
#         lst.append(i)
#     return lst

# for i in get_list():
#     print("for loop 2")
#     print(i)

# =========================
# def gen():
#     counter=0
#     while counter<=10:
#         print('yield')
#         print(counter)
#         yield counter
#         counter+=1

# for i in gen():
#     print("for loop")
#     print(i)

# =========
# for i in range(1000000000):
#     print(i)

# def gen():
#     counter=0
#     while counter<=10:
#         print('yield')
#         print(counter)
#         yield counter
#         counter+=1
# =========
# my_gen=gen()
# for i in gen():
#     print("for loop")
#     print(i)

# # for i in my_gen():
# #     print("for loop qwe")
# #     print(i)
# =========
# my_gen = (i for i in range(10))
# print(my_gen)
# =========
# a = sum([i for i in range(10)])
# b = sum((i for i in range(10)))
# print(a)
# print(b)
# =========
# def add():
#     time.sleep(random.randint(0, 3))
#     return 10+10

# start = time.time()
# add()
# print(time.time()-start)

# =========
# def decor(func):
#     return func

# add2 = decor(add)
# print(add2())
# =========
# def decor(func):
#     def wrapper():
#         start = time.time()
#         result = func()
#         print(time.time()-start)
#         return func
#     return wrapper
# =======
# @decor
# def add():
#     time.sleep(random.randint(0, 3))
#     return 10+10


# add = decor(add)
# print(add())

# class Human:
#     def foo(self):
#         return 1
    
#     def __call__(self, *arg, **kwargs):
#         return "hello"
    
#     # def __add__
#     # def __init__
#     # def __str__

# hi = Human()
# print('hi: ', hi.foo())
# print('hi: ', hi())
# print('hi: ', hi)

# def foo():
#     return 1

# print(dir(foo))


class Human:
    c = 4
    # def __add__
    def __init__(self, a, b):
        self.a = a
        self.b = b
    # def __str__

hi = Human("asd", "xvd")
print('hi: ', hi.a)
print('hi: ', hi.__dict__['a'])

print('hi: ', hi.c)
print('hi: ', hi.__class__.__dict__['c'])

h1.d = 4
h1.__dict__["d"] = 5
print('h1.d: ', h1.d)
