import requests
import pandas as pd
import json
from math import log10, radians, atan2, sin, cos, sqrt
from datetime import datetime, timedelta


class Hotels:
    def __init__(self, coords, checkin_date, nr_days, max_budget=20, hotel_nr=5, adults_nr=1, radius=25):
        self.coords = coords
        self.checkin = checkin_date
        date = datetime.strptime(checkin_date, "%Y-%m-%d")
        self.nr_days = nr_days
        self.checkout = date + timedelta(days=self.nr_days)
        self.checkout = datetime.strftime(self.checkout, "%Y-%m-%d")
        self.budget = max_budget*nr_days
        self.auth = ('booking_hackathon_ichack18', 'WorkingAtBooking.com2018')
        # self.city_api = 'https://distribution-xml.booking.com/2.1/json/autocomplete?language=en;text='+ self.coords
        # self.city_id = requests.get(self.city_api, auth=self.auth).json()['result'][0]['id']
        self.hotel_nr = hotel_nr
        self.adults_nr = "A," * adults_nr
        self.adults_nr = self.adults_nr[:len(self.adults_nr) - 1]
        self.radius = str(radius)

    def available_hotels(self):
        if self.nr_days >0:
            # hotel_availables = 'https://distribution-xml.booking.com/2.1/json/hotelAvailability?checkin=' + self.checkin + \
            #                    '&checkout=' + self.checkout + '&city_ids=' + self.city_id + '&room1=' + self.adults_nr + \
            #                    '&extras=room_details,hotel_details&currency=EUR'
            hotel_availables = 'https://distribution-xml.booking.com/2.1/json/hotelAvailability?checkin=' + self.checkin + \
                               '&checkout=' + self.checkout + '&latitude=' + str(self.coords[0]) + '&longitude=' + str(
                self.coords[1]) + '&radius=' + self.radius + '&room1=' + self.adults_nr + \
                               '&extras=room_details,hotel_details&currency=EUR'
            self.hotels = requests.get(hotel_availables, auth=self.auth).json()['result']
                # self.hotels = None
            # json.dump(self.hotels, open("temp.json", 'w'), indent=4)
        else:
            self.hotels = None
        return self.hotels

    def price_quality(self, the_hotel,dist):
        try:
            stars = float(the_hotel["stars"])
            review = float(the_hotel["review_score"])
            rev_nr = float(the_hotel["review_nr"])
            breakfast =int(the_hotel['rooms'][0]["breakfast_included"])

        except KeyError:  # if no review/star give minimum score
            stars = 1
            review = 1
            rev_nr = 1
            breakfast = 0
        price = float(the_hotel["price"])

        return abs((price * 2) / (review + 0.4 * (review - 5) * (1.0 + 0.1 * int(log10(rev_nr) - 1)))+breakfast*0.5)

    def dist(self,lat1, lon1, lat2, lon2):
        r = 6371
        lat1 = radians(lat1)
        lon1= radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)
        delta_lat = (lat2 - lat1)
        delta_lon = (lon2 - lon1)
        a = sin(delta_lat / 2) * sin(delta_lat / 2) + cos(lat1) * cos(lat2) * sin(delta_lon / 2) * sin(delta_lon / 2);
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        d = r * c
        return d

    def hotels_ranking(self):
        hotels_df = pd.DataFrame(columns=['name', 'price', 'heuristic', 'position', 'hotel_id', 'distance', 'breakfast', 'rev_score'])

        for hotel in self.available_hotels():
            if hotel["price"] < self.budget:
                # print(hotel['rooms'][0]["extra_charge"][1]["excluded"])
                # name.append(hotel['hotel_name'])
                # hotel_price.append(hotel["price"])
                # hotel_heuristic.append(price_quality(hotel))
                try:
                    score_rews = hotel['review_score']
                except KeyError:
                    score_rews= 0

                dist = self.dist(float(hotel['location']['latitude']), float(hotel['location']['longitude']),
                                 self.coords[0], self.coords[1])

                real_price = hotel["price"] #+ hotel['rooms'][0]["extra_charge"]["amount"]+hotel['rooms'][0]["extra_charge"][1]["amount"]
                hotels_df = hotels_df.append(
                    {'name': hotel['hotel_name'], 'price': real_price, 'heuristic': self.price_quality(hotel,dist),
                     'position': (hotel['location']['latitude'], hotel['location']['longitude']),
                     'hotel_id': hotel['hotel_id'], 'distance': dist, 'breakfast':str(bool(hotel['rooms'][0]["breakfast_included"])),'rev_score':score_rews}, ignore_index=True)

        # hotels_df['price'] = hotel_price
        # hotels_df["Quality heuristic"] = hotel_heuristic
        hotels_df.set_index('hotel_id', drop=True, inplace=True)
        hotels_df = hotels_df.sort_values(['heuristic'])
        if self.hotel_nr > len(hotels_df["heuristic"]):
            self.hotel_nr = len(hotels_df["heuristic"])

        # hotel_array = hotels_df.as_matrix()
        # hotels_df.to_excel("C:\\Users\Daniel\Downloads\BSc 3rd year\HackDelft\Bacpac\prices.xlsx")

        return hotels_df.head(self.hotel_nr)  # hotel_array[:hotel_nr, :]  # hotels_df.iloc[[0:self.hotel_nr]]

    def get_average_price(self):
        if  self.available_hotels()!= None and self.hotels_ranking().empty == False:
            try:
                self.price = self.hotels_ranking()["price"].mean()
                # print(self.hotels_ranking())
            except KeyError:
                self.price = " This destination was deleted from your itinerary"
                self.nr_days = 0
        else:
            self.price = " This destination was deleted from your itinerary"
            self.nr_days = 0

        return self.price


if __name__ == "__main__":
    city = (-8.51367100280735,119.716000556946)
    max_budget = 20
    checkin_date = '2018-05-29'
    nr_days = 0
    hotel_nr = 20
    adults_nr = 1
    radius=5
    my_hotels = Hotels(city, checkin_date, nr_days)
    print(my_hotels.hotels_ranking())
