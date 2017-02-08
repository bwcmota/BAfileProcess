from osgeo import gdal,osr,ogr
import numpy
import sys

#-----------------------------------------------------------------------
# Program written to convert the MCD64A1 HDF files into TIF files 
# 
# Bernardo Mota (bwcmota@gmail.com)
# Date: 29 October 2015
#-----------------------------------------------------------------------

new_file=sys.argv[1] #'/home/admin/bernardo/BA_datasets/MCD64A1/h12v04/MCD64A1.A2003182.h12v04.051.2014205233014.hdf'
new_tif=sys.argv[2] #'/home/admin/Documents/teste2.tif'


# load data, new version
c_1 = gdal.Open ("HDF4_EOS:EOS_GRID:"+new_file+":MOD_GRID_Monthly_500km_BA:burndate")
band_1 = c_1.ReadAsArray()
c_2 = gdal.Open ("HDF4_EOS:EOS_GRID:"+new_file+":MOD_GRID_Monthly_500km_BA:ba_qa")
band_2 = c_2.ReadAsArray()


numcolunas, numlinhas = band_1.shape

driver = gdal.GetDriverByName("GTiff")
ds = driver.Create(str(new_tif), numpy.int(numcolunas), numpy.int(numlinhas), 2, gdal.GDT_Int16)
ds.SetGeoTransform(c_1.GetGeoTransform())
ds.SetDescription(c_1.GetDescription())
ds.SetProjection(c_1.GetProjection())
ds.GetRasterBand(1).WriteArray(band_1)
ds.GetRasterBand(2).WriteArray(band_2)

ds = None
