#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#importing libraries 
import arcpy
from arcpy import env
from arcpy.sa import*

# check out the Spatial Analyst extension
arcpy.CheckOutExtension("Spatial")

# set the input environment
env.workspace = r''
# set the output path
output_path = r''

# Define headWater values for each DEM raster uisng Dic
X_values = {
    'dem_ft_0': 11.46,
    'dem_ft_1': 11.48,
    'dem_ft_2': 9.02,
    'dem_ft_3': 41.04,
}
# loop through each raster in the workspace
 for raster in arcpy.ListRasters ('dem_ft_*'):
        # get the corresponding X value
        X = X_values[raster]
        
        # perform the calculation
        raster_obj = Raster(raster)
        output_raster = (X-raster_obj)/0.46
        
        # get the DEM number from the raster name
        dem_num = raster.split('_')[-1]
        # save the output raster in tif format
        output_raster.save(f'{output_path}\inundation_king_tide_100y1d_SLR1_huc_{dem_number}.tif')
print('raster calculation is done!')
            
        
    
        

    
    
    
    
    

