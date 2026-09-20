from telemetry import generate_telemetry, validate_reading
from diagnostics import process_data, recursive_analysis

LAST_NAME = "Manansala"
SEED_NUM = 9
FAVORITE_ARTIST = "Joshua Garcia"

print("===== INTELLIGENT EQUIPMENT MONITORING PIPELINE =====")

print(f"Student: {LAST_NAME}")
print(f"Seed Number: {SEED_NUM}")
print(f"Favorite Artist: {FAVORITE_ARTIST}")

readings = []
valid_count = 0
invalid_count = 0

print("\nGenerated Telemetry Data:")
for reading in generate_telemetry(
    LAST_NAME, SEED_NUM, FAVORITE_ARTIST
):
    print(reading)
    try:
        validate_reading(reading)
        readings.append(reading)
        valid_count += 1
    except ValueError as error:
        print(f"Invalid reading: {error}")
        invalid_count += 1

average_temperature, abnormal_count = process_data(readings)

print("\nValid/Invalid Results:")
print(f"Valid readings: {valid_count}")
print(f"Invalid readings: {invalid_count}")

print("\nProcessed Results:")
print(f"Average Temperature: {average_temperature}")
print(f"Abnormal Conditions: {abnormal_count}")

print("\nRecursive Analysis:")
print(recursive_analysis(abnormal_count))

print("\nFinal Diagnostic Summary:")
print(f"Processed readings: {valid_count + invalid_count}")
print(f"Abnormal conditions: {abnormal_count}")

if abnormal_count > 0:
    print("WARNING")
else:
    print("NORMAL")

print("\nExecution Log:")
print("Telemetry generated")
print("Data validated")
print("Data processed")
print("Abnormal conditions analyzed") 
print("Diagnostic report completed")

print("\nFinal Output:")
print("Equipment diagnostic report generated successfully.")