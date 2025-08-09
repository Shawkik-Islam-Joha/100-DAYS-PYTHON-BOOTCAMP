def calculate_voltage(current, resistance):
    voltage = current * resistance
    return voltage

I = 2.5   
R = 4     
V = calculate_voltage(I, R)
print("Voltage:", V, "volts")
