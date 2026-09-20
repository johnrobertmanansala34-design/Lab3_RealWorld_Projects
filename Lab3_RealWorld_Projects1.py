import random
from functools import wraps

LAST_NAME = "Manansala"
SEED_NUM = 9
FAVORITE_ARTIST = "Joshua Garcia"

seed_value = SEED_NUM + sum(ord(c) for c in LAST_NAME + FAVORITE_ARTIST)
random.seed(seed_value)

def diagnostic_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] Running {func.__name__}...")
        result = func(*args, **kwargs)
        print(f"[LOG] {func.__name__} completed.")
        return result
    return wrapper

def generate_readings():
    readings = {
        "temperature": round(random.uniform(60, 100), 2),
        "pressure": round(random.uniform(80, 120), 2),
        "vibration": round(random.uniform(1, 10), 2)
    }
    return readings

def validate_readings(readings):
    if not isinstance(readings, dict):
        raise ValueError("Invalid reading format.")

    if not 0 <= readings["temperature"] <= 150:
        raise ValueError("Invalid temperature reading.")

    if not 0 <= readings ["pressure"] <= 200:
        raise ValueError("Invalidd pressure reading.")

    if not 0 <= readings ["vibration"]:
        raise ValueError("Invalid vibration reading.")

    return True

def calculate_score(readings):
    temperature_score = readings["temperature"] / 150 * 100
    pressure_score = readings["pressure"] / 200 * 100
    vibration_score = readings["vibration"] / 20 * 100

    score = (temperature_score + pressure_score + vibration_score) / 3

    return round(score, 2)

def classify_condition(score):
    if score < 40:
        return "NORMAL"
    elif score < 70:
        return "WARNING"
    else:
        return "CRITICAL"

@diagnostic_log
def run_diagnostic():
    try:
        readings = generate_readings()

        print("\nGenerated Equipment Data:")
        for key, value in readings.items():
            print(f"{key.capitalize()}: {value}")

        validate_readings(readings)
        print("\nValidation Results: VALID")

        score = calculate_score(readings)
        condition = classify_condition(score)

        print("\nDiagnostic Results:")
        print(f"Diagnostic Score: {score}")
        print(f"Equipment Condition: {condition}")

        return readings, score, condition

    except ValueError as error:
        print(f"\nValidation Error: {error}")
        print("The program continues")

print("==== EQUIPMENT DIAGNOSTIC SYSTEM =====")
print(f"Student: {LAST_NAME}")
print(f"Seed Number: {SEED_NUM}")
print(f"Favorite Artist: {FAVORITE_ARTIST}")

run_diagnostic()

print("\nExecution Log: Diagnostic process completed.")
print("\nFinal Output: Equipment diagnostic report generated")