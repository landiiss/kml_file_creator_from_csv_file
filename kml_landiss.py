import simplekml
import csv

kml = simplekml.Kml()
t_end = 415
num = 1

while num < t_end:
    file = open("data.csv")
    csvreader = csv.reader(file)
    rows = []
    for row in csvreader:
        rows.append(row)

    latitude = rows[num][1]
    longitude = rows[num][2]
    
    kml.newpoint(name=f"{num}", coords=[(longitude, latitude)])
    file.close()
    num += 1

kml.save("./iss_location_landiss.kml")
