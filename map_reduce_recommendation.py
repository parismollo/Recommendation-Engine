import subprocess
import sys

products = []

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        products.append(arg.upper())   
else:
    raise TypeError('Missing arguments. Please type one or multiple products\n Ex: main.py AAA\n')

products = str(products)

p1 = subprocess.Popen(('python', 'main.py', products),
    stdin=open('products/chunk-1.txt'), stdout=subprocess.PIPE)

p2 = subprocess.Popen(('python', 'main.py', products),
    stdin=open('products/chunk-2.txt'), stdout=subprocess.PIPE)

p3 = subprocess.Popen(('python', 'main.py', products),
    stdin=open('products/chunk-3.txt'), stdout=subprocess.PIPE)

p4 = subprocess.Popen(('python', 'main.py', products),
    stdin=open('products/chunk-4.txt'), stdout=subprocess.PIPE)


out1, err1 = p1.communicate()
out2, err2 = p2.communicate()
out3, err3 = p3.communicate()
out4, err4 = p4.communicate()


outputs = [out1, out2, out3, out4]

for out in outputs:
    print(out.decode('ASCII'))
