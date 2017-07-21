import sys, hashlib

password = sys.argv[1]
m = hashlib.new('sha512')
m.update(str(password).encode('utf-8'))
print(m.hexdigest())
