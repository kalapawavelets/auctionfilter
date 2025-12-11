import pandas as pd
import tabula 
import xlsxwriter
from openpyxl import Workbook

file = "12_11_2025_current_cars.pdf"

tabula.convert_into(file, "converted_records_all.csv", output_format="csv", lattice=True, stream=False,  pages="all" )

df = pd.read_csv("converted_records_all.csv", on_bad_lines='skip')

df['Manual'] = 'No'
df['CVT'] = 'No'
df['Automatic'] = 'No'
df['average_value_if_sold'] = 0
df['sold_price_average'] = 0

#buy_proirity (1 - Must buy, 2 - Good, , 3 - Unknown, 4 - Do not buy)
df['buy_priority'] = 3

#TODO:This is to remove those x000D from the cells
# for str_col in df.select_dtypes(include=['object']).columns:
#     df[str_col] = df[str_col].astype(str).apply(openpyxl.utils.escape.unescape)


filtered_df_honda = df[(df['Make'] == 'HOND')]
filtered_df_toyota = df[(df['Make'] == 'TOYT')]
filtered_df_silverado = df[(df['Model'] == 'SLV')]
filtered_df_tesla = df[(df['Make'] == 'TESL')]
filtered_df_bmw = df[(df['Make'] == 'BMW')]
filtered_df_audi = df[(df['Make'] == 'AUDI')]
filtered_df_mercedes = df[(df['Make'] == 'MERZ')]
filtered_df_lexus = df[(df['Make'] == 'LEXS')]
filtered_df_acura = df[(df['Make'] == 'ACUR')]


#need to use with statement so files get closed when done writing
with pd.ExcelWriter('filtered_output.xlsx', engine='xlsxwriter') as writer:
		filtered_df_honda.to_excel(writer, sheet_name='Honda', index=False)
		filtered_df_toyota.to_excel(writer, sheet_name='Toyota', index=False)
		filtered_df_silverado.to_excel(writer, sheet_name='Silverado', index=False)
		filtered_df_tesla.to_excel(writer, sheet_name='Tesla', index=False)
		filtered_df_bmw.to_excel(writer, sheet_name='BMW', index=False)
		filtered_df_mercedes.to_excel(writer, sheet_name='Mercedes', index=False)
		filtered_df_lexus.to_excel(writer, sheet_name='Lexus', index=False)
		filtered_df_acura.to_excel(writer, sheet_name='Acura', index=False)
		filtered_df_audi.to_excel(writer, sheet_name='Audi', index=False)
		
#https://honda-tech.com/forums/vindecoder.php?vin=1HGCY2F57RA054098

#TODO: Get this working and inside the dataframe before tabs are made
#from vininfo import Vin

#print(f"Prius are {filtered_df_multi}")
#print(f"ALL Cars are {df}")

# for current_vin in df['VIN']:
# 	vin = Vin(current_vin)
# 	print(f"country is {vin.country}\n manufacturer {vin.manufacturer}\n")
# 	annotated = vin.annotate()
# 	details = vin.details

# 	checksum = Vin(current_vin).verify_checksum()
# 	print(f"***check sum for VIN {current_vin} is {checksum} annotated is {annotated}***")
