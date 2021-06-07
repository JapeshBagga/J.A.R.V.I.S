import requests
import datetime
import json

#Opening The Settings.json file for fetching details
with open('c:/Users/japba/Desktop/Projects/Jarvis/settings.json','r') as file:
    settings = json.load(file)
browser_header = {"User-Agent": settings['user-agent']}  # Google "My User Agent" And Replace It

DIST_ID = 488 # Ludhiana
PIN_CODE = settings['pin-code'] #Model Town
numdays = settings['days']
age = settings['age']

print_flag = 'y' # Print available centre description (y/n)?

base = datetime.datetime.today()
date_list = [base + datetime.timedelta(days=x) for x in range(numdays)]
date_str = [x.strftime("%d-%m-%Y") for x in date_list]



# Retriviing Districts code with state codes
def findDistrictCodes():
    for state_code in range(1,40):
        print("State code: ", state_code)
        response = requests.get("https://cdn-api.co-vin.in/api/v2/admin/location/districts/{}".format(state_code), headers=browser_header)
        json_data = json.loads(response.text)
        for i in json_data["districts"]:
            print(i["district_id"],'\t', i["district_name"])
        print("\n")

# Retriviing Vaccination Locations and details with Distrcit code
def findByDistrict():
    for INP_DATE in date_str:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(DIST_ID, INP_DATE)
        response = requests.get(URL, headers=browser_header)
        if response.ok:
            resp_json = response.json()
            # print(json.dumps(resp_json, indent = 1))
            if resp_json["centers"]:
                print("Available on: {}".format(INP_DATE))
                if(print_flag=='y' or print_flag=='Y'):
                    for center in resp_json["centers"]:
                        for session in center["sessions"]:
                            if session["min_age_limit"] <= age:
                                print("\t", center["name"])
                                print("\t", center["block_name"])
                                print("\t Price: ", center["fee_type"])
                                print("\t Available Capacity: ", session["available_capacity"])
                                if(session["vaccine"] != ''):
                                    print("\t Vaccine: ", session["vaccine"])
                                print("\n\n")      
            else:
                print("No available slots on {}".format(INP_DATE))
    
# Retriviing Vaccination Locations and details with Pin code
def findByPin():
    for INP_DATE in date_str:
        URL = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode={}&date={}".format(PIN_CODE, INP_DATE)
        response = requests.get(URL, headers=browser_header)
        if response.ok:
            resp_json = response.json()
            # print(json.dumps(resp_json, indent = 1))
            flag = False
            if resp_json["centers"]:
                result = []
                print("Available on: {}".format(INP_DATE))
                if(print_flag=='y' or print_flag=='Y'):
                    for center in resp_json["centers"]:
                        for session in center["sessions"]:
                            if session["min_age_limit"] <= age:
                                vaccine_info =  center["vaccine_fees"][0]
                                block_name,name,fee_type,vaccine,price = center["block_name"], center["name"], center["fee_type"], vaccine_info["vaccine"], vaccine_info["fee"]
                                # print("\t", name)
                                # print("\t", block_name)
                                # print("\t Price: ", fee_type)
                                # print("\t Available Capacity: ", session["available_capacity"])
                                # if(session["vaccine"] != ''):
                                #     print("\t Vaccine: ", vaccine)
                                #res = vaccine, "is available @ ",price," on ",INP_DATE," at",name,block_name
                                res = "At {} {}, {} is available @ {} Rupees, as per {} ".format(name,block_name,vaccine,price,INP_DATE)
                                result.append(res)
            else:
                result = "No available slots on {}".format(INP_DATE)
    return result

if __name__ == '__main__':
    result = findByPin()
    if type(result) is list:
        print("There are ",len(result), "Locations Avaiable near you")
        for res in result:
            print(str(res))
    else: 
        print(result)
