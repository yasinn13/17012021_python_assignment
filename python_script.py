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
        "total_monthly_precipitation": total_monthly_precipitation   }

}

with open('results.json', 'w', encoding='utf-8') as file:
    json.dump(results, file, indent=4) 