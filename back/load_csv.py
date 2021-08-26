import requests

from back.models import City, Hotel


# Load data the City from file CSV with request lib
def load_csv_city():
    # Define url, username, and password
    url = 'http://rachel.maykinmedia.nl/djangocase/city.csv'
    user, password = 'python-demo', 'claw30_bumps'
    resp = requests.get(url, auth=(user, password))
    if resp.status_code == 200:
        citys = resp.text.split('\n')  # Split value for \n
        for c in citys:
            city = c.split(';')  # Split value for ;
            if len(city) == 2:  # If have two value
                code, name = str(city[0]).replace('"', ''), str(city[1]).replace('"',
                                                                                 '')  # create variables and delete value " in each variable and  iqual with the value1 an value2
                citys_list = City.objects.filter(code=code, name=name)  # filter for value and save in variable
                if len(citys_list) == 0:
                    city_obj = City()
                    city_obj.code = code
                    city_obj.name = name
                    city_obj.save()  # if not exist save and  continue for each value if found
    else:
        return False
    return True


# Load data the City from file CSV with request lib
def load_csv_hotel():
    load_csv_city()
    url = 'http://rachel.maykinmedia.nl/djangocase/hotel.csv'
    user, password = 'python-demo', 'claw30_bumps'
    resp = requests.get(url, auth=(user, password))
    if resp.status_code == 200:
        hotels = resp.text.split('\n')
        # print(hotels)
        for hotel in hotels:
            # print(hotel)
            h = hotel.split(';')
            # print(h)
            if len(h) == 3:
                city_code, code, name = str(h[0]).replace('"', ''), str(h[1]).replace('"', ''), str(
                    h[2]).replace('"', '')
                # print(city, hotel_code, hotel_name)
            city = City.objects.filter(code=city_code).first()
            if city is not None:
                hotels_list = Hotel.objects.filter(code=code, name=name)
                if len(hotels_list) == 0:
                    hotel = Hotel()
                    hotel.code = code
                    hotel.name = name
                    hotel.cit = city
                    hotel.save()
                    print(hotels)
    else:
        return False
    return True
