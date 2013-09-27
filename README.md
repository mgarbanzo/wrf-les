wrf-les
=======

WRF-LES Simulation code to visualize the products

FILES: 

=== writeNetCDF.py

Created to extract the variable W from the large NetCDF 
file that the WRF outputs. The problem with that NetCDF
container is that the variable is presented to Paraview
as a 4 dimensional structure that the program can't
open properly.

Once the variable has been extracted the Paraview can
open it without problem.


=== pythonNetCDF.py


The initial program was intended to visualize and
generate products from python. IDV does a better
job because it would require a lot of time to 
achieve the same level of results.

For the moment I am sticking with IDV for 2D crossed
sections of the data and with Paraview for 3D output.

