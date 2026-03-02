'''
Given a voltage reading, print "Under Voltage", "Nominal", or "Over Voltage".
(Nominal is between 3.0V and 3.3V inclusive.)
Input: 3.35
Output: Over Voltage
'''
voltage = 3.35

status = "Nominal" if 3.0 <= voltage <= 3.3 else "Under Voltage" if voltage < 3.0 else "Over Voltage"
print(status)

'''
Take an 8-bit register value and print if the **MSB** (most significant bit) is set or not.
Input: 0b10010010
Output: MSB set
'''
reg = 0b10010010

print("MSB set" if reg & 0b10000000 else "MSB not set")

'''
Enter a temperature and print "Overheat" (>75°C), "Normal" (25-75°C), or "Low Temp" (<25°C).
Input: 18
Output: Low Temp
'''
temp = 18

status = "Normal" if 25 <= temp <= 75 else "Low Temp" if temp < 25 else "Overheat"
print(status)


'''
Given two pin logic levels (0 or 1), print the type of logic gate output if these were inputs to an AND, OR, and XOR gate.
Input: 1, 0
Output: AND: 0, OR: 1, XOR: 1
'''
pin1, pin2 = 1, 0

and_out = pin1 & pin2
or_out = pin1 | pin2
xor_out = pin1 ^ pin2

print(f"AND: {and_out}, OR: {or_out}, XOR: {xor_out}")

'''
If a sensor value is outside the range 100–900, print "Sensor Fault". If within, print "Sensor OK".
Input: 950
Output: Sensor Fault
'''
sensor = 950

print("Sensor OK" if 100 <= sensor <= 900 else "Sensor Fault")

'''
Take an error code (integer). Print "Critical" if code ≥1000, "Warning" if 100–999, and "Info" if <100.
Input: 230
Output: Warning
'''
error_code = 230

status = "Critical" if error_code >= 1000 else "Warning" if 100 <= error_code <= 999 else "Info"
print(status)

'''
Given three boolean flags: `power_on`, `overcurrent`, `overvoltage`, print:
- "System Safe" if only `power_on` is True.
- "Shut Down: Overcurrent" if `overcurrent` is True.
- "Shut Down: Overvoltage" if `overvoltage` is True.
- "Critical Failure" if both faults are True.
Input: True, True, False
Output: Shut Down: Overcurrent
'''
power_on, overcurrent, overvoltage = True, True, False

if overcurrent and overvoltage:
    print("Critical Failure")
elif overcurrent:
    print("Shut Down: Overcurrent")
elif overvoltage:
    print("Shut Down: Overvoltage")
elif power_on:
    print("System Safe")
else:
    print("Unknown Status")
'''
Given a digital input value (0–255), determine and print which of 4 quadrants it falls into:
- 0–63, 64–127, 128–191, 192–255
'''
value = 150

if 0 <= value <= 63:
    quadrant = 1
elif 64 <= value <= 127:
    quadrant = 2
elif 128 <= value <= 191:
    quadrant = 3
else:
    quadrant = 4
#quadrant = 1 if 0 <= value <= 63 else 2 if 64 <= value <= 127 else 3 if 128 <= value <= 191 else 4
print("Quadrant:", quadrant)

'''
Given a digital input value (0–255), determine and print which of 4 quadrants it falls into:
- 0–63, 64–127, 128–191, 192–255
Enter a signal frequency (Hz). Print "Low Band" (<1000), "Mid Band" (1000–9999), "High Band" (10000–99999), or "Out of Range".
Input: 8000
Output: Mid Band
'''
freq = 8000

band = "Low Band" if freq < 1000 else "Mid Band" if freq <= 9999 else "High Band" if freq <= 99999 else "Out of Range"
print(band)

'''
Given three sensor readings, print "Majority High" if at least two readings are above a threshold (e.g., 50), otherwise "Majority Low".
Input: 40, 65, 70
Output: Majority High
'''
s1, s2, s3 = 40, 65, 70
threshold = 50

majority = "Majority High" if sum([s1>threshold, s2>threshold, s3>threshold]) >= 2 else "Majority Low"
print(majority)

'''
Enter a 16-bit value and print if parity (number of 1s) is even or odd.
Input: 0xAAAA
Output: Parity: Even
'''
value = 0xAAAA

parity = "Even" if bin(value).count('1') % 2 == 0 else "Odd"
print("Parity:", parity)

'''
Given a voltage and current reading, print "Power OK" if both are in safe ranges, otherwise print specific error:
- Voltage out of 3.0–3.3V: "Voltage Error"
- Current out of 10–500mA: "Current Error"
- Both out: "Power Error"
Given the status of three LEDs (on/off as 1/0), print which LEDs are ON. If all are off, print "All LEDs off".
Input: 0, 1, 0
Output: LED2 ON
'''
led1, led2, led3 = 0, 1, 0

leds_on = []
if led1: leds_on.append("LED1")
if led2: leds_on.append("LED2")
if led3: leds_on.append("LED3")

print("ON LEDs:", ", ".join(leds_on) if leds_on else "All LEDs off")

'''
Accept a device mode value:
- 0: "Standby"
- 1: "Active"
- 2: "Fault"
- Any other: "Unknown mode"
Enter two analog readings. Print "Match" if they are within 5 units of each other, "No Match" otherwise.
Input: 98, 101
Output: Match
'''
mode = 2

modes = {0: "Standby", 1: "Active", 2: "Fault"}
print(modes.get(mode, "Unknown mode"))

'''
Enter two analog readings. Print "Match" if they are within 5 units of each other, "No Match" otherwise.
Input: 98, 101
Output: Match
'''
a1, a2 = 98, 101
print("Match" if abs(a1 - a2) <= 5 else "No Match")