import requests
import json
auth = ('booking_hackathon_ichack18','WorkingAtBooking.com2018')
cities_req='https://distribution-xml.booking.com/2.1/json/cities=Delft'
api_url='https://developers.booking.com/api/'
cities = ['Kuta', 'Bali Ubud', 'Nusa Penida', 'Gili Islands', 'Borobudur', 'Ujung Kulon', 'Mount Bromo', 'Yogyakarta',
          'Jakarta', 'Lombok', 'Flores', 'Labuan Bajo']
get_city_ids = [for i in cities]
ams = 'https://distribution-xml.booking.com/2.1/json/autocomplete?language=en;text=Ujung Kulon'

magic = 'https://distribution-xml.booking.com/2.1/json/hotelAvailability?checkin=2018-07-27&checkout=2018-07-28&city_ids=-1565670&room1=A,A&extras=room_details,hotel_details'
req = requests.get(magic, auth=auth)
#output = req.json()
#json1_sata = json.loads(output)[1]
print(req.content)
