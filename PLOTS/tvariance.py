##################################################################
# Flageul and Tiselj
# https://doi.org/10.1016/j.ijheatfluidflow.2017.10.009
##################################################################

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
    def __init__(self, xlsfile, ncell):
         self.file = xlsfile
         self.ny = ncell
         self.wkbk = xlrd.open_workbook(self.file)
         self.sht = self.wkbk.sheet_by_name('tvariance')
         self.y = purge(self.sht.col_values(1)[2:self.ny])
         self.L18dat = purge(self.sht.col_values(2)[2:self.ny])
         self.L18sig = 2*purge(self.sht.col_values(3)[2:self.ny])
         self.L18 = self.L18sig / (self.L18dat + self.L18sig)
         self.S18dat = purge(self.sht.col_values(9)[2:self.ny])
         self.S18sig = 2*purge(self.sht.col_values(10)[2:self.ny])
         self.S18 = self.S18sig / (self.S18dat + self.S18sig)
         self.L16dat = abs(purge(self.sht.col_values(16)[2:self.ny]))
         self.L16sig = 2*purge(self.sht.col_values(17)[2:self.ny])
         self.L16 = self.L16sig / (self.L16dat + self.L16sig)
         self.S16dat = abs(purge(self.sht.col_values(23)[2:self.ny]))
         self.S16sig = 2*purge(self.sht.col_values(24)[2:self.ny])
         self.S16 = self.S16sig / (self.S16dat + self.S16sig)

sec3 = case('./section3.xlsx', 129)

#Graph settings
xscale('linear')
yscale('log')
axis([-1,1,0.001,1.])
xlabel(r"$y$")
ylabel(r"$E[\theta'^2]$")

plot(sec3.y,sec3.L18,'-',color='k',label=r'$18L$')
plot(sec3.y,sec3.S18,'--',color='r',label=r'$18S$')
plot(sec3.y,sec3.L16,'-.',color='g',label=r'$16L$')
plot(sec3.y,sec3.S16,':',color='b',label=r'$16S$')

savefig("tvariance.png",bbox_inches='tight')
savefig("tvariance.pdf",bbox_inches='tight')
