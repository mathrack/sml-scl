##################################################################
# Flageul and Tiselj
# https://doi.org/10.1016/j.ijheatfluidflow.2017.10.009
##################################################################

from numpy import *
from pylab import *
import xlrd

matplotlib.rc('figure', figsize=(5.83,4.13))
matplotlib.rc('text', usetex = True)
size=16
size_legend=14
size_label=20
linewidth=1.5
markersize=10
matplotlib.rc('lines', linewidth=linewidth,markersize=markersize)
matplotlib.rc('font', size=size)
matplotlib.rc('axes', labelsize=size_label, titlesize=size)
matplotlib.rc('legend', fontsize=size_legend)

#
def purge(L):
    return array([x for x in L if x <> ''])

class case(object):
    def __init__(self, xlsfile, fact, ncell, i, j):
         self.file = xlsfile
         self.ny = ncell
         self.wkbk = xlrd.open_workbook(self.file)
         self.sht = self.wkbk.sheet_by_name('Sheet1')
         self.y = purge(self.sht.col_values(7*(i-1)+1)[((j-1)*(self.ny+2)+1):((j-1)*(self.ny+2)+self.ny+1)])
         self.dat1 = fact*(purge(self.sht.col_values(7*(i-1)+2)[((j-1)*(self.ny+2)+1):((j-1)*(self.ny+2)+self.ny+1)]))
         self.sig1 = fact*2*purge(self.sht.col_values(7*(i-1)+3)[((j-1)*(self.ny+2)+1):((j-1)*(self.ny+2)+self.ny+1)])

#
# 1 <= i <= 6 : scalars, larger i, coarser grid
# i = 7 : streamwise velocity
#
# j = 2 > y2z2
#     3 > x2z2
#     4 > x2y2
#     5 > z4
#     6 > y4
#     7 > x4
#     8 > yz
#     9 > xz
#     10 > xy
#     11 > z2
#     12 > y2
#     13 > x2
#     14 > dfdz
#     15 > f4
#     16 > f3
#     17 > f2
#     18 > f

j = 17
ny = 181
re = 160
fct = re**2

i = 1
sca1 = case('./fort.stat.xlsm', fct, ny, i, j)

for i in [2, 3, 4, 5, 6]:
    sca = case('./fort.stat.xlsm', fct, ny, i, j)
    print log10(trapz((sca1.dat1-sca.dat1)**2,sca1.y)/trapz(sca1.dat1**2,sca1.y)),trapz(sca.dat1**2,sca1.y)/trapz(sca1.dat1**2,sca1.y)
