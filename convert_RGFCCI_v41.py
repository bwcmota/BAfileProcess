from osgeo import gdal,osr,ogr
import numpy
import sys

#------------------------------------------------------------------------
# Program written to aggregate the continental Fire CCI maps into coarser 
#  resolutions based on proportion of BA extent
# 
# Bernardo Mota (bwcmota@gmail.com)
# Date: 29 October 2015
#------------------------------------------------------------------------

 
in_file=sys.argv[1] 
in_file2=sys.argv[2] 
continent=numpy.int(sys.argv[3])
resolution=numpy.float(sys.argv[4])

print('--------------------------------------------------------------')
print('Resampling file :')
print('  '+str(in_file))
print('  into '+str(resolution)+str(' dregrees'))

RES=0.005	
if continent==1:
	area='NAmerica'
	UL=[-180.0, 83.0]
	LR=[-50.0, 19.0]
if continent==2:
	area='SAmerica'
	UL=[-105.0, 19.0]
	LR=[-34.0, -57.0]
if continent==3:
	area='Europe'
	UL=[-26.0, 83.0]
	LR=[53.0, 25.0]
if continent==4:
	area='Asia'
	UL=[53.0, 83.0]
	LR=[180.0, 0.0]
if continent==5:
	area='Africa'
	UL=[-26.0, 25.0]
	LR=[53.0, -40.0]
if continent==6:
	area='Oceania'
	UL=[95.0, 0.0]
	LR=[180.0, -53.0]
if resolution==0.5:
	step=200
	resname='050'
if resolution==0.25:
	step=100
	resname='025'
if resolution==0.10:
	step=40
	resname='025'
if resolution==0.05:
	step=20
	resname='025'
limlon=numpy.int((LR[0]-UL[0])/resolution)
limlat=numpy.int((UL[1]-LR[1])/resolution)
		


print('File with '+str(limlat)+str(' lines X ')+str(limlon)+str(' columns'))
print('Study region: '+str(area))
print('--------------------------------------------------------------')

# load data, new version
c_1 = gdal.Open (str(in_file))
band_1 = c_1.GetRasterBand(1)
BDate = band_1.ReadAsArray()
band_2 = c_1.GetRasterBand(2)
BDateUnc = band_2.ReadAsArray()

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
		BA_nP[lat02, lon02]=(step*step)-varDB[varDB>900].shape[0] # pixels not processed have a value of 999
		BA_nD[lat02, lon02]=varDB[(varDB>0) & (varDB<900)].shape[0] # detected burnt pixels have a value betweem 1 and 366
		if BA_nD[lat02, lon02]>0:
			BA_MD[lat02, lon02]=numpy.median(varDB[(varDB>0) & (varDB<900)])
			BA_mD[lat02, lon02]=numpy.min(varDB[(varDB>0) & (varDB<900)])
			BA_MU[lat02, lon02]=numpy.mean(varUN[(varDB>0) & (varDB<900)])

driver = gdal.GetDriverByName("GTiff")
ds = driver.Create(str(in_file2), numpy.int(limlon), numpy.int(limlat), 5, gdal.GDT_Int32)

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
