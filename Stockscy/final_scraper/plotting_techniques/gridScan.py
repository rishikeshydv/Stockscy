import os, sys
import matplotlib.pyplot as plt
import numpy as np
fL_step = 0.015
fR_step = 0.0067
fL = np.arange(-3, 4, 1)*fL_step + 0.3112
fR = np.arange(-1, 7, 1)*fR_step + 0.0017
print(fR)
for indx, val in enumerate(fR):
    if val < 0:
        fR[indx] = 0
print(fR)
c_fR = np.take(fR, fR.size // 5)
c_fL = np.take(fL, fL.size // 2)
x,y = np.meshgrid(fR, fL)
plt.xlabel("$f_{R}$", horizontalalignment='right', fontsize=12, x=1.0, fontweight='bold')
plt.ylabel("$f_{L}$", horizontalalignment='right', fontsize=12, labelpad=10, y=0.95)
plt.xlim(-0.0001, fR[fR.size-1]+0.0001)
plt.ylim(fL[0]-0.001, fL[fL.size-1]+0.001)
plt.annotate(s='Nominal value at index (0,0)', xy=(c_fR, c_fL), xytext=(c_fR + 2*fR_step, c_fL + 1.25*fL_step), arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
plt.annotate(s='', xy=(c_fR,c_fL), xytext=(c_fR + fR_step, c_fL), arrowprops=dict(arrowstyle='<-', color='red', lw=1.5))
#plt.annotate(s='', xy=(c_fR,c_fL), xytext=(c_fR - fR_step, c_fL), arrowprops=dict(arrowstyle='<-', color='red', lw=1.5))
plt.annotate(s='', xy=(c_fR,c_fL), xytext=(c_fR, c_fL + fL_step), arrowprops=dict(arrowstyle='<-', color='blue', lw=1.5))
plt.annotate(s='', xy=(c_fR,c_fL), xytext=(c_fR, c_fL - fL_step), arrowprops=dict(arrowstyle='<-', color='blue', lw=1.5))
plt.text(x=c_fR + fR_step/3, y=c_fL - fL_step/2, s=r"+$\Delta f_{R}$ = " + str(fR_step) + r" $\approx 0.5\sigma$", color='red')
plt.text(x=0.003, y=c_fL + fL_step/3, s=r"+$\Delta f_{L}$ = " + str(fL_step) + r" $\approx 1\sigma$", color='blue', rotation=90)
#plt.text(x=c_fR + fR_step/2, y=c_fL + fL_step/3, s=r"+$\Delta f_{L}$ = " + str(fL_step), color='blue')
plt.text(x=fR[0], y=fL[fL.size-1] +fL_step/2, s=r"Grid-Scan for different helicity fractions", color='blue', fontweight='bold')
plt.xticks(fR, rotation=45)
plt.yticks(fL, rotation=45)
plt.tick_params(axis='both', labelsize=10)
plt.scatter(x,y)
plt.tight_layout()
#plt.savefig("/Users/ishan/work_temp/plots/GridScan_template.pdf")
plt.show()
sys.exit(0)
