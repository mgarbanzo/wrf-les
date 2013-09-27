from scipy.io import netcdf
from scipy.io.netcdf import NetCDFFile as Dataset
from numpy import arange, dtype # array module from http://numpy.scipy.org
nx = 159; ny = 39 ; nz = 40
ncfile = Dataset('/home/marcial/test_out.nc','w') 

f = netcdf.netcdf_file('/media/VERBATIM/LES/wrfout.nc', 'r')
vertical = f.variables['W']

data_out = arange(nx*ny*nz) # 1d array
data_out.shape = (nz,ny,nx) # reshape to 2d array

ncfile.createDimension('x',nx)
ncfile.createDimension('y',ny)
ncfile.createDimension('z',nz)
data = ncfile.createVariable('data',dtype('float32').char,('z','y','x'))
data[:] = vertical[100]
ncfile.close()
print '*** SUCCESS writing example file simple_xy.nc!'
