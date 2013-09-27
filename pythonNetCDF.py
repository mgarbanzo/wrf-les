from scipy.io import netcdf
import matplotlib.pyplot as plt

OUTDIR='/home/m5k/WRF-LES/python-out/'

f = netcdf.netcdf_file('/home/m5k/WRF-LES/wrfoutLARGE.nc', 'r')
zonal=f.variables['U']
meridional=f.variables['V']
vertical=f.variables['W']

#zs = range(zonal.shape[1])
zs = 2,

for H in zs:
    for t in range(f.variables['Times'].shape[0]):
        plt.imshow(zonal[t][H], vmin=-10, vmax=10)
        plt.xlabel("Distance 5km")
        plt.xlabel("Distance 5km")
        plt.title( "Zonal Wind." + " Time: " + str(t) + " Z: " + str(H) )
        cmap=plt.cm.RdBu
        plt.colorbar()
        plt.savefig(OUTDIR+'zonal'+'T'+str(t)+'H'+str(H)+'.png', dpi=100)
        plt.close()

        plt.imshow(meridional[t][H], vmin=-1, vmax=1)
        plt.xlabel("Distance 5km")
        plt.xlabel("Distance 5km")
        plt.title( "Meridional Wind." + " Time: " + str(t) + " Z: " + str(H) )
        cmap=plt.cm.RdBu
        plt.colorbar()
        plt.savefig(OUTDIR+'meridional'+'T'+str(t)+'H'+str(H)+'.png', dpi=100)
        plt.close()

        plt.imshow(vertical[t][H], vmin=-1, vmax=1)
        plt.xlabel("Distance 5km")
        plt.xlabel("Distance 5km")
        plt.title( "Vertical Wind." + " Time: " + str(t) + " Z: " + str(H) )
        cmap=plt.cm.RdBu
        plt.colorbar()
        plt.savefig(OUTDIR+'vertical'+'T'+str(t)+'H'+str(H)+'.png', dpi=100)
        plt.close()
