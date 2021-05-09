#!/usr/bin/env python
# coding: utf-8

# In[7]:


user_input = arcpy.GetParameterAsText(0)   

# modules (environ = arcgispro -py3)
import arcpy
import os
arcpy.CheckOutExtension('spatial')
from arcpy import env
from arcpy.sa import *
import csv
import numpy as np

#data
filename = os.path.split(user_input)[1]
filename = filename.replace(".gpx", "")

template = r'C:\Users\A02315404\Documents\python\frolic_analysis\data\ecoregionsL4.shp'

#folders
conv_data_folder = r'C:\Users\A02315404\Documents\python\frolic_analysis\data_converted'
data_folder = r'C:\Users\A02315404\Documents\python\frolic_analysis\data'
data_orig_folder = r'C:\Users\A02315404\Documents\python\frolic_analysis\data_orig'
int_folder = r'C:\Users\A02315404\Documents\python\frolic_analysis\intersections'
in_folder = r'C:\Users\A02315404\Documents\python\frolic_analysis\data_gpx_files'
out_folder = r'C:\Users\A02315404\Documents\python\frolic_analysis\data_converted'
frolic_folder = r'C:\Users\A02315404\Documents\python\frolic_analysis'

arcpy.env.workspace = data_folder

#shape/image data
rock = os.path.join(data_orig_folder, "rock.tif")
nlcd = os.path.join(data_orig_folder, "nlcd.tif")
nlcd_key = os.path.join(data_orig_folder, "nlcd_key.csv")
rock_key = os.path.join(data_orig_folder, "rock_key.csv")
eco3 = os.path.join(data_orig_folder, "ecoregionsL3.shp")
eco4 = os.path.join(data_orig_folder, "ecoregionsL4.shp")


#trail (from user input)
trail =  os.path.join(conv_data_folder, filename) + ".shp"
output_name_shp = os.path.join(out_folder, filename)+ ".shp"
output_name_tif = os.path.join(out_folder, filename)+ ".tif"
out_name_nlcd=os.path.join(int_folder, filename) + "_nlcd.tif"
out_name_rock=os.path.join(int_folder, filename) + "_rock.tif"
temp_fn = os.path.join(frolic_folder, filename) + '_test_maps.pdf'
pdf_fn = os.path.join(frolic_folder, filename) + '_maps.pdf'


## Converting user_input (.gpx) to .tif and  .shp files

#print(filename,"\n", output_name_shp, "\n", output_name_tif)
arcpy.GPXtoFeatures_conversion(user_input, output_name_shp)
arcpy.conversion.PointToRaster(in_features=output_name_shp, 
                               value_field='FID', 
                               out_rasterdataset=output_name_tif)


## Make maps

# Get the current project.
project = arcpy.mp.ArcGISProject("C:/Users/A02315404/Documents/python/frolic_analysis/frolic_map1.aprx")
[m.name for m in project.listMaps()]
# Get the currently active map.
mapp = project.listMaps('utah')[0]
print(mapp.name)
print(filename)
# Get the  layers.
eco3 = mapp.listLayers('eco3_crop')[0]
eco4 = mapp.listLayers('eco4_crop')[0]
rock = mapp.listLayers('rock_crop.tif')[0]
nlcd = mapp.listLayers('nlcd_crop.tif')[0]
lyr_list = [eco3,eco4,rock,nlcd]
lyr_names = ["Ecoregion Classificaiton III","Ecoregion Classificaiton IV","Type of Lithology" , "Landcover"]
mapp.addDataFromPath(trail)
trail_lyr = mapp.listLayers(filename)[0]
mapp = project.listMaps('utah')[0]
layout = project.listLayouts('current_layout')[0]
final_doc = arcpy.mp.PDFDocumentCreate(pdf_fn)


## Making and saving pdf of maps

cur_lyr= lyr_list[0]
print(cur_lyr.name)

for lyr in lyr_list:
    lyr.visible = False

cur_lyr.visible = True
trail_lyr.visible = True

layout.exportToPDF(temp_fn)
final_doc.appendPages(temp_fn)


cur_lyr= lyr_list[1]
print(cur_lyr.name)

for lyr in lyr_list:
    lyr.visible = False

cur_lyr.visible = True
trail_lyr.visible = True
layout.exportToPDF(temp_fn)
final_doc.appendPages(temp_fn)

cur_lyr= lyr_list[2]
print(cur_lyr.name)

for lyr in lyr_list:
    lyr.visible = False

cur_lyr.visible = True
trail_lyr.visible = True
layout.exportToPDF(temp_fn)
final_doc.appendPages(temp_fn)

cur_lyr= lyr_list[3]
print(cur_lyr.name)

for lyr in lyr_list:
    lyr.visible = False

cur_lyr.visible = True
trail_lyr.visible = True

layout.exportToPDF(temp_fn)
final_doc.appendPages(temp_fn)

# Save and close the final pdf.
final_doc.saveAndClose()

# Delete variables to make sure everything is closed.
del final_doc, project

