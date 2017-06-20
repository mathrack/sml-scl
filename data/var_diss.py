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

ny = 181
re = 160
fct = (2./re)**2

# case 6S / 3S / 1KMM
for i in [1, 4, 6]:
    ref=zeros(ny)
    refr=zeros(ny)
    for j in [5, 6, 7]:
        sca1 = case('./fort.stat.xlsm', fct, ny, i, j)
        ref=ref+sca1.dat1
        refr=refr+sca1.sig1
    for j in [2, 3, 4]:
        sca1 = case('./fort.stat.xlsm', fct, ny, i, j)
        ref=ref+2*sca1.dat1
        refr=refr+2*sca1.sig1
    ref2=zeros(ny)
    ref2r=zeros(ny)
    for j in [11, 12, 13]:
        sca1 = case('./fort.stat.xlsm', sqrt(fct), ny, i, j)
        ref2=ref2+sca1.dat1
#        ref2r=ref2r+sca1.sig1
#    ref=ref-square(ref2)
    if i == 1:
        plot(sca1.y,ref+refr-square(ref2-ref2r),'--',color='k',label='6S')
        plot(sca1.y,ref-refr-square(ref2+ref2r),'--',color='k')
    elif i == 4:
        plot(sca1.y,ref+refr-square(ref2-ref2r),'-.',color='g',label='3S')
        plot(sca1.y,ref-refr-square(ref2+ref2r),'-.',color='g')
    elif i == 6:
        plot(sca1.y,ref+refr-square(ref2-ref2r),':',color='b',label='1KMM')
        plot(sca1.y,ref-refr-square(ref2+ref2r),':',color='b')

#Graph settings
xscale('linear')
yscale('linear')
axis([-1,1,0.001,0.035])
xlabel(r"$y$")
ylabel(r"Variance of $\varepsilon_\theta$")

legend(bbox_to_anchor=(0.35,0.65),numpoints=1)
savefig("var_diss.png",bbox_inches='tight')
savefig("var_diss.pdf",bbox_inches='tight')
