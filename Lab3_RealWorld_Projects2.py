LAST_NAME = "Manansala"
SEED_NUM = 9
FAVORITE_ARTIST = "Joshua Garcia"

def generate_fault_code():
    name_value = sum(ord(c) for c in LAST_NAME)
    artist_value = sum(ord(c) for c in FAVORITE_ARTIST)

    fault_code = (name_value + artist_value + SEED_NUM) % 1000

    return fault_code

def fault_trace(fault_code, trace, call_count):
    call_count += 1

    trace.append(f"Level {call_count}: Fault Code = {fault_code}")

    if fault_code <= 10:
        trace.append("Base condition reached.")
        return trace, call_count

    new_code = fault_code - 10
    return fault_trace(new_code, trace, call_count)

print("===== RECURSIVE FAULT TRACE =====")
print(f"Student: {LAST_NAME}")
print(f"Seed Number: {SEED_NUM}")
print(f"Favorite Artist: {FAVORITE_ARTIST}")

fault_code = generate_fault_code()

print("\nGenerated Fault Data:")
print(f"Fault Code: {fault_code}")

trace = []
trace, call_count = fault_trace(fault_code, trace, 0)

print("\nRecursive Trace:")
for step in trace: 
    print(step)

print(f"\nNumber of Recursive Calls: {call_count}")

print("\nExecution Log:")
print("Recursive fault tracing completed.")

print("\nFinal Output:")
print(f"Final Fault Code: {trace[-2] if len(trace) > 1 else trace[-1]}")
print("Fault trace completed successfully.")