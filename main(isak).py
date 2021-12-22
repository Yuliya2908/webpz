import numpy as np
from PIL import Image



data = open("MTL.txt", "r").readlines()

dotc = {"UL":[0.0, 0.0],
        "UR":[0.0, 0.0],
        "LL":[0.0, 0.0],
        "LR":[0.0, 0.0]}

for line in data:
  microdata = line.split()
  if microdata[0] == "CORNER_UL_LAT_PRODUCT":
      dotc["UL"][0] = float(microdata[2])
  if microdata[0] == "CORNER_UL_LON_PRODUCT":
      dotc["UL"][1] = float(microdata[2])
  if microdata[0] == "CORNER_UR_LAT_PRODUCT":
      dotc["UR"][0] = float(microdata[2])
  if microdata[0] == "CORNER_UR_LON_PRODUCT":
      dotc["UR"][1] = float(microdata[2])
  if microdata[0] == "CORNER_LL_LAT_PRODUCT":
      dotc["LL"][0] = float(microdata[2])
  if microdata[0] == "CORNER_LL_LON_PRODUCT":
      dotc["LL"][1] = float(microdata[2])
  if microdata[0] == "CORNER_LR_LAT_PRODUCT":
      dotc["LR"][0] = float(microdata[2])
  if microdata[0] == "CORNER_LR_LON_PRODUCT":
      dotc["LR"][1] = float(microdata[2])

print (f"UL: {dotc['UL']}")
print (f"UR: {dotc['UR']}")
print (f"LL: {dotc['LL']}")
print (f"LR: {dotc['LR']}")


delta_y = abs(dotc['UL'][0]-dotc['LR'][0])
delta_x = abs(dotc['UR'][1]-dotc['LL'][1])

print(f"delta_y = {delta_y}")
print(f"delta_x = {delta_x}")

image = Image.open("B2.TIF")
pix_len,pix_lat = image.size
print(f"Image size {pix_len}x{pix_lat}")

d_lat = delta_y/pix_lat
d_len = delta_x/pix_len
print(f"d_lat = {d_lat}")
print(f"d_len = {d_len}")

y = 45.0322
x = 38.9765
lat_y = int(abs(dotc['UL'][0] - y)/d_lat)
len_x = int(abs(dotc['LL'][1] - x)/d_len)

result = image.crop(((len_x-800), (lat_y-800), (len_x+800), (lat_y+800)))
result.save("result.png")


image_red = Image.open("B3.TIF")
image_infred = Image.open("B4.TIF")
result1 = image_red.crop(((len_x-800), (lat_y-800), (len_x+800), (lat_y+800)))
#result1.save("result_red.png")
result2 = image_infred.crop(((len_x-800), (lat_y-800), (len_x+800), (lat_y+800)))
#result2.save("result_infred.png")

matr_red = np.array(result1)
matr_infred = np.array(result2)

matr_ndvi = (matr_infred - matr_red)/(matr_infred + matr_red)

ndvi = Image.new('RGB', result1.size, color=(255,255,255))

cnt = 0
for i in matr_ndvi:
    for j in range(len(i)):
        if i[j] >= 0.9:
            ndvi.putpixel((j,cnt), (4,18,14))
        elif i[j] >= 0.8:
            ndvi.putpixel((j,cnt), (4,38,4))
        elif i[j] >= 0.7:
            ndvi.putpixel((j,cnt), (4,54,4))
        elif i[j] >= 0.6:
            ndvi.putpixel((j,cnt), (4,66,4))
        elif i[j] >= 0.5:
            ndvi.putpixel((j,cnt), (4,94,4))
        elif i[j] >= 0.4:
            ndvi.putpixel((j,cnt), (28,114,4))
        elif i[j] >= 0.3:
            ndvi.putpixel((j,cnt), (100,162,4))
        elif i[j] >= 0.2:
            ndvi.putpixel((j,cnt), (142,182,20))
        elif i[j] >= 0.166:
            ndvi.putpixel((j,cnt), (132,138,52))
        elif i[j] >= 0.1:
            ndvi.putpixel((j,cnt), (164,130,76))
        elif i[j] >= 0.66:
            ndvi.putpixel((j, cnt), (180,150,108))
        elif i[j] >= 0:
            ndvi.putpixel((j, cnt), (252,254,252))
        elif i[j] >= -1:
            ndvi.putpixel((j, cnt), (4,18,60))
    cnt += 1

ndvi.save("ndvi.png")
