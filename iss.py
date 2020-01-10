#!/usr/bin/env python
import requests
import json
import turtle

__author__ = 'Bryan'


def get_astronauts():
    """ Obtain list of astronauts currently in space

    Print their full names, the spacecraft they are currently on board,
    and the total number of astronauts in space.
    """

    response = requests.get("http://api.open-notify.org/astros.json")

    data_dict = json.loads(response.content)
    people_list = data_dict['people']
    print("People currently in space: {}\n".format(data_dict['number']))
    print("Craft => Full_Name\n{}\n".format(people_list))


def get_coordinates():
    """
    Using another public API, obtain the current geographic coordinates
    (lat/lon) of the space station, along with a timestamp.
    """

    response = requests.get("http://api.open-notify.org/iss-now.json")
    data = response.content
    geo_coordinates = json.loads(data)
    print(geo_coordinates["iss_position"],
          "Time Stamp: {}\n".format(geo_coordinates["timestamp"]))


def part_C():
    window = turtle.Screen()
    window.title("poop")
    turtle.bgpic("map.gif")
    turtle.setup(width=0.5, height=0.4)
    turtle.setpos(-50, 150)
    turtle.write("International Space Stations Current Location!",
                 font=(40, "bold"))
    turtle.penup()

    apple = turtle.Turtle()
    apple.screen.register_shape("iss.gif")
    apple.screen.getshapes()
    apple.shape("iss.gif")

    """
    Examples:
    >>> setup (width=200, height=200, startx=0, starty=0)

    sets window to 200x200 pixels, in upper left of screen

    >>> setup(width=.75, height=0.5, startx=None, starty=None)

    sets window to 75% of screen by 50% of screen and centers

        >>> setworldcoordinates(-10,-0.5,50,1.5)
    >>> for _ in range(36):
    ...     left(10)
    ...     forward(0.5)

    """


def main():
    # get_astronauts()
    # get_coordinates()
    part_C()


if __name__ == '__main__':
    print("\n")
    main()
    print("\n")
