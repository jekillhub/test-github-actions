import random

class Sensor:

    @staticmethod
    def get_random_temperature():
        return random.uniform(-40, 40)

    @staticmethod   
    def get_random_humidity():
        return random.uniform(0, 100)

    @staticmethod 
    def get_random_atmospheric_pressure():
        return random.uniform(1065,1084.8)

    @staticmethod 
    def calculate_water_fusion_point(pressure):
        vP = (pressure * 0.0145038)
        if (not (pressure < 0.1)) and (not (pressure > 29000)):
            return ((-0.00000000000000001795*vP*vP*vP*vP*vP+0.00000000000008783408*vP*vP*vP*vP-0.00000000012723755581*vP*vP*vP-0.00000143315813123946*vP*vP-0.00745997412927792*vP+0.00984550279459087)*10)/10
        return None

    @staticmethod 
    def calculate_dew_point(temperature, humidity):
        aux = 100
        return pow((humidity/aux),0.125) * (112+(0.9*temperature))+((0.1*temperature)-112)

    @staticmethod 
    def get_road_state(temperature, humidity, pressure):
        dewPoint = calculate_dew_point(temperature, humidity);
        fusionPoint = calculate_water_fusion_point(pressure);
    
        if dewPoint < fusionPoint:
            return False
        return True