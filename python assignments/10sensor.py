def get_sensor_data():
    data = input("Enter 6 sensor values: ").split()

    sensors = list(map(int, data))

    count = len(list(filter(lambda x: x == 1, sensors)))

    print("Sensors detecting line:", count)

    return sensors,active_sensors