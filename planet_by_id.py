#Question

#The function is not returning the correct values. Can you figure out why?
#Example (Input --> Output ):

"""
def get_planet_name(id):
    # This doesn't work; Fix it!
    name=""
    switch id:
        case 1: name = "Mercury"
        case 2: name = "Venus"
        case 3: name = "Earth"
        case 4: name = "Mars"
        case 5: name = "Jupiter"
        case 6: name = "Saturn"
        case 7: name = "Uranus"  
        case 8: name = "Neptune"
    return name
"""    

#Solution
def get_planet_name(id):
    planet_names = {
        1: "Mercury",
        2: "Venus",
        3: "Earth",
        4: "Mars",
        5: "Jupiter",
        6: "Saturn",
        7: "Uranus" , 
        8: "Neptune"
        }
    return planet_names.get(id, "Unknown")


#NB:
#Python does not have a switch statement as seen in some other programming languages. To achieve the same functionality, you can use a dictionary to map the id values to the planet names.
