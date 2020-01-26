import reverse_geocoder as rg 
import pprint,sqlite3 
from math import radians, sin, cos, acos, atan2, sqrt
PI = 3.14159265

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
    con = sqlite3.connect('doctor.db')
    cur = con.cursor()
    cur.execute("select Location_Coordinates,Location,Hospital_Name,Address_Original_First_Line,State,District,Pincode,Telephone from hospital_location where District = ?",(res[2],))
    hospital_list = cur.fetchall()
    slat = float(res[0])
    slon = float(res[1])
    final_list = []
    for i in range(len(hospital_list)):
        coordinates = hospital_list[i][0]
        Co_ordinates= coordinates.split(',')
        if Co_ordinates[0] not in ['NA','Error']:
            elat = float(Co_ordinates[0])
            elon = float(Co_ordinates[1])
            dist = getDistanceFromLatLonInKm(slat,slon,elat,elon)
            if dist < 5:
                final_list.append(hospital_list[i])
    print(final_list[:10])

def getDistanceFromLatLonInKm(lat1,lon1,lat2,lon2):
  R = 6371; # Radius of the earth in km
  dLat = deg2rad(lat2-lat1);  # deg2rad below
  dLon = deg2rad(lon2-lon1); 
  a = sin(dLat/2) * sin(dLat/2) + cos(deg2rad(lat1)) * cos(deg2rad(lat2)) * sin(dLon/2) * sin(dLon/2) 
  c = 2 * atan2(sqrt(a), sqrt(1-a)); 
  d = R * c; # Distance in km
  return d;

def deg2rad(deg):
    return deg * (PI/180)


    
# Driver function 
if __name__=="__main__":
    # Coorinates tuple.Can contain more than one pair. 
    coordinates =(19.0723225,72.9006249) 
      
    reverseGeocode(coordinates)  
