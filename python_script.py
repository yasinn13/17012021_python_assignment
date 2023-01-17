#Seattle station code: GHCND:US1WAKG0038
import json 
with open('precipitation.json', encoding='utf-8') as file:
    precipitation_data = json.load(file) 

#Select only Seattle data
seattle_precipitation_data = []
for measurement in precipitation_data:
    station_code = measurement['station']
    if station_code == 'GHCND:US1WAKG0038':
        seattle_precipitation_data.append(measurement)
#Create json file (not necessary, for easier overview of data)
with open('seattle_precipitation_data.json', 'w', encoding='utf-8') as file:
    json.dump(seattle_precipitation_data, file, indent=4) 

#Calculate list of total monthly precipitation
total_monthly_precipitation = [0]*12
for measurement in seattle_precipitation_data:
    date = measurement['date']
    split_date = date.split('-') 
    month = int(split_date[1])
    total_monthly_precipitation[month-1] += measurement['value']

#Create results file
results = {
    "Seattle":{
        "station": "GHCND:US1WAKG0038",
        "state": "WA",
        "total_monthly_precipitation": total_monthly_precipitation,
        "total_yearly_precipitation": [],
        "relative_monthly_precipitation": [],
        "relative_yearly_precipitation": [] }

}

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, indent=4) 

#Calculate yearly precipitation
total_yearly_precipitation = 0
for measurement in seattle_precipitation_data:
    total_yearly_precipitation += measurement['value']

#Calculate relative monthly precipitation
relative_monthly_precipitation = []
for month in total_monthly_precipitation:
    relative_monthly_precipitation.append(month/total_yearly_precipitation)

#Create results file
results = {
    "Seattle":{
        "station": "GHCND:US1WAKG0038",
        "state": "WA",
        "total_monthly_precipitation": total_monthly_precipitation,
        "total_yearly_precipitation": total_yearly_precipitation,
        "relative_monthly_precipitation": relative_monthly_precipitation,
        "relative_yearly_precipitation": 0 }

}

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, indent=4) 

#Read codes from CSV file
from csv import DictReader
with open ('stations.csv') as file:
    reader = DictReader(file)
    stations_list = list(reader)

results = []
for station in stations_list:
    #Get variables from csv file 
    location = station['Location']
    state = station['State']
    station_id = station['Station']

    total_monthly_precipitation = [0]*12
    
    for measurement in precipitation_data:
        #Get the station's data
        station_code = measurement['station']
        if station_code == station_id:
         #Calculate total monthly precipitation
            date = measurement['date']
            split_date = date.split('-') 
            month = int(split_date[1])
            total_monthly_precipitation[month-1] += measurement['value']
        #Calculate yearly total
            total_yearly_precipitation += measurement['value']
            
    partial_results = {
        location:{
            "station": station_id,
            "state": state,
            "total_monthly_precipitation": total_monthly_precipitation,
            "total_yearly_precipitation": total_yearly_precipitation,
            "relative_monthly_precipitation": [],
            "relative_yearly_precipitation": [] }}
    results.append(partial_results)
    
with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, indent=4) 




