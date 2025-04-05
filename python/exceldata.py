import pandas as pd
writer=pd.ExcelWriter('excelfile.xlsx',engine="openpyxl",mode='w')
empty_dataframe=pd.DataFrame()
empty_dataframe.to_excel(writer,sheet_name='empty')
writer.close()
data=[["Aditya",179],
      ['Sameer',181],
      ['Dharwish',170],
      ["Joel",167]]
column_names=["Name","Height"]
df=pd.DataFrame(data,columns=column_names)
writer=pd.ExcelWriter('excel_with_list.xlsx',engine='openpyxl')
df.to_excel(writer,sheet_name='first_sheet',index=0,startrow=3,startcol=4)
writer.close()
#index=False=>removes the extra unnamed column with index counts.
#Shifting rows :. startrow=> starts from the nth row. indexing starts from 0.
#shifting columns:. startcol=> takes the column number after which the data should be written
data=[{"Name":"Aditya","Height":179},
      {"Name":'Sameer',"Height":181},
      {"Name":'Dharwish',"Height":170},
      {"Name":"Joel","Height":167}]
pd.DataFrame(data)
writer=pd.ExcelWriter('excel_with_dict.xlsx',engine='openpyxl')
df.to_excel(writer,sheet_name='first_sheet',index=False)
writer.close()
df=pd.read_csv("output_2.csv")
writer=pd.ExcelWriter('excel_from_csv.xlsx',engine='openpyxl')
df.to_excel(writer, sheet_name='first_sheet',index=False)
writer.close()
height_data=[{"Name":"Aditya","Height":179},
      {"Name":"Sameer","Height":181},
      {"Name":"Dharwish","Height":170},
      {"Name":"Joel","Height":167}]

weight_data=[{"Name":"Aditya","Weight":76},
      {"Name":"Sameer","Weight":68},
      {"Name":"Dharwish","Weight":69},
      {"Name":"Joel", "Weight":73}]

marks_data=[{"Name":"Aditya","Marks":79},
      {"Name":"Sameer","Marks":81},
      {"Name":"Dharwish","Marks":70},
      {"Name":"Joel","Marks":67}]
height_df=pd.DataFrame(height_data)
weight_df=pd.DataFrame(weight_data)
marks_df=pd.DataFrame(marks_data)
writer=pd.ExcelWriter('excel_with_multiple_sheets.xlsx',engine='openpyxl')
height_df.to_excel(writer,sheet_name='height',index=False)
weight_df.to_excel(writer,sheet_name='weight',index=False)
marks_df.to_excel(writer,sheet_name='marks',index=False)
writer.close()
df=pd.read_excel('excel_with_dict.xlsx')
print("The dataframe is:")
print(df)
#sheet_name parameter in read_excel() allows us to read files with multiple sheets
#ExcelFile() takes the file name of the spreadsheet as its input argument and returns an ExcelFile object.
