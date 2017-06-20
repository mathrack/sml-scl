from numpy import *
from pylab import *
import xlrd

matplotlib.rc('figure', figsize=(2*5.,4.13))
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
fct = 2./re

#Graph settings
xscale('linear')
yscale('linear')
xlabel(r"$y$")
ylabel(r"Anisotropy of $\overline{ \partial_i T' \partial_j T' }$")
axis([-1.,1.,0.,1.])
#text(0.93,0.15,'1C')
#text(-1.08,0.15,'2C')
#text(0.1,1.65,'3C')
#plot([-1,1,0,-1],[0,0,sqrt(3),0],'-',color='k')

x=zeros(ny)
y=zeros(ny)
z=zeros(ny)

# case 6S / 3S / 1KMM
for i in [1]:#, 4, 6]:
    j = 13
    sca1 = case('./fort.stat.xlsm', fct, ny, i, j)
    refxx=sca1.dat1
    j = j-1
    sca1 = case('./fort.stat.xlsm', fct, ny, i, j)
    refyy=sca1.dat1
    j = j-1
    sca1 = case('./fort.stat.xlsm', fct, ny, i, j)
    refzz=sca1.dat1
    j = j-1
    sca1 = case('./fort.stat.xlsm', fct, ny, i, j)
    refxy=sca1.dat1
    j = j-1
    sca1 = case('./fort.stat.xlsm', fct, ny, i, j)
    refxz=sca1.dat1
    j = j-1
    sca1 = case('./fort.stat.xlsm', fct, ny, i, j)
    refyz=sca1.dat1
    for ii in range(refxx.size):
        mat = array([ [refxx[ii],refxy[ii],refxz[ii]], [refxy[ii],refyy[ii],refyz[ii]], [refxz[ii],refyz[ii],refzz[ii]] ])
        lambdas = flipud(eigvalsh( mat/(refxx[ii]+refyy[ii]+refzz[ii])-identity(3)/3 ))
        c1c = lambdas[0]-lambdas[1]
        c2c = 2*(lambdas[1]-lambdas[2])
        c3c = 3*lambdas[2]+1
        x[ii] = c1c#-c2c
        y[ii] = c2c#c3c*sqrt(3)
        z[ii] = c3c
    if i == 1:
#        plot(x,y,'--',color='k',label='6S')
        plot(sca1.y,x,'--',color='k',label='1C')
        plot(sca1.y,y,'-.',color='g',label='2C')
        plot(sca1.y,z,':',color='b',label='3C')
        grid(True)
        gca().set_xticks(arange(-1,1.1,0.1))
        gca().xaxis.grid(True,'both')
    elif i == 4:
        plot(x,y,'-.',color='g',label='3S')
    elif i == 6:
        plot(x,y,':',color='b',label='1KMM')

legend(bbox_to_anchor=(0.65,0.65),numpoints=1)
savefig("tmp.png",bbox_inches='tight')
savefig("tmp.pdf",bbox_inches='tight')
