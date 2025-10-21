import pandas as pd
import tabula 
import xlsxwriter

file = "10_20_2025_336PM.pdf"

tabula.convert_into(file, "converted_records_all.csv", output_format="csv", lattice=True, stream=False,  pages="all" )

df = pd.read_csv("converted_records_all.csv")

filtered_df_honda = df[(df['Make'] == 'HOND')]
filtered_df_toyota = df[(df['Make'] == 'TOYT')]
filtered_df_silverado = df[(df['Model'] == 'SLV')]
filtered_df_tesla = df[(df['Make'] == 'TESL')]
filtered_df_bmw = df[(df['Make'] == 'BMW')]
filtered_df_mercedes = df[(df['Make'] == 'MERZ')]
filtered_df_lexus = df[(df['Make'] == 'LEXS')]

#need to use with statement so files get closed when done writing
with pd.ExcelWriter('filtered_output.xlsx', engine='xlsxwriter') as writer:
		filtered_df_honda.to_excel(writer, sheet_name='Honda', index=False)
		filtered_df_toyota.to_excel(writer, sheet_name='Toyota', index=False)
		filtered_df_silverado.to_excel(writer, sheet_name='Silverado', index=False)
		filtered_df_tesla.to_excel(writer, sheet_name='Tesla', index=False)
		filtered_df_bmw.to_excel(writer, sheet_name='BMW', index=False)
		filtered_df_mercedes.to_excel(writer, sheet_name='Mercedes', index=False)
		filtered_df_lexus.to_excel(writer, sheet_name='Lexus', index=False)
		

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
