import csv
import pandas as pd

def add_crop(crop_name, humidity_times, humidity_vals, light_times, light_vals, temperature_times, temperature_vals):
    add_crop_helper(crop_name, "humidity", humidity_times, humidity_vals)
    add_crop_helper(crop_name, "light", light_times, light_vals)
    add_crop_helper(crop_name, "temperature", temperature_times, temperature_vals)

def add_crop_helper(crop_name, aspect_name, aspect_times, aspect_vals):
    aspect_df = pd.read_csv(f"./data/{aspect_name}.csv")

    aspect_start_times = [aspect_times[i] for i in range(0,len(aspect_times),2)]
    aspect_end_times = [aspect_times[i] for i in range(1,len(aspect_times),2)]

    insert_df = pd.DataFrame({"crop_name": [crop_name for i in aspect_vals],
                            "start_time": aspect_start_times,
                            "end_time": aspect_end_times,
                            aspect_name: aspect_vals})

    new_df = pd.concat([aspect_df, insert_df]).reset_index(drop=True)
    new_df.to_csv(f"./data/{aspect_name}.csv", index=False)

def edit_crop(crop_name, humidity_times, humidity_vals, light_times, light_vals, temperature_times, temperature_vals):
    create_new_csv(crop_name, "humidity", humidity_times, humidity_vals)
    create_new_csv(crop_name, "light", light_times, light_vals)
    create_new_csv(crop_name, "temperature", temperature_times, temperature_vals)

def create_new_csv(crop_name, aspect_name, aspect_times, aspect_vals):
    aspect_df = pd.read_csv(f"./data/{aspect_name}.csv")
    
    aspect_inds = aspect_df.index[aspect_df["crop_name"] == crop_name].tolist()
    aspect_begin = aspect_inds[0]
    aspect_end = aspect_inds[-1]

    aspect_start_times = [aspect_times[i] for i in range(0,len(aspect_times),2)]
    aspect_end_times = [aspect_times[i] for i in range(1,len(aspect_times),2)]

    insert_df = pd.DataFrame({"crop_name": [crop_name for i in aspect_vals],
                            "start_time": aspect_start_times,
                            "end_time": aspect_end_times,
                            aspect_name: aspect_vals})
    
    new_df = pd.concat([aspect_df.iloc[:aspect_begin], insert_df, aspect_df[aspect_end+1:]]).reset_index(drop=True)
    new_df.to_csv(f"./data/{aspect_name}.csv", index=False)
     

def process_crop_info():
    crop_names=[]
    crop_img_paths=[]
    humidity_times=[]
    humidity_vals=[]
    light_times=[]
    light_vals=[]
    temperature_times=[]
    temperature_vals=[]

    with open("./data/humidity.csv", 'r', newline='') as humidity_data, \
        open("./data/light.csv", 'r', newline='') as light_data, \
        open("./data/temperature.csv", 'r', newline='') as temperature_data:
        humidity_reader = csv.reader(humidity_data, delimiter=',')
        light_reader = csv.reader(light_data, delimiter=',')
        temperature_reader = csv.reader(temperature_data, delimiter=',')

        next(humidity_reader)
        next(light_reader)
        next(temperature_reader)

        for i, row in enumerate(humidity_reader):
            crop_name_i = row[0]
            start_time_i = row[1]
            end_time_i = row[2]
            val_i = row[3]
            if crop_name_i not in crop_names:
                    crop_names.append(crop_name_i)
                    crop_img_paths.append(f"../static/imgs/{crop_name_i}.png")
                    humidity_times.append([])
                    humidity_vals.append([])
                    light_times.append([])
                    light_vals.append([])
                    temperature_times.append([])
                    temperature_vals.append([])
            crop_ind = crop_names.index(crop_name_i)
            humidity_times[crop_ind].append(start_time_i)
            humidity_times[crop_ind].append(end_time_i)
            humidity_vals[crop_ind].append(val_i)
        
        for i, row in enumerate(light_reader):
            crop_name_i = row[0]
            start_time_i = row[1]
            end_time_i = row[2]
            val_i = row[3]
            crop_ind = crop_names.index(crop_name_i)
            light_times[crop_ind].append(start_time_i)
            light_times[crop_ind].append(end_time_i)
            light_vals[crop_ind].append(val_i)
        
        for i, row in enumerate(temperature_reader):
            crop_name_i = row[0]
            start_time_i = row[1]
            end_time_i = row[2]
            val_i = row[3]
            crop_ind = crop_names.index(crop_name_i)
            temperature_times[crop_ind].append(start_time_i)
            temperature_times[crop_ind].append(end_time_i)
            temperature_vals[crop_ind].append(val_i)
    
    return crop_names, crop_img_paths, humidity_times,humidity_vals,\
        light_times,light_vals,temperature_times,temperature_vals