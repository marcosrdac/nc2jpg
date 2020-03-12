import numpy as np
import netCDF4 as nc
from PIL import Image
from os.path import splitext
from sys import argv


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


assert len(argv)>1
filename=argv[1]
if len(argv)<3:
    variable = choose_variable(ncf)
else:
    variable=argv[2]
if len(argv)<4:
    quality = input('Quality of compression (0-100): ')
    quality = int(quality)
else:
    variable=argv[3]

ncf = nc.Dataset(filename)
img = ncf[variable]
maxval = np.max(img)
minval = np.min(img)
img = 255 * (img - minval)/(maxval - minval)
img = Image.fromarray(img.astype(np.uint8))

outfilename = splitext(filename)[0]
img.save(f'{outfilename}.jpg', quality=quality)
