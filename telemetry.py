import random 

def generate_telemetry(last_name, seed_num, favorite_artist):
    import random
    seed = seed_num + sum(ord(c) for c in last_name + favorite_artist)
    random.seed(seed)

    for i in range(10):
        reading = {
            "temperature": round(random.uniform(50, 100), 2),
            "pressure": round(random.uniform(80, 120), 2),
            "vibration": round(random.uniform(1, 10), 2)
        }

        if i == 5:
            reading["temperature"] = -10

        yield reading

def validate_reading(reading):
    if reading["temperature"] < 0:
        raise ValueError("Invalid temperature")
    if reading["pressure"] < 0:
        raise ValueError("Invaliid pressure")
    if reading["vibration"] < 0:
        raise ValueError("Invalid vibration")
    return True