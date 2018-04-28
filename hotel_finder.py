import requests
import pandas as pd
import json

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
        self.adults_nr = "A,"*adults_nr
        self.adults_nr = self.adults_nr[:len(self.adults_nr)-1]

    def available_hotels(self):
        hotel_availables = 'https://distribution-xml.booking.com/2.1/json/hotelAvailability?checkin=' + self.checkin + '&checkout=' + self.checkout + '&city_ids=' + self.city_id + '&room1='+self.adults_nr+'&extras=room_details,hotel_details'
        self.hotels = requests.get(hotel_availables, auth=self.auth).json()['result']
        # json.dump(self.hotels, open("temp.json", 'w'), indent=4)

        return self.hotels



    def price_quality(self, the_hotel):
        try:
            stars = float(the_hotel["stars"])
            review = float(the_hotel["review_score"])
        except KeyError:  # if no review/star give minimum score
            stars = 1
            review = 1
        price = float(the_hotel["price"])

        return price / (stars * review)

    def hotels_ranking(self):

        hotels_df = pd.DataFrame(columns=['name', 'price', 'heuristic'])
        for hotel in self.available_hotels():
            if hotel["price"] < self.budget:
                # name.append(hotel['hotel_name'])
                # hotel_price.append(hotel["price"])
                # hotel_heuristic.append(price_quality(hotel))
                hotels_df = hotels_df.append(
                    {'name': hotel['hotel_name'], 'price': hotel["price"], 'heuristic': self.price_quality(hotel),
                     'position': (hotel['location']['latitude'], hotel['location']['longitude']),'hotel_id': hotel['hotel_id']}, ignore_index=True)

        # hotels_df['price'] = hotel_price
        # hotels_df["Quality heuristic"] = hotel_heuristic
        hotels_df.set_index('hotel_id', drop=True, inplace=True)
        hotels_df = hotels_df.sort_values(['heuristic'])
        np_df = hotels_df.as_matrix()

        return np_df[:hotel_nr, :]  # hotels_df.iloc[[0:self.hotel_nr]]


if __name__ == "__main__":
    city = "gili trawangan indonesia"
    max_budget = 130e5
    checkin_date = '2018-07-29'
    checkout_date = '2018-07-30'
    hotel_nr = 20
    adults_nr = 5
    my_hotels = Hotels(city, checkin_date, checkout_date, max_budget, hotel_nr, adults_nr)
    print(my_hotels.hotels_ranking())
