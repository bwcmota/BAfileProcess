#!/bin/bash

#-----------------------------------------------------------------------
# Program written to convert the MCD45A1 Tiles into global maps 
# 
# Bernardo Mota (bwcmota@gmail.com)
# Date: 29 October 2015
#-----------------------------------------------------------------------

echo "================================================================"
echo "= Script to merge and process BA MODIS tiles for MCD45A1"
echo "================================================================"

rundir="/home/wildube/Datasets/Global_BA_datasets/MCD45A1/"



product="MCD45A1.A"

year=2012
yearn='2012'


#composite=(001 032 060 091 121 152 182 213 244 274 305 335)	# non-leap-years
composite=(001 032 061 092 122 153 183 214 245 275 306 336)	# leap-years
mes=(01 02 03 04 05 06 07 08 09 10 11 12)


out_dir2="/home/wildube/CompositeData/AgreFireData/MCD45/"
out_dir="/home/wildube/BA_make"


patterns_globe=" h01v10 h03v06 h03v07 h03v10 h05v13 h07v03 h07v06 h08v03 h08v04 h08v05 h08v06 h08v07 h08v09 h09v02 h09v03 h09v04 h09v05 h09v06 h09v07 h09v08 h09v09 h10v02 h10v03 h10v04 h10v05 h10v06 h10v07 h10v08 h10v09 h10v10 h11v02 h11v03 h11v04 h11v05 h11v06 h11v07 h11v08 h11v09 h11v10 h11v11 h11v12 h12v01 h12v02 h12v03 h12v04 h12v05 h12v07 h12v08 h12v09 h12v10 h12v11 h12v12 h12v13 h13v01 h13v02 h13v03 h13v04 h13v08 h13v09 h13v10 h13v11 h13v12 h13v13 h13v14 h14v01 h14v02 h14v03 h14v04 h14v09 h14v10 h14v11 h14v14 h15v01 h15v02 h15v05 h15v14 h16v01 h16v02 h16v06 h16v07 h16v08 h17v01 h17v02 h17v03 h17v04 h17v05 h17v06 h17v07 h17v08 h18v01 h18v02 h18v03 h18v04 h18v05 h18v06 h18v07 h18v08 h18v09 h19v01 h19v02 h19v03 h19v04 h19v05 h19v06 h19v07 h19v08 h19v09 h19v10 h19v11 h19v12 h20v01 h20v02 h20v03 h20v04 h20v05 h20v06 h20v07 h20v08 h20v09 h20v10 h20v11 h20v12 h21v01 h21v02 h21v03 h21v04 h21v05 h21v06 h21v07 h21v08 h21v09 h21v10 h21v11 h22v01 h22v02 h22v03 h22v04 h22v05 h22v06 h22v07 h22v08 h22v09 h22v10 h22v11 h22v13 h23v01 h23v02 h23v03 h23v04 h23v05 h23v06 h23v07 h23v08 h23v11 h24v02 h24v03 h24v04 h24v05 h24v06 h24v07 h25v02 h25v03 h25v04 h25v05 h25v06 h25v07 h25v08 h26v02 h26v03 h26v04 h26v05 h26v06 h26v07 h26v08 h27v03 h27v04 h27v05 h27v06 h27v07 h27v08 h27v09 h27v12 h28v03 h28v04 h28v05 h28v06 h28v07 h28v08 h28v09 h28v11 h28v12 h28v13 h29v05 h29v06 h29v07 h29v08 h29v09 h29v10 h29v11 h29v12 h29v13 h30v07 h30v08 h30v09 h30v10 h30v11 h30v12 h30v13 h31v09 h31v10 h31v11 h31v12 h31v13 h32v09 h32v10 h32v12 h33v09 h33v11 h34v10"


for ((compo=0;compo<12;compo++))
do
	echo ${composite[$compo]}
	for pattern in $patterns_globe
	do		
		cp $rundir/$year/${composite[$compo]}/$product$year${composite[$compo]}.${pattern}*.hdf $out_dir
	done

	ficheiros=`ls *.hdf`

	for fiche in $ficheiros
	do
		echo $tilename
		tilename=`echo ${fiche} | cut -f3 -d'.'`
	
		python convert_MCD45A1.py ${fiche} $out_dir2$tilename.tif 

	done

	rm *.hdf

	cd $out_dir2


	#Africa
	python /home/wildube/anaconda2/bin/gdal_merge.py -o $out_dir2/GL/global_y${yearn}c${compo}.tif h16v05.tif h16v06.tif h16v07.tif h16v08.tif h17v05.tif h17v06.tif h17v07.tif h17v08.tif h18v05.tif h18v06.tif h18v07.tif h18v08.tif h19v05.tif h19v06.tif h19v07.tif h19v08.tif h19v09.tif h19v10.tif h19v11.tif h19v12.tif h20v05.tif h20v06.tif h20v07.tif h20v08.tif h20v09.tif h20v10.tif h20v11.tif h20v12.tif h21v06.tif h21v07.tif h21v08.tif h21v09.tif h21v10.tif h21v11.tif h22v07.tif h22v08.tif h22v09.tif h22v10.tif h22v11.tif h23v07.tif h23v08.tif h23v10.tif h23v11.tif h07v03.tif h07v06.tif h08v03.tif h08v04.tif h08v05.tif h08v06.tif h08v07.tif h09v02.tif h09v03.tif h09v04.tif h09v05.tif h09v06.tif h09v07.tif h10v02.tif h10v03.tif h10v04.tif h10v05.tif h10v06.tif h10v07.tif h11v02.tif h11v03.tif h11v04.tif h11v05.tif h11v06.tif h11v07.tif h12v01.tif h12v02.tif h12v03.tif h12v04.tif h12v05.tif h12v07.tif h13v01.tif h13v02.tif h13v03.tif h13v04.tif h14v01.tif h14v02.tif h14v03.tif h14v04.tif h15v01.tif h15v02.tif h15v05.tif h09v08.tif h09v09.tif h10v07.tif h10v08.tif h10v09.tif h10v10.tif h11v07.tif h11v08.tif h11v09.tif h11v10.tif h11v11.tif h11v12.tif h12v07.tif h12v08.tif h12v09.tif h12v10.tif h12v11.tif h12v12.tif h12v13.tif h13v08.tif h13v09.tif h13v10.tif h13v11.tif h13v12.tif h13v13.tif h13v14.tif h14v09.tif h14v10.tif h14v11.tif h14v14.tif h17v01.tif h17v02.tif h17v03.tif h17v04.tif h17v05.tif h17v06.tif h18v01.tif h18v02.tif h18v03.tif h18v04.tif h18v05.tif h19v01.tif h19v02.tif h19v03.tif h19v04.tif h19v05.tif h20v01.tif h20v02.tif h20v03.tif h20v04.tif h20v05.tif h21v01.tif h21v02.tif h21v03.tif h21v04.tif h21v05.tif h21v01.tif h21v02.tif h21v03.tif h21v04.tif h21v05.tif h21v06.tif h21v07.tif h22v01.tif h22v02.tif h22v03.tif h22v04.tif h22v05.tif h22v06.tif h22v07.tif h23v01.tif h23v02.tif h23v03.tif h23v04.tif h23v05.tif h23v06.tif h23v07.tif h23v08.tif h24v02.tif h24v03.tif h24v04.tif h24v05.tif h24v06.tif h24v07.tif h25v02.tif h25v03.tif h25v04.tif h25v05.tif h25v06.tif h25v07.tif h25v08.tif h26v02.tif h26v03.tif h26v04.tif h26v05.tif h26v06.tif h26v07.tif h26v08.tif h27v03.tif h27v04.tif h27v05.tif h27v06.tif h27v07.tif h27v08.tif h28v03.tif h28v04.tif h28v05.tif h28v06.tif h28v07.tif h28v08.tif h29v05.tif h29v06.tif h29v07.tif h29v08.tif h27v07.tif h27v08.tif h27v09.tif h27v12.tif h28v07.tif h28v08.tif h28v09.tif h28v11.tif h28v12.tif h28v13.tif h29v07.tif h29v08.tif h29v09.tif h29v10.tif h29v11.tif h29v12.tif h29v13.tif h30v07.tif h30v08.tif h30v09.tif h30v10.tif h30v11.tif h30v12.tif h30v13.tif h31v09.tif h31v10.tif h31v11.tif h31v12.tif h31v13.tif h32v09.tif h32v10.tif h32v12.tif h29v13.tif h30v13.tif h31v13.tif


	rm *.tif
	cd $out_dir2/GL
	gdalwarp -t_srs "+proj=longlat +datum=WGS84" -tr 0.005 0.005 -te -180.0 -90.0 180.0 90.0 -r near global_y${year}c${composite[$compo]}.tif global_y${year}c${mes[$compo]}_ll.tif

	python /home/wildube/BA_make/convert_RGMCD45.py global_y${year}c${mes[$compo]}_ll.tif 0 0.5
	python /home/wildube/BA_make/convert_RGMCD45.py global_y${year}c${mes[$compo]}_ll.tif 0 0.25
	python /home/wildube/BA_make/convert_RGMCD45.py global_y${year}c${mes[$compo]}_ll.tif 0 0.10
	python /home/wildube/BA_make/convert_RGMCD45.py global_y${year}c${mes[$compo]}_ll.tif 0 0.05
	gzip global_y${year}c${mes[$compo]}_ll.tif
	gzip global_y${year}c${composite[$compo]}.tif
	gzip global_y${year}c${mes[$compo]}_ll_025.tif
	gzip global_y${year}c${mes[$compo]}_ll_050.tif
	gzip global_y${year}c${mes[$compo]}_ll_010.tif
	gzip global_y${year}c${mes[$compo]}_ll_005.tif

	cd $out_dir


done


#cd $out_dir
