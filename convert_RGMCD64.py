from osgeo import gdal,osr,ogr
import numpy
import sys

#-----------------------------------------------------------------------
# Program written to aggregate the global MCD64A1 maps into coarser 
#  resolutions based on proportion of BA extent
# 
# Bernardo Mota (bernardo.mota@jrc.ec.europa.eu)
# Date: 29 October 2015
#-----------------------------------------------------------------------


in_file=sys.argv[1] 
continent=numpy.int(sys.argv[2])
resolution=numpy.float(sys.argv[3])

print('--------------------------------------------------------------')
print('Resampling file :')
print('  '+str(in_file))
print('  into '+str(resolution)+str(' dregrees'))

if continent==0:
	area='Globe'
	UL=[-180.0, 90.0]
	RES=0.005	
	if resolution==0.5:
		step=100
		limlon=720
		limlat=360
		resname='050'
	if resolution==0.25:
		step=50
		limlon=1440
		limlat=720
		resname='025'
	if resolution==0.10:
		step=20
		limlon=3600
		limlat=1800
		resname='010'
	if resolution==0.05:
		step=10
		limlon=7200
		limlat=3600
		resname='005'

if continent==1:
	area='Africa'
	UL=[-20.0, 40.0]
	RES=0.005	
	if resolution==0.5:
		step=100
		limlon=156
		limlat=152
		resname='050'
	if resolution==0.25:
		step=50
		limlon=312
		limlat=304
		resname='025'

if continent==2:
	area='NAmerica'
	UL=[-180.0, 80.0]
	RES=0.005	
	if resolution==0.5:
		step=100
		limlon=260
		limlat=140
		resname='050'
	if resolution==0.25:
		step=50
		limlon=520
		limlat=280
		resname='025'

if continent==3:
	area='SAmerica'
	UL=[-105.0, 20.0]
	RES=0.005	
	if resolution==0.5:
		step=100
		limlon=140
		limlat=156
		resname='050'
	if resolution==0.25:
		step=50
		limlon=280
		limlat=312
		resname='025'

if continent==4:
	area='Asia'
	UL=[30.0, 80.0]
	RES=0.005	
	if resolution==0.5:
		step=100
		limlon=300
		limlat=160
		resname='050'
	if resolution==0.25:
		step=50
		limlon=600
		limlat=320
		resname='025'

if continent==5:
	area='Europe'
	UL=[-10.0, 80.0]
	RES=0.005	
	if resolution==0.5:
		step=100
		limlon=100
		limlat=100
		resname='050'
	if resolution==0.25:
		step=50
		limlon=200
		limlat=200
		resname='025'

if continent==6:

	area='Oceania'
	UL=[90.0, 20.0]
	RES=0.005	
	if resolution==0.5:
		step=100
		limlon=180
		limlat=120
		resname='050'
	if resolution==0.25:
		step=50
		limlon=360
		limlat=240
		resname='025'


print('File with '+str(limlat)+str(' lines X ')+str(limlon)+str(' columns'))
print('Study region: '+str(area))
print('--------------------------------------------------------------')

out_file=str(in_file[0:-4])+str('_')+str(resname)+str('.tif')

# load data, new version
c_1 = gdal.Open (str(in_file))
band_1 = c_1.GetRasterBand(1)
BDate = band_1.ReadAsArray()
band_2 = c_1.GetRasterBand(2)
BDateUnc = band_2.ReadAsArray()
band_3 = c_1.GetRasterBand(3)
QA = band_3.ReadAsArray()
numlinhas, numcolunas = BDate.shape
BA_nD=numpy.zeros((limlat, limlon)) # Number of pixels burned
BA_nP=numpy.zeros((limlat, limlon)) # Number of pixels processed (Not==-1)
BA_MD=numpy.zeros((limlat, limlon)) # Median day of burnt (excluding the 0 and -1)
BA_mD=numpy.zeros((limlat, limlon)) # minimum day of burnt event in the cell (excluding 0 and -1)

BA_MU=numpy.zeros((limlat, limlon)) # Median day of Uncertainty (excluding the 0 and -1 day flags)

for lat02 in range(0, limlat):
	for lon02 in range(0, limlon):
		varDB=numpy.reshape(BDate[(lat02*step):(lat02*step)+step,(lon02*step):(lon02*step)+step], step*step)
		varUN=numpy.reshape(BDateUnc[(lat02*step):(lat02*step)+step,(lon02*step):(lon02*step)+step], step*step)
		BA_nP[lat02, lon02]=(step*step)-varDB[varDB==-1].shape[0]
		BA_nD[lat02, lon02]=varDB[varDB>0].shape[0]
		if BA_nD[lat02, lon02]>0:
			BA_MD[lat02, lon02]=numpy.median(varDB[varDB>0])
			BA_mD[lat02, lon02]=numpy.min(varDB[varDB>0])
			BA_MU[lat02, lon02]=numpy.mean(varUN[varDB>0])

#c_1 = gdal.Open ("HDF4_EOS:EOS_GRID:"+new_file+":MOD_Grid_Monthly_500m_DB_BA:Burn Date")
#c_2 = gdal.Open ("HDF4_EOS:EOS_GRID:"+new_file+":MOD_Grid_Monthly_500m_DB_BA:Burn Date Uncertainty")
#c_3 = gdal.Open ("HDF4_EOS:EOS_GRID:"+new_file+":MOD_Grid_Monthly_500m_DB_BA:QA")
#c_4 = gdal.Open ("HDF4_EOS:EOS_GRID:"+new_file+":MOD_Grid_Monthly_500m_DB_BA:First Day")
#c_5 = gdal.Open ("HDF4_EOS:EOS_GRID:"+new_file+":MOD_Grid_Monthly_500m_DB_BA:Last Day")

driver = gdal.GetDriverByName("GTiff")
ds = driver.Create(str(out_file), numpy.int(limlon), numpy.int(limlat), 5, gdal.GDT_Int16)

#ds.SetGeoTransform(c_1.GetGeoTransform())
ds.SetGeoTransform((UL[0], resolution, 0.0, UL[1], 0.0, -resolution))
#ds.SetDescription(c_1.GetDescription())
ds.SetProjection(c_1.GetProjection())

ds.GetRasterBand(1).WriteArray(BA_nP)
ds.GetRasterBand(2).WriteArray(BA_nD)
ds.GetRasterBand(3).WriteArray(BA_MD)
ds.GetRasterBand(4).WriteArray(BA_mD)
ds.GetRasterBand(5).WriteArray(BA_MU)
ds = None
