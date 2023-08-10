#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

print("+++======== Create a new State ========+++")
state = State()
state.name = "Ogun-State"
state.save()
print(state)

print("+++======== Create a new City =========+++")
city = City()
city.name = "Ijebu-Ode"
for key, value in storage.all().items():
    if "State" in key and value.name == "Ogun-State":
        State.id = value.id
city.state_id = State.id
city.save()
print(city)


print("+++======== Create a new Amenity ========+++")
amenity = Amenity()
amenity.name = "Twin-Bedroom"
amenity.save()
print(amenity)

print("+++======== Create a new Place ========+++")
place = Place()
for key, value in storage.all().items():
    if "City" in key and value.name == "Ijebu-Ode":
        City.id = value.id
place.city_id = City.id

for key, value in storage.all().items():
    if "User" in key and value.first_name == "John":
        User.id = value.id
place.user_id = User.id
place.name = "The place"
place.description = "It's a beautiful place to be"
place.number_room = 2
place.number_bathroom = 1
place.max_guest = 2
place.price_by_night = 200
place.latitude = "N50E"
place.longitude = "S255W"
for key, value in storage.all().items():
    if "Amenity" in key and value.name == "Twin-Bedroom":
        Amenity.id = value.id
place.amenity_ids = Amenity.id
place.save()
print(place)
