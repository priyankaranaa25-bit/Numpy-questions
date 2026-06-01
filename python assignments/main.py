from sensor import get_sensor_data
from movement import decide_movement

sensors, active_sensors = get_sensor_data()

action = decide_movement(sensors)

print("Sensor Values:", sensors)
print("Active Sensors:", active_sensors)
print("Robot Action:", action)