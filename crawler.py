import requests

url = "https://wish.wis.ntu.edu.sg/webexe/owa/aus_schedule.main_display1"

payload = "acadsem=2016%3B1&r_search_type=F&boption=CLoad&staff_access=false&r_subj_code=Enter%20Keywords%20or%20Course%20Code&r_course_yr=ACC%3BGA%3B2%3BF"
headers = {'content-type': 'application/x-www-form-urlencoded'}

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
