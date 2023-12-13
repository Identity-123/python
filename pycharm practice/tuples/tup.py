def capitalize_in_list():
    planets = ['mercury', 'venus', 'jupiter', 'earth', 'jupiter', 'saturn', 'uranus', 'neptune']
    planets = [planet.capitalize() for planet in planets]
    print(planets)


def tu_ple():
    t = ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune')
    print(type(t))
    print(t[-1])
    print(t[1:3])


tu_ple()