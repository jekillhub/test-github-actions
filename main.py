from sensor import Sensor
from pprint import pprint

class Main:

  if __name__ == "__main__":
    sensor_object = Sensor()

    new_measure = {}
    new_measure['temperature'] = sensor_object.get_random_temperature()
    new_measure['humidity'] = sensor_object.get_random_humidity()
    new_measure['atmospheric_pressure'] = sensor_object.get_random_atmospheric_pressure()

    pprint(new_measure)