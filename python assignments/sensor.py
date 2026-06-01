def get_sensor_data():
    data = input("Enter 6 sensor values: ")

    sensors = list(map(int, data))

    active_sensors = len(list(filter(lambda x: x == 1, sensors)))

    print("Sensors detecting line:", active_sensors)

    return sensors, active_sensors