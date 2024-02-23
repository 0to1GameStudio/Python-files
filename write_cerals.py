import csv
import pandas as pd
#cerals = [
 #   ["Barley",556,1.7,32.9,10.1,13.8],
  #  ["Durum",339,5,27.4,4.09,9.7],
   # ["Fonio",240,1,4,1.7,0.05],
    #["Maize",442,7.4,37.45,6.15,11.03],
 #   ["Millet",484,2,37.9,13.4,9.15],
  #  ["Oats",231,9.2,35.1,10.3,3.73],
   # ["Rice (Brown)",346,2.8,38.1,9.9,0.8],
#    ["Rice, (White)",345,3.6,37.6,5.4,0.1],
 #   ["Rye",442,2,31.4,18.2,21.2],
  #  ["Sorghum",316,3,37.8,9.92,9.15],
   # ["Triticale",338,1.81,36.6,19,0.9],
    #["Wheat",407,1.2,27.8,12.9,13.8],
   # ]

#print(cerals)
#column_headings = ["Ceral","Calories","Fat","Protein","Fibre","Vitamin E"]
output_filename = 'my_cerals.csv'

#with open(output_filename,'w',encoding='utf-8',newline='') as output_file:
 #   writer = csv.writer(output_file,quoting=csv.QUOTE_NONNUMERIC)
  #  writer.writerow(column_headings)
   # writer.writerows(cerals)

#with open(output_filename,encoding='utf-8',newline='') as output_file:
 #   reader = csv.reader(output_file)
  #  for file in reader:
   #     print(file)


df = pd.read_csv(output_filename)
print(df)
