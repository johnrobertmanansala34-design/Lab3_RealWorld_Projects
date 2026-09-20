def monitor_process(function):
    def wrapper(*args, **kwargs):
        print("[LOG] Diagnostic process started.")
        result = function(*args, **kwargs)
        print("[LOG] Diagnostic process completed.")
        return result
    return wrapper

calculate_average = lambda values: round(sum(values) / len(values), 2) if values else 0

def detect_abnormal(reading):
    temperature = reading.get("temperature", 0)
    pressure = reading.get("pressure", 0)
    vibration = reading.get("vibration", 0)

    return (
        temperature > 90
        or pressure > 110
        or vibration > 8
    )

def recursive_analysis(abnormal_count):
    if abnormal_count <= 0:
        return "No more abnormal conditions."
    return (
        f"Abnormal conditions traced."
        f"Remaining: {abnormal_count - 1}\n"
        + recursive_analysis(abnormal_count - 1)
    )

@monitor_process
def process_data(readings):
    temperatures = [r["temperature"] for r in readings]
    average_temperature = calculate_average(temperatures)
    abnormal_count = sum(
        1 for reading in readings if detect_abnormal(reading)
    )
    return average_temperature, abnormal_count
