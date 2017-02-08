

import os

#------------------------------------------------------------------------
# Program written to check the consistency of the C-GLS BA files
# 
# Bernardo Mota (bwcmota@gmail.com)
# Date: 29 October 2015
#------------------------------------------------------------------------

data_path="/home/wildube/Datasets/Global_BA_datasets/CGLS/BA/"

continents=['AFRI', 'ASIA', 'EURO', 'NOAM', 'OCEA', 'SOAM']
month=['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] 


for conti in range(0, 6):

	for year in range(2009, 2012):


		for mth in range(0, 12):
			for step in range(0, 3):


				mes=month[mth]
				compo=['10', '20', '31'] 
				if mes=='02':
					if (year==2000) or (year==2004) or (year==2008) or (year==2012) or (year==2016):
						compo=['10', '20', '29'] 
					else:
						compo=['10', '20', '28'] 
				if (mes=='04') or (mes=='06') or (mes=='04') or (mes=='06') or (mes=='09') or (mes=='11'):
					compo=['10', '20', '30'] 
				directory_name=str('/BA_')+str(year)+str(mes)+str(compo[step])+str('0000_')+str(continents[conti])+str('_VGT_V1.3')




				#check_path=str(server_path)+str(data_path)+str(directory_name)
				check_path=str(data_path)+str(year)+str(directory_name)


				valor=os.path.exists(check_path)

				if valor==False:
					#print('Missing: '+str(mes)+str(', ')+str(compo[step]))
					print(valor, check_path)
