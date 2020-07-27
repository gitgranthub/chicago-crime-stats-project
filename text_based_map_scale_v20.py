import bpy
import csv
import numpy as np

# **make sure to set csv file path**
with open('/Users/datascience/Documents/DataScience/Blender/projects/crime_wellbeing/comm_health_crime_sml.csv') as csv_file:
    readout = csv.reader(csv_file)
    
    next(readout, None)
    

    col_values = []
    #counter = 0
    
    for row in readout:
        #***************************^CHANGE_CSV_ROW!
        current_row_val = float(row[5])
        col_values.append(current_row_val)
        #counter = counter + 1
        current_value = row[:]
        print(current_row_val)
        
    obj_counter = -1
    for active in bpy.context.selected_objects:
        obj_counter = obj_counter + 1
        bpy.context.view_layer.objects.active = active 
        
        # **Change the multiple divide value below, so the bars look better!
        
        if max(col_values) < 101.0:
            
            # **FOR DATA BETWEEN 0-50 - sample Homicides - INDEX 5
            bpy.context.object.scale[2] = (col_values[obj_counter] / 8) * 3
            
        elif max(col_values) < 99999.0:
        
            # **FOR DATA BETWEEN 1000-100000 - sample 'Per Capita Income' INDEX 2!!!!!
            bpy.context.object.scale[2] = (col_values[obj_counter] / 7000) * 3
