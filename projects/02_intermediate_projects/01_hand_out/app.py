                        # MILESTONE 1

# A few years ago, NASA made history with the first controlled flight on another planet. 
# Its latest Mars Rover, Perseverance, has onboard a 50cm high helicopter called Ingenuity. 
# Ingenuity made its third flight, during which it flew faster and further than it had on any of its test flights on Earth.
#  Interestingly, Ingenuity uses Python for some of its flight modeling software!

# Ingenuity on the surface of Mars (source: NASA)

# When programming Ingenuity, one of the things that NASA engineers need to account for is the fact that due to the weaker gravity on Mars, an 
# Earthling's weight on Mars is 37.8% of their weight on Earth. Write a Python program that prompts an Earthling to enter their weight on Earth
#  and prints their calculated weight on Mars.
# The output should be rounded to two decimal places when necessary.
#  Python has a round function which can help you with this. You pass in the value to be rounded and the number of decimal places to use.
#  In the example below, the number 3.1415926 is rounded to 2 decimal places which is 3.14. 


def weight_on_mars():
   earth_weight = float(input("Enter your weight on Earth in kg: "))
   mars_weight = earth_weight * 0.378
   rounded_mars_weight = round(mars_weight, 2)
   print(f"Your weight on Mars is {rounded_mars_weight} kg") 

# Call the weight_on_mars function
weight_on_mars()


#                         #  MILESTONE 2
# # ars is not the only planet in our solar system with its own unique gravity.
# #  In fact, each planet has a different gravitational constant, which affects how much an object would weigh on that planet.
# #  Below is a list of the constants for each planet compared to Earth's gravity:

# # Mercury: 37.6%
# # Venus: 88.9%
# # Mars: 37.8%
# # Jupiter: 236.0%
# # Saturn: 108.1%
# # Uranus: 81.5%
# # Neptune: 114.0%                       


def weight_on_planet():
   earth_weight = float(input("Enter your weight on Earth in kg: "))

   planet = input("Enter the name of the planet: ")

   if planet == "mercury":
      mars_weight = earth_weight * 0.376

   elif planet == "venus":
      mars_weight = earth_weight * 0.889

   elif planet == "mars":
      mars_weight = earth_weight * 0.378

   elif planet == "jupiter":
      mars_weight = earth_weight * 2.36

   elif planet == "saturn":
      mars_weight = earth_weight * 0.108

   elif planet == "uranus":
      mars_weight = earth_weight * 0.815

   elif planet == "neptune":
      mars_weight = earth_weight * 1.14

   else:
      print("Invalid planet name.")
      return
   
   rounded_mars_weight = round(mars_weight, 2)
   print(f"Your weight on {planet} is {rounded_mars_weight} kg")

# Call the weight_on_planet function
weight_on_planet()   


# example 2


planetary_weight_constants = {
   "mercury": 37.6,
   "venus": 88.9,
   "mars": 37.8,
   "jupiter": 236.0,
   "saturn": 108.1,
   "uranus": 81.5,
   "neptune": 114.0
}


def weight_on_planet():
   earth_weight = float(input("Enter your weight on Earth in kg: "))
   planet = input("Enter the name of the planet: ")
   if planet in planetary_weight_constants:
      
      planet_weight = planetary_weight_constants[planet] / 100
      print(f"Your weight on {planet} is {round(earth_weight * planet_weight, 2)} kg")

   else:
      print("Invalid planet name.")

weight_on_planet()      