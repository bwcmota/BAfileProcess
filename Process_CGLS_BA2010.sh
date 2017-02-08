#!/bin/bash

#------------------------------------------------------------------------
# Program written to aggregate the continental C-GLS ba maps into coarser 
#  resolutions based on proportion of BA extent
# 
# Bernardo Mota (bwcmota@gmail.com)
# Date: 29 October 2015
#------------------------------------------------------------------------

rundir="/home/wildube/Datasets/Global_BA_datasets/CGLS/BA/"
rundir2="/home/wildube/Datasets/Global_BA_datasets/CGLS/PreProcessed/"

year=2010
yearn='2010'


janela="AFRI NOAM SOAM ASIA EURO OCEA"
composite="01 02 03 04 05 06 07 08 09 10 11 12"




out_dir="/home/wildube/teste"



for compo in $composite
do
	if [ "$compo" -eq "04" ] || [ "$compo" -eq "06" ] || [ "$compo" -eq "09" ] || [ "$compo" -eq "11" ]; then time="10 20 30"; fi
	if [ "$compo" -eq "01" ] || [ "$compo" -eq "03" ] || [ "$compo" -eq "05" ] || [ "$compo" -eq "07" ] || [ "$compo" -eq "08" ] || [ "$compo" -eq "10" ] || [ "$compo" -eq "12" ]; then time="10 20 31"; fi
	if [ "$compo" -eq "02" ]; then time="10 20 28"; fi
	if [ "$compo" -eq "02" ] && [ "$yearn" -eq "2000" ]; then time="10 20 29"; fi
	if [ "$compo" -eq "02" ] && [ "$yearn" -eq "2004" ]; then time="10 20 29"; fi
	if [ "$compo" -eq "02" ] && [ "$yearn" -eq "2008" ]; then time="10 20 29"; fi
	if [ "$compo" -eq "02" ] && [ "$yearn" -eq "2012" ]; then time="10 20 29"; fi

	echo $compo$time
	for cont in $janela
	do
		echo $cont	
		for step in $time
		do		
			cp $rundir/${yearn}/BA_${yearn}${compo}${step}0000_${cont}_VGT_V1.3/*.ZIP $out_dir

		done
	done

	cd $out_dir

	for f in *.ZIP; do unzip -o $f -d $out_dir; done

	continente="1 2 3 4 5 6"

	for k in $continente
	do 

		python Aggregate_CGLS.py $year $compo $k

	done
	for step in $time
	do		
		rm -R $year$compo$step
	done
	gzip *.tif
        mv *.tif.gz $rundir2
	rm *.ZIP


done



