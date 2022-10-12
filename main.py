import pandas as pd
data = pd.read_csv('AGCOM_BBmap_opendata_comuni_csv.csv',encoding='utf-8',delimiter=';')

datanew = data[['COMUNE','REGIONE','P1','SPEED_DOWN_ADSL_AVG']]

datanew['AvgSpeedProCapite'] = datanew['SPEED_DOWN_ADSL_AVG'] / datanew['P1']
print(datanew['AvgSpeedProCapite'])