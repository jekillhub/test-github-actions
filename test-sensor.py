from sensor import Sensor
import unittest

class TestSensor(unittest.TestCase):
    def test_sum(self):
        sensor_object = Sensor()

        temperature = sensor_object.get_random_temperature()
        humidity = sensor_object.get_random_humidity()
        #atmospheric_pressure = sensor_object.get_random_atmospheric_pressure()

        self.assertEqual(sensor_object.sum(temperature,humidity), temperature - humidity)

if __name__ == '__main__':
    unittest.main()