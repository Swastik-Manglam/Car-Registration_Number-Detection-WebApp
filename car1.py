import cgi
import subprocess
import js2py
print("context-type:text/html")
print()

def get_details_of_vehicle(Reg_no):
    r = requests.get("http://www.regcheck.org.uk/api/reg.asmx/CheckIndia?RegistrationNumber={0}&username=swastik".format(str(Reg_no)))
    json_data = json.dumps(xmltodict.parse(r.content))
    detail = json.loads(json_data)
    return json.loads(detail['Vehicle']['vehicleJson'])

f = cgi.FieldStorage()
no = f.getvalue("x")
#out= subprocess.getoutput(cmd)
#print(get_details_of_vehicle(no))
print("{'Description': 'HYUNDAI I10 1.2 L KAPPA SPORTZ GLS',\
 'RegistrationYear': '2011',\
 'CarMake': {'CurrentTextValue': 'HYUNDAI'},\
 'CarModel': {'CurrentTextValue': 'I10 1.2 L KAPPA SPORTZ GLS'},\
 'Variant': '1.2 Kappa GLS Sportz Petrol 1197.0',\
 'EngineSize': {'CurrentTextValue': '1197.0'},\
 'MakeDescription': {'CurrentTextValue': 'HYUNDAI'},\
 'ModelDescription': {'CurrentTextValue': 'I10 1.2 L KAPPA SPORTZ GLS'},\
 'NumberOfSeats': {'CurrentTextValue': '5'},\
 'VechileIdentificationNumber': 'MALAN51CLBM826996A',\
 'EngineNumber': 'G4LAAM585304',\
 'FuelType': {'CurrentTextValue': 'PETROL'},\
 'RegistrationDate': '26/02/2011',\
 'Owner': 'MR SHAILESH KUMAR',\
 'Fitness': '',\
 'Insurance': '2022-02-07',\
 'PUCC': '2021-10-09',\
 'VehicleType': 'MOTOR CAR(LMV)',\
 'Location': 'DTO,RANCHI',\
 'ImageUrl': 'http://www.carregistrationapi.in/image.aspx/@SFlVTkRBSSBJMTAgMS4yIEwgS0FQUEEgU1BPUlRaIEdMUw=='}")
