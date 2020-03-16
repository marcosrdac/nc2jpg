# nc2jpg

This program exports a NetCDF file variable to a JPEG file (values are scaled to fit between 0-255). JPEG quality can be chosen. This code is meant to ease posterior creation of handmade masks for a NetCDF variable with an image editor like *GIMP*.


## Dependencies:

You need `Python 3+` and `pip 3+` in order to use this script.

| Python libraries needed |
| - |
| numpy |
| netcdf4 |
| pillow |

If your distribution still calls `python` as `python2`, instead of `python3` (you can tell that by sending `realpath $(which python)`), as debian and debian based distros do (Ubuntu and Linux Mint are examples), use `pip3` instead of `pip` to install these dependencies with:

Install them with:
```
pip install --user numpy netcdf4 pillow
# or, if  python3 isn't default,
pip3 install --user numpy scipy pillow
```


## USAGE



```sh
./nc2jpg.py INPUT_FILE_PATH.nc
```

Image output to INPUT_FILE_PATH.jpg


## contact

  - *Name*: Marcos Conceição
  - *E-mail*: [marcosrdac@gmail.com](mailto:marcosrdac@gmail.com)
  - *GitHub*: [marcosrdac](github.com/marcosrdac)
  - *Website*: [marcosrdac.github.io](http://marcosrdac.github.io)
