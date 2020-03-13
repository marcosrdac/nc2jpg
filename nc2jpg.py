import numpy as np
import netCDF4 as nc
from PIL import Image
from os.path import splitext, isdir, join
from sys import argv

FALLBACK_EXT='.jpg'


def choose_variable(ncf):
    '''
    Show all variables of an open NetCDF file.
    '''
    variables = list(ncf.variables.keys())
    print('Choose a variable to be converted:')
    for i, variable in enumerate(variables):
        print(f'\t{i+1}\t{variable}')
    variable_number = int(input('Variable number: '))-1
    variable = variables[variable_number]
    print()
    return(variable)

# reading inputfrom user
assert len(argv) > 1
filepath = argv[1]  # always
options  = argv[2:]  # 0 is python
# opening NetCDF file
ncf = nc.Dataset(filepath)
while len(options) > 1:
    if options[0] == '-v':
        variable = options[1]
    if options[0] == '-o':
        outfilepath = options[1]
    if options[0] == '-q':
        quality = int(options[1])
    del(options[:2])
if not 'variable' in globals():
    variable = choose_variable(ncf)
if not 'quality' in globals():
    quality = input('Quality of compression (0-100): ')
    quality = int(quality)
if not 'outfilepath' in globals():
    outfilepath = splitext(filepath)[0] + FALLBACK_EXT

# checking if output is a directory or a filepath
name = splitext(filepath)[0]
ext  = splitext(outfilepath)[1]
outext  = ext if ext else FALLBACK_EXT
if isdir(outfilepath):
    outfilepath = join(outfilepath, name+outext)

print(outfilepath)

# getting NetCDF variable
img = ncf[variable]

# scaling variable to fit a RGB image
maxval = np.max(img)
minval = np.min(img)
img = 255 * (img - minval)/(maxval - minval)
img = Image.fromarray(img.astype(np.uint8))

# saving file
img.save(outfilepath, quality=quality)
