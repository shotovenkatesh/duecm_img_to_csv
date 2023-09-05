import csv
import os
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

#df: name and barcode csv
df = pd.read_csv("alms.csv",encoding= 'unicode_escape')

#df1: final template
df1 = pd.read_csv("alm.csv",encoding= 'unicode_escape')



# Specify the path to the desktop folder where your images are stored
desktop_folder = os.path.expanduser("/Users/venkatesh/Desktop/al maya")

img_names = []
data_dict = df.to_dict('records')
names = [str(item['Name']) for item in data_dict]
barcodes = [str(item['Barcode']) for item in data_dict]
images = df1['Image']
index = 0



for filename in os.listdir(desktop_folder):
    if filename.endswith((".jpg", ".jpeg", ".png", ".gif")):
        img_names.append(filename)
image_names_without_extension = [os.path.splitext(filename)[0] for filename in img_names]

# print(image_names)

d_names = df['Name'].astype(str)
d_barcodes = df['Barcode'].astype(str)






# print(my_series)

for i,barcode in enumerate(barcodes):
    warnings.filterwarnings("ignore")
    if barcodes[i] in image_names_without_extension:
        # print(barcodes[i])
        b_row_number = d_barcodes[d_barcodes == barcodes[i]].idxmax()
        images.loc[b_row_number] = barcodes[i]

        df1.at[b_row_number, 'Image'] = f"catalog/products/{barcodes[i]}.jpg"
        df1.to_csv('alm.csv', index=False)

        image_names_without_extension.remove(barcodes[i])
        print(f"{barcodes[i]} is added to the csv")
    elif names[i] in image_names_without_extension:
        n_row_number = d_names[d_names == names[i]].idxmax()
        images.loc[n_row_number] = names[i]

        df1.at[n_row_number, 'Image'] = f"catalog/products/{names[i]}.jpg"
        df1.to_csv('alm.csv', index=False)

        image_names_without_extension.remove(names[i])
        print(f"{names[i]} is added to the csv")








