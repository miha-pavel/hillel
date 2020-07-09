from hashlib import sha256

class Human:
    def __init__(self, first_name):
        self.first_name = first_name


h1 = Human("Dima")
h2 = Human("Alex")
print(h1.first_name)
print(h1.__hash__())

d = {
    h1: 1,
    h2: 2
}
print(d)

# print(dir(sha256(b'password')))
print(sha256(b'password').hexdigest())
print(sha256(b'password').hexdigest())
print(sha256(b'password').hexdigest())