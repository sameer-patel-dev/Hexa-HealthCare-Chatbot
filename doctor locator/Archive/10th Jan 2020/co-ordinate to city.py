import reverse_geocoder as rg 
import pprint 
from math import radians, sin, cos, acos
import csv

def reverseGeocode(coordinates): 
    result = rg.search(coordinates) 
    res = result[0].values().__str__().split('(')
    res = res[1][1:-2].split("'")
    result = []
    for i in range(len(res)):
        if i%2 != 0:
            result.append(res[i])
    print(result)
    location(result)

def location(res):
    filename = "../../Database/Location data/hospitals_directory.csv"
    with open(filename,'r') as csvfile:
        reader = csv.reader(csvfile)
        field_name = next(reader)
        print(field_name)
        hospitals = []
        for rows in reader:
            if rows[9] == res[2]:
                hospitals.append(rows)
        print(hospitals)
    #dist = 6371.01 * acos(sin(slat)*sin(elat) + cos(slat)*cos(elat)*cos(slon - elon))
    #print("The distance is %.2fkm." % dist)
    


    
# Driver function 
if __name__=="__main__":
    # Coorinates tuple.Can contain more than one pair. 
    coordinates =(19.0723225,72.9006249) 
      
    reverseGeocode(coordinates)  
