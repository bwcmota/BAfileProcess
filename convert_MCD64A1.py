from osgeo import gdal,osr,ogr
import numpy
import sys

#-----------------------------------------------------------------------
# Program written to convert the MCD64A1 HDF files into TIF files 
# 
# Bernardo Mota (bernardo.mota@jrc.ec.europa.eu)
# Date: 29 October 2015
#-----------------------------------------------------------------------


#new_file='/home/admin/FAPAR_vComp/new/S2003121_2003151.GS_000_020'
#new_tiff='/home/admin/FAPAR_vComp/old/S2003121_2003151.GS_000_020'
new_file=sys.argv[1] #'/home/admin/bernardo/BA_datasets/MCD64A1/h12v04/MCD64A1.A2003182.h12v04.051.2014205233014.hdf'
#new_tif='home/admin/bernardo/BA_datasets/test.tif'
new_tif=sys.argv[2] #'/home/admin/Documents/teste2.tif'



# load data, new version
c_1 = gdal.Open ("HDF4_EOS:EOS_GRID:"+new_file+":MOD_Grid_Monthly_500m_DB_BA:Burn Date")
band_1 = c_1.ReadAsArray()
c_2 = gdal.Open ("HDF4_EOS:EOS_GRID:"+new_file+":MOD_Grid_Monthly_500m_DB_BA:Burn Date Uncertainty")
band_2 = c_2.ReadAsArray()
c_3 = gdal.Open ("HDF4_EOS:EOS_GRID:"+new_file+":MOD_Grid_Monthly_500m_DB_BA:QA")
band_3 = c_3.ReadAsArray()
c_4 = gdal.Open ("HDF4_EOS:EOS_GRID:"+new_file+":MOD_Grid_Monthly_500m_DB_BA:First Day")
band_4 = c_4.ReadAsArray()
c_5 = gdal.Open ("HDF4_EOS:EOS_GRID:"+new_file+":MOD_Grid_Monthly_500m_DB_BA:Last Day")
band_5 = c_5.ReadAsArray()

numcolunas, numlinhas = band_1.shape

driver = gdal.GetDriverByName("GTiff")
ds = driver.Create(str(new_tif), numpy.int(numcolunas), numpy.int(numlinhas), 5, gdal.GDT_Int16)
ds.SetGeoTransform(c_1.GetGeoTransform())
ds.SetDescription(c_1.GetDescription())
ds.SetProjection(c_1.GetProjection())
ds.GetRasterBand(1).WriteArray(band_1)
ds.GetRasterBand(2).WriteArray(band_2)
ds.GetRasterBand(3).WriteArray(band_3)
ds.GetRasterBand(4).WriteArray(band_4)
ds.GetRasterBand(5).WriteArray(band_5)
ds = None
