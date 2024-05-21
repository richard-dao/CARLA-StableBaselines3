"""
CARLA Reset Function
"""


import carla

def reset_carla(host="localhost", port=2000):
    client = carla.Client(host, port)
    world = client.get_world()

    sensors = world.get_actors().filter("sensor.*")
    vehicles = world.get_actors().filter("vehicle.*")
    walkers = world.get_actors().filter("walker.*")

    for sensor in sensors:
        sensor.destroy()

    for vehicle in vehicles:
        vehicle.destroy()

    for walker in walkers:
        walker.destroy()
