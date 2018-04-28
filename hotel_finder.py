import requests
auth = ('booking_hackathon_ichack18','WorkingAtBooking.com2018')
city = 'https://distribution-xml.booking.com/2.1/json/autocomplete?language=en;text=jakarta indonesia'
city_id = requests.get(city, auth=auth).json()['result'][0]['id']

hotel_avaiability = 'https://distribution-xml.booking.com/2.1/json/hotelAvailability?checkin=2018-07-29&checkout=2018-07-30&city_ids='+city_id+'&room1=A,A&extras=room_details,hotel_details'

hotel_id = requests.get(hotel_avaiability, auth=auth).json()['result'][2]['hotel_id']

hotel_cost = 'https://distribution-xml.booking.com/2.1/json/blockAvailability?checkin=2018-07-27&checkout=2018-07-28&hotel_ids='+str(hotel_id)

hotel_price = city_id = requests.get(hotel_cost, auth=auth).json()['result'][0]


print(hotel_price)
'Keys in output json var'
# for i in output['result'][0]:
#     print(i)
# region
# country_name
# city_ufi
# label
# type
# longitude
# url
# latitude
# id
# country
# nr_hotels
# name
# city_name
# language
# right-to-left