import requests
import pandas as pd
import json
from math import log10


class Hotels:
    def __init__(self, city, checkin_date, checkout_date, max_budget, hotel_nr, adults_nr):
        self.city = city
        self.checkin = checkin_date
        self.checkout = checkout_date
        self.budget = max_budget
        self.auth = ('booking_hackathon_ichack18', 'WorkingAtBooking.com2018')
        self.city_api = 'https://distribution-xml.booking.com/2.1/json/autocomplete?language=en;text=' + self.city
        self.city_id = requests.get(self.city_api, auth=self.auth).json()['result'][0]['id']
        self.hotel_nr = hotel_nr
        self.adults_nr = "A," * adults_nr
        self.adults_nr = self.adults_nr[:len(self.adults_nr) - 1]

    def available_hotels(self):
        hotel_availables = 'https://distribution-xml.booking.com/2.1/json/hotelAvailability?checkin=' + self.checkin + \
                           '&checkout=' + self.checkout + '&city_ids=' + self.city_id + '&room1=' + self.adults_nr + \
                           '&extras=room_details,hotel_details&currency=EUR'
        self.hotels = requests.get(hotel_availables, auth=self.auth).json()['result']
        json.dump(self.hotels, open("temp.json", 'w'), indent=4)

        return self.hotels

    def price_quality(self, the_hotel):
        try:
            stars = float(the_hotel["stars"])
            review = float(the_hotel["review_score"])
            rev_nr = float(the_hotel["review_nr"])
        except KeyError:  # if no review/star give minimum score
            stars = 1
            review = 3
            rev_nr = 1
        price = float(the_hotel["price"])

        return abs(price / (review + 0.4*(review-5) * (1.0 + 0.1*int(log10(rev_nr)-1))))

    def hotels_ranking(self):

        hotels_df = pd.DataFrame(columns=['name', 'price', 'heuristic'])
        for hotel in self.available_hotels():
            if hotel["price"] < self.budget:
                # name.append(hotel['hotel_name'])
                # hotel_price.append(hotel["price"])
                # hotel_heuristic.append(price_quality(hotel))
                hotels_df = hotels_df.append(
                    {'name': hotel['hotel_name'], 'price': hotel["price"], 'heuristic': self.price_quality(hotel),
                     'position': (hotel['location']['latitude'], hotel['location']['longitude']),
                     'hotel_id': hotel['hotel_id']}, ignore_index=True)

        # hotels_df['price'] = hotel_price
        # hotels_df["Quality heuristic"] = hotel_heuristic
        hotels_df.set_index('hotel_id', drop=True, inplace=True)
        hotels_df = hotels_df.sort_values(['heuristic'])
        hotel_array = hotels_df.as_matrix()
        hotels_df.to_excel("C:\\Users\Daniel\Downloads\BSc 3rd year\HackDelft\Bacpac\prices.xlsx")

        return hotels_df.head(self.hotel_nr)#hotel_array[:hotel_nr, :]  # hotels_df.iloc[[0:self.hotel_nr]]


if __name__ == "__main__":
    city = "Ngadisari indonesia"
    max_budget = 130e5
    checkin_date = '2018-07-29'
    checkout_date = '2018-07-31'
    hotel_nr = 5
    adults_nr = 1
    my_hotels = Hotels(city, checkin_date, checkout_date, max_budget, hotel_nr, adults_nr)
    print(my_hotels.hotels_ranking())
