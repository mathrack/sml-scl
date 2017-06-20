from numpy import *
from pylab import *
import xlrd

matplotlib.rc('figure', figsize=(5.,4.13))
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
    def __init__(self, xlsfile, ncell, i, j):
         self.file = xlsfile
         self.ny = ncell
         self.wkbk = xlrd.open_workbook(self.file)
         self.sht = self.wkbk.sheet_by_name('zspec')
         self.k = purge(self.sht.col_values(0)[2:(self.ny+2)])
         self.dat = purge(self.sht.col_values(7*(j-1)+i)[2:(self.ny+2)])
         self.k = self.k[1:self.dat.size]
         self.dat = self.dat[1:self.dat.size]

#
# 1 <= i <= 6 : scalars, larger i, coarser grid
#
# j = 1 > Z = 1, top wall
#     2 > Z = 0.9563, Z+ = 7
#     3 > Z = 0.7313, Z+ = 43
#     4 > Z = 0, middle of the channel

nx = 90
re = 160
j = 4


for i in [1, 4, 6]:
    cas = case('./ft6.xlsx', nx, i, j)
    if i == 1:
        plot(cas.k,cas.dat*(cas.k**(2.)),'--',color='k',label='6S')
    elif i == 4:
        plot(cas.k,cas.dat*(cas.k**(2.)),'-.',color='g',label='3S')
    elif i == 6:
        plot(cas.k,cas.dat*(cas.k**(2.)),':',color='b',label='1KMM')

#Graph settings
xscale('log')
yscale('log')
axis([0.017,1.0,0.0000000001,0.001])
xlabel(r"$k_z^+$")
ylabel(r"${k_z^+}^2 |T'(k_z^+, y = 0)|^2$")

legend(bbox_to_anchor=(0.5,0.5),numpoints=1)
savefig("z4.png",bbox_inches='tight')
savefig("z4.pdf",bbox_inches='tight')