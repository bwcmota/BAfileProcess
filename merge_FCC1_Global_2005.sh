#------------------------------------------------------------------------
# Program written to aggregate the continental Fire CCI maps into coarser 
#  resolutions based on proportion of BA extent
# 
# Bernardo Mota (bwcmota@gmail.com)
# Date: 29 October 2015
#------------------------------------------------------------------------


dir_data='/home/wildube/storage/space2/storage/products/Fire/Burnt_Area/FireCCI/Original/V4.1'
out_dir="/home/wildube/storage/space2/storage/products/Fire/Burnt_Area/FireCCI/Agregated/V4.1"

year="2005"

mes="01 02 03 04 05 06 07 08 09 10 11 12"



for compo in $mes
do
	gdalwarp -t_srs "+proj=longlat +datum=WGS84" -tr 0.0025 0.0025 -te -180.0 19.0 -50.0 83.0 -r near $dir_data/${year}/${year}${compo}01-ESACCI-L3S_FIRE-BA-MERIS-AREA_1-fv04.1/${year}${compo}01-ESACCI-L3S_FIRE-BA-MERIS-AREA_1-fv04.1.tif $dir_data/NA_y${year}c${compo}_ll.tif
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/NA_y${year}c${compo}_ll.tif $dir_data/NA_y${year}c${compo}_ll_005.tif 1 0.05
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/NA_y${year}c${compo}_ll.tif $dir_data/NA_y${year}c${compo}_ll_010.tif 1 0.1
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/NA_y${year}c${compo}_ll.tif $dir_data/NA_y${year}c${compo}_ll_025.tif 1 0.25
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/NA_y${year}c${compo}_ll.tif $dir_data/NA_y${year}c${compo}_ll_050.tif 1 0.5

	gdalwarp -t_srs "+proj=longlat +datum=WGS84" -tr 0.0025 0.0025 -te -105.0 -57.0 -34.0 19.0 -r near $dir_data/${year}/${year}${compo}01-ESACCI-L3S_FIRE-BA-MERIS-AREA_2-fv04.1/${year}${compo}01-ESACCI-L3S_FIRE-BA-MERIS-AREA_2-fv04.1.tif $dir_data/SA_y${year}c${compo}_ll.tif
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/SA_y${year}c${compo}_ll.tif $dir_data/SA_y${year}c${compo}_ll_005.tif 2 0.05
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/SA_y${year}c${compo}_ll.tif $dir_data/SA_y${year}c${compo}_ll_010.tif 2 0.1
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/SA_y${year}c${compo}_ll.tif $dir_data/SA_y${year}c${compo}_ll_025.tif 2 0.25
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/SA_y${year}c${compo}_ll.tif $dir_data/SA_y${year}c${compo}_ll_050.tif 2 0.5


	gdalwarp -t_srs "+proj=longlat +datum=WGS84" -tr 0.0025 0.0025 -te -26.0 25.0 53.0 83.0 -r near $dir_data/${year}/${year}${compo}01-ESACCI-L3S_FIRE-BA-MERIS-AREA_3-fv04.1/${year}${compo}01-ESACCI-L3S_FIRE-BA-MERIS-AREA_3-fv04.1.tif $dir_data/EU_y${year}c${compo}_ll.tif
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/EU_y${year}c${compo}_ll.tif $dir_data/EU_y${year}c${compo}_ll_005.tif 3 0.05
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/EU_y${year}c${compo}_ll.tif $dir_data/EU_y${year}c${compo}_ll_010.tif 3 0.1
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/EU_y${year}c${compo}_ll.tif $dir_data/EU_y${year}c${compo}_ll_025.tif 3 0.25
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/EU_y${year}c${compo}_ll.tif $dir_data/EU_y${year}c${compo}_ll_050.tif 3 0.5


	gdalwarp -t_srs "+proj=longlat +datum=WGS84" -tr 0.0025 0.0025 -te 53.0 0.0 180.0 83.0 -r near $dir_data/${year}/${year}${compo}01-ESACCI-L3S_FIRE-BA-MERIS-AREA_4-fv04.1/${year}${compo}01-ESACCI-L3S_FIRE-BA-MERIS-AREA_4-fv04.1.tif $dir_data/AS_y${year}c${compo}_ll.tif
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/AS_y${year}c${compo}_ll.tif $dir_data/AS_y${year}c${compo}_ll_005.tif 4 0.05
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/AS_y${year}c${compo}_ll.tif $dir_data/AS_y${year}c${compo}_ll_010.tif 4 0.1
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/AS_y${year}c${compo}_ll.tif $dir_data/AS_y${year}c${compo}_ll_025.tif 4 0.25
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/AS_y${year}c${compo}_ll.tif $dir_data/AS_y${year}c${compo}_ll_050.tif 4 0.5


	gdalwarp -t_srs "+proj=longlat +datum=WGS84" -tr 0.0025 0.0025 -te -26.0 -40.0 53.0 25.0 -r near $dir_data/${year}/${year}${compo}01-ESACCI-L3S_FIRE-BA-MERIS-AREA_5-fv04.1/${year}${compo}01-ESACCI-L3S_FIRE-BA-MERIS-AREA_5-fv04.1.tif $dir_data/AF_y${year}c${compo}_ll.tif
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/AF_y${year}c${compo}_ll.tif $dir_data/AF_y${year}c${compo}_ll_005.tif 5 0.05
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/AF_y${year}c${compo}_ll.tif $dir_data/AF_y${year}c${compo}_ll_010.tif 5 0.1
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/AF_y${year}c${compo}_ll.tif $dir_data/AF_y${year}c${compo}_ll_025.tif 5 0.25
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/AF_y${year}c${compo}_ll.tif $dir_data/AF_y${year}c${compo}_ll_050.tif 5 0.5


	gdalwarp -t_srs "+proj=longlat +datum=WGS84" -tr 0.0025 0.0025 -te 95.0 -53.0 180.0 0.0 -r near $dir_data/${year}/${year}${compo}01-ESACCI-L3S_FIRE-BA-MERIS-AREA_6-fv04.1/${year}${compo}01-ESACCI-L3S_FIRE-BA-MERIS-AREA_6-fv04.1.tif $dir_data/OC_y${year}c${compo}_ll.tif
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/OC_y${year}c${compo}_ll.tif $dir_data/OC_y${year}c${compo}_ll_005.tif 6 0.05
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/OC_y${year}c${compo}_ll.tif $dir_data/OC_y${year}c${compo}_ll_010.tif 6 0.1
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/OC_y${year}c${compo}_ll.tif $dir_data/OC_y${year}c${compo}_ll_025.tif 6 0.25
	python /home/wildube/BA_make/convert_RGFCCI_v41.py $dir_data/OC_y${year}c${compo}_ll.tif $dir_data/OC_y${year}c${compo}_ll_050.tif 6 0.5

	gzip $dir_data/NA_y${year}c${compo}_ll.tif
	gzip $dir_data/SA_y${year}c${compo}_ll.tif
	gzip $dir_data/EU_y${year}c${compo}_ll.tif
	gzip $dir_data/AS_y${year}c${compo}_ll.tif
	gzip $dir_data/AF_y${year}c${compo}_ll.tif
	gzip $dir_data/OC_y${year}c${compo}_ll.tif

	python /home/wildube/anaconda2/bin/gdal_merge.py -o $out_dir/${year}/global_y${year}c${compo}_ll_005.tif -ul_lr -180.0 90.0 180.0 -90.0 $dir_data/NA_y${year}c${compo}_ll_005.tif $dir_data/SA_y${year}c${compo}_ll_005.tif $dir_data/EU_y${year}c${compo}_ll_005.tif $dir_data/AS_y${year}c${compo}_ll_005.tif $dir_data/AF_y${year}c${compo}_ll_005.tif $dir_data/OC_y${year}c${compo}_ll_005.tif
	python /home/wildube/anaconda2/bin/gdal_merge.py -o $out_dir/${year}/global_y${year}c${compo}_ll_010.tif -ul_lr -180.0 90.0 180.0 -90.0 $dir_data/NA_y${year}c${compo}_ll_010.tif $dir_data/SA_y${year}c${compo}_ll_010.tif $dir_data/EU_y${year}c${compo}_ll_010.tif $dir_data/AS_y${year}c${compo}_ll_010.tif $dir_data/AF_y${year}c${compo}_ll_010.tif $dir_data/OC_y${year}c${compo}_ll_010.tif
	python /home/wildube/anaconda2/bin/gdal_merge.py -o $out_dir/${year}/global_y${year}c${compo}_ll_025.tif -ul_lr -180.0 90.0 180.0 -90.0 $dir_data/NA_y${year}c${compo}_ll_025.tif $dir_data/SA_y${year}c${compo}_ll_025.tif $dir_data/EU_y${year}c${compo}_ll_025.tif $dir_data/AS_y${year}c${compo}_ll_025.tif $dir_data/AF_y${year}c${compo}_ll_025.tif $dir_data/OC_y${year}c${compo}_ll_025.tif
	python /home/wildube/anaconda2/bin/gdal_merge.py -o $out_dir/${year}/global_y${year}c${compo}_ll_050.tif -ul_lr -180.0 90.0 180.0 -90.0 $dir_data/NA_y${year}c${compo}_ll_050.tif $dir_data/SA_y${year}c${compo}_ll_050.tif $dir_data/EU_y${year}c${compo}_ll_050.tif $dir_data/AS_y${year}c${compo}_ll_050.tif $dir_data/AF_y${year}c${compo}_ll_050.tif $dir_data/OC_y${year}c${compo}_ll_050.tif

	gzip $dir_data/NA_y${year}c${compo}_ll_005.tif
	gzip $dir_data/SA_y${year}c${compo}_ll_005.tif
	gzip $dir_data/EU_y${year}c${compo}_ll_005.tif
	gzip $dir_data/AS_y${year}c${compo}_ll_005.tif
	gzip $dir_data/AF_y${year}c${compo}_ll_005.tif
	gzip $dir_data/OC_y${year}c${compo}_ll_005.tif

	gzip $dir_data/NA_y${year}c${compo}_ll_010.tif
	gzip $dir_data/SA_y${year}c${compo}_ll_010.tif
	gzip $dir_data/EU_y${year}c${compo}_ll_010.tif
	gzip $dir_data/AS_y${year}c${compo}_ll_010.tif
	gzip $dir_data/AF_y${year}c${compo}_ll_010.tif
	gzip $dir_data/OC_y${year}c${compo}_ll_010.tif

	gzip $dir_data/NA_y${year}c${compo}_ll_025.tif
	gzip $dir_data/SA_y${year}c${compo}_ll_025.tif
	gzip $dir_data/EU_y${year}c${compo}_ll_025.tif
	gzip $dir_data/AS_y${year}c${compo}_ll_025.tif
	gzip $dir_data/AF_y${year}c${compo}_ll_025.tif
	gzip $dir_data/OC_y${year}c${compo}_ll_025.tif

	gzip $dir_data/NA_y${year}c${compo}_ll_050.tif
	gzip $dir_data/SA_y${year}c${compo}_ll_050.tif
	gzip $dir_data/EU_y${year}c${compo}_ll_050.tif
	gzip $dir_data/AS_y${year}c${compo}_ll_050.tif
	gzip $dir_data/AF_y${year}c${compo}_ll_050.tif
	gzip $dir_data/OC_y${year}c${compo}_ll_050.tif


done

