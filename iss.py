#!/usr/bin/env python
import requests
import time
import json
import turtle

__author__ = 'Bryan'


def get_astronauts():
    response = requests.get("http://api.open-notify.org/astros.json")

    data_dict = json.loads(response.content)
    people_list = data_dict['people']
    print("People currently in space: {}\n".format(data_dict['number']))
    print("Craft => Full_Name\n{}\n".format(people_list))


def get_coordinates():

    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.content
    geo_coordinates = json.loads(data)
    print(geo_coordinates["iss_position"],
          "Time Stamp: {}\n".format(geo_coordinates["timestamp"]))
    return geo_coordinates


def indy_locate():
    payload = {'lat': '39.7', 'lon': '-86.1'}
    r = requests.get("http://api.open-notify.org/iss-pass.json",
                     params=payload)
    # print(type(r.text))
    indy_content = json.loads(r.content)

    rise_time = indy_content["response"][0]["risetime"]
    our_time = time.ctime(rise_time)
    print("\nNext time ISS will be over Indianapolis: {}".format(our_time))
    indy_location = [our_time, 39.7, -86.1]

    return indy_location


def create_Turtle():
    window = turtle.Screen()

    window.title("poop")
    turtle.bgpic("map.gif")
    turtle.setup(width=0.5, height=0.4)
    turtle.penup()

    turtle.setpos(-50, 150)
    turtle.color("yellow")
    turtle.write("International Space Stations Current Location!",
                 font=(40, "bold"))
    turtle.penup()

    iss = turtle.Turtle()
    iss.register_shape("iss.gif")
    iss.getshapes()
    iss.shape("iss.gif")
    iss.penup()

    iss_coord = get_coordinates()["iss_position"]
    latitude = iss_coord["latitude"]
    longitude = iss_coord["longitude"]
    # latitude = y, longitude = x, to make it work
    iss.setpos(iss_coord[2], iss_coord[1])

    indy_location = indy_locate()
    dot = turtle.Turtle()
    dot.shape("circle")
    dot.color("yellow")
    dot.setpos(longitude, latitude)
    my_string = "{}".format(indy_location[0])
    dot.write(my_string, font=("Arial", "bold"))

    turtle.exitonClick()


def main():
    get_astronauts()
    create_Turtle()


if __name__ == '__main__':
    print("\n")
    main()
    print("\n")
