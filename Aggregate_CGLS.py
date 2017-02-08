
from osgeo import gdal
import numpy
import sys
import os.path

#------------------------------------------------------------------------
# Program written to convert the C-GLS BA continental maps into TIF files
# 
# Bernardo Mota (bwcmota@gmail.com)
# Date: 29 October 2015
#------------------------------------------------------------------------


year=numpy.int(sys.argv[1]) 
mth=numpy.int(sys.argv[2])-1
cont=numpy.int(sys.argv[3])

#  SUBDATASET_1_NAME=HDF5:"g2_BIOPAR_BA_200601310000_AFRI_VGT_V1_3.h5"://ba_product_dekad
#  SUBDATASET_1_DESC=[8960x10080] //ba_product_dekad (8-bit unsigned character)
#  SUBDATASET_2_NAME=HDF5:"g2_BIOPAR_BA_200601310000_AFRI_VGT_V1_3.h5"://fdob_product_dekad
#  SUBDATASET_2_DESC=[8960x10080] //fdob_product_dekad (16-bit unsigned integer)
#  SUBDATASET_3_NAME=HDF5:"g2_BIOPAR_BA_200601310000_AFRI_VGT_V1_3.h5"://fdob_product_fire_season
#  SUBDATASET_3_DESC=[8960x10080] //fdob_product_fire_season (16-bit unsigned integer)
#  SUBDATASET_4_NAME=HDF5:"g2_BIOPAR_BA_200601310000_AFRI_VGT_V1_3.h5"://obs_passed_dekad
#  SUBDATASET_4_DESC=[8960x10080] //obs_passed_dekad (8-bit unsigned character)

#continents=['AFRI', 'ASIA', 'EURO', 'NOAM', 'OCEA', 'SOAM']


path_in="/home/wildube/teste/"


factor=(year-1980)*1000


if cont==1:
	res=0.00892857142857
	UL=[-30.0, 40.0]
	cname='AFRI'
if cont==2:
	res=0.00892857142857
	UL=[-170.0, 80.0]
	cname='NOAM'

if cont==3:
	res=0.00892857142857
	UL=[-110.0, 20.0]
	cname='SOAM'

if cont==4:
	res=0.00892857142857
	UL=[60.0, 80.0]
	cname='ASIA'

if cont==5:
	res=0.00892857142857
	UL=[-30.0, 80.0]
	cname='EURO'

if cont==6:
	res=0.00892857142857
	UL=[100.0, 0.0]
	cname='OCEA'


month=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] 

mes=month[mth]
compo=['10', '20', '31'] 
if mes=='02':
	if (year==2000) or (year==2004) or (year==2008) or (year==2012) or (year==2016):
		compo=['10', '20', '29'] 
	else:
		compo=['10', '20', '28'] 
if (mes=='04') or (mes=='06') or (mes=='04') or (mes=='06') or (mes=='09') or (mes=='11'):
	compo=['10', '20', '30'] 

file_name = str(path_in)+str(year)+str(mes)+str(compo[0])+str('/g2_BIOPAR_BA_')+str(year)+str(mes)+str(compo[0])+str('0000_')+str(cname)+str('_VGT_V1_3.h5')
answer=os.path.isfile(file_name)
tag=0
if answer==False:
	tag=1
	file_name = str(path_in)+str(year)+str(mes)+str(compo[0])+str('/g2_BIOPAR_BA_')+str(year)+str(mes)+str(compo[0])+str('0000_')+str(cname)+str('_VGT_V1.3.h5')
	answer2=os.path.isfile(file_name)
	if answer2==False:
		print "cannot process"+str(year)+str(mes)+str(compo[0])

gdal_file = gdal.Open ("HDF5:"+file_name+"://ba_product_dekad")
dekad_granule = gdal_file.ReadAsArray() # no factor needed
gdal_file = gdal.Open ("HDF5:"+file_name+"://fdob_product_dekad")
fdob_granule = gdal_file.ReadAsArray() # no factor needed
if tag==1:
	nl,nc=dekad_granule.shape
	dekad_granule=dekad_granule[0:nl-1,0:nc-1]
	fdob_granule=dekad_granule[0:nl-1,0:nc-1]

ba_map=numpy.uint16(dekad_granule)
ba_map[ba_map>=254]=ba_map[ba_map>=254]*10
ba_map[dekad_granule==1]=fdob_granule[dekad_granule==1]-factor
ba_map_geral=ba_map

file_name = str(path_in)+str(year)+str(mes)+str(compo[1])+str('/g2_BIOPAR_BA_')+str(year)+str(mes)+str(compo[1])+str('0000_')+str(cname)+str('_VGT_V1_3.h5')
answer=os.path.isfile(file_name)
tag=0
if answer==False:
	tag=1
	file_name = str(path_in)+str(year)+str(mes)+str(compo[1])+str('/g2_BIOPAR_BA_')+str(year)+str(mes)+str(compo[1])+str('0000_')+str(cname)+str('_VGT_V1.3.h5')
	answer2=os.path.isfile(file_name)
	if answer2==False:
		print "cannot process"+str(year)+str(mes)+str(compo[0])
gdal_file = gdal.Open ("HDF5:"+file_name+"://ba_product_dekad")
dekad_granule = gdal_file.ReadAsArray() # no factor needed
gdal_file = gdal.Open ("HDF5:"+file_name+"://fdob_product_dekad")
fdob_granule = gdal_file.ReadAsArray() # no factor needed

if tag==1:
	nl,nc=dekad_granule.shape
	dekad_granule=dekad_granule[0:nl-1,0:nc-1]
	fdob_granule=dekad_granule[0:nl-1,0:nc-1]
ba_map=numpy.uint16(dekad_granule)
ba_map[ba_map>=254]=ba_map[ba_map>=254]*10
ba_map[dekad_granule==1]=fdob_granule[dekad_granule==1]-factor
ba_map_geral[(ba_map>0) & (ba_map<2540)]=ba_map[(ba_map>0) & (ba_map<2540)]

file_name = str(path_in)+str(year)+str(mes)+str(compo[2])+str('/g2_BIOPAR_BA_')+str(year)+str(mes)+str(compo[2])+str('0000_')+str(cname)+str('_VGT_V1_3.h5')
answer=os.path.isfile(file_name)
tag=0
if answer==False:
	tag=1
	file_name = str(path_in)+str(year)+str(mes)+str(compo[2])+str('/g2_BIOPAR_BA_')+str(year)+str(mes)+str(compo[2])+str('0000_')+str(cname)+str('_VGT_V1.3.h5')
	answer2=os.path.isfile(file_name)
	if answer2==False:
		print "cannot process"+str(year)+str(mes)+str(compo[0])
gdal_file = gdal.Open ("HDF5:"+file_name+"://ba_product_dekad")
dekad_granule = gdal_file.ReadAsArray() # no factor needed
gdal_file = gdal.Open ("HDF5:"+file_name+"://fdob_product_dekad")
fdob_granule = gdal_file.ReadAsArray() # no factor needed
if tag==1:
	nl,nc=dekad_granule.shape
	dekad_granule=dekad_granule[0:nl-1,0:nc-1]
	fdob_granule=dekad_granule[0:nl-1,0:nc-1]
ba_map=numpy.uint16(dekad_granule)
ba_map[ba_map>=254]=ba_map[ba_map>=254]*10
ba_map[dekad_granule==1]=fdob_granule[dekad_granule==1]-factor
ba_map_geral[(ba_map>0) & (ba_map<2540)]=ba_map[(ba_map>0) & (ba_map<2540)]


Ncas=dekad_granule.shape
out_file=str(path_in)+str('CGLS_BA_')+str(cname)+str('_')+str(year)+str('_')+str(mes)+str('.tif')
driver = gdal.GetDriverByName("GTiff")
ds = driver.Create(str(out_file), numpy.int(Ncas[1]), numpy.int(Ncas[0]), 1, gdal.GDT_UInt16)
ds.SetGeoTransform((UL[0], res, 0.0, UL[1], 0.0, -res))
#ds.SetGeoTransform(map_trans)
ds.SetProjection('GEOGCS["WGS 84",DATUM["WGS_1984",SPHEROID["WGS 84",6378137,298.257223563,AUTHORITY["EPSG","7030"]],AUTHORITY["EPSG","6326"]],PRIMEM["Greenwich",0],UNIT["degree",0.0174532925199433],AUTHORITY["EPSG","4326"]]')
#ds.SetProjection(map_proj)
ds.GetRasterBand(1).WriteArray(ba_map_geral)
#ds.GetRasterBand(2).WriteArray(fdob_granule)
#ds.GetRasterBand(3).WriteArray(fdobFS_granule)
#ds.GetRasterBand(4).WriteArray(obs_granule)
ds = None

