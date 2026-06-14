import math

# Global variable
station_name = "Kathmandu Weather Station"
temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]

def get_average(temps):
    return sum(temps)/len(temps)

def get_deviation(temps):
    # local_mean is a local variable
    local_mean = get_average(temps)
    variance_sum = 0
    for t in temps:
        variance_sum += (t-local_mean)**2
    variance = variance_sum/len(temps)
    return math.sqrt(variance)

def get_summary(temps):
    print(station_name)
    print("Min:", min(temps))
    print("Max:", max(temps))
    print("Average:", get_average(temps))
    print("Deviation:", get_deviation(temps))

# Demonstrating NameError with a comment as requested:
# print(local_mean) 
# This causes NameError because local_mean only exists inside get_deviation()

get_summary(temperatures)