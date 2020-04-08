import sys 
import glob
from tqdm import tqdm


dir_name = 'products'
products = []

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        products.append(arg.upper())   
else:
    raise TypeError('Missing arguments. Please type one or multiple products\n Ex: main.py AAA\n')

products = str(products)
processes = []


def sub_process(pgm_name, file_name, products):
    import subprocess
    return subprocess.Popen(
        ("python", pgm_name + ".py", products),
        stdin=open(file_name),
        stdout=subprocess.PIPE
    )


print('Looking into files...')
for file_name in tqdm(glob.glob(dir_name + "/chunk-*.txt")):
    processes.append(
        sub_process("main", file_name, products)
    )

print('Extracting results...')
outputs = []
for process in tqdm(processes):
    out, err = process.communicate()
    for item in out.split():
        # if type(ite)
        outputs.append(item.decode('ASCII'))

if len(outputs) == 0:
    print('\nThere are no recommendation for this product set')
else:
    print('\n', *outputs, sep=' ')
