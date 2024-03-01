import csv
from converter.temperature import celsius_to_fahrenheit, fahrenheit_to_celsius
from converter.distance import distance_to_meters, distance_to_feet

def convert_temperature(reading, target_unit):
    value, unit = reading[:-2], reading[-2:]
    print('convert_temperature unit', value, unit, target_unit)
    if unit == '°C' and target_unit == '°F':
        return celsius_to_fahrenheit(float(value))
    elif unit == '°F' and target_unit == '°C':
        return fahrenheit_to_celsius(float(value))
    elif unit == target_unit:
        return float(value)
    else:
        raise ValueError(f"Invalid temperature unit {target_unit}")

def convert_distance(reading, target_unit):
    value, unit = reading[:-1], reading[-1:]
    if unit != 'm':
        value, unit = reading[:-2], reading[-2:]
    print('convert_distance unit', value, unit, target_unit)
    if unit == 'm' and target_unit == 'ft':
        return distance_to_meters(float(value))
    elif unit == 'ft' and target_unit == 'm':
        return distance_to_feet(float(value))
    elif unit == target_unit:
        return float(value)
    else:raise ValueError(f'Invalid distance unit {target_unit}')


def main6(input_filename, output_filename, distance_target_unit, temperature_target_unit):
    with open(input_filename, 'r') as csvfile:
        reader = csv.DictReader(csvfile)
        rows = list(reader)

    converted_rows = []
    for row in rows:
        converted_temp = convert_temperature(row['Reading'], temperature_target_unit)
        converted_distance = convert_distance(row['Distance'], distance_target_unit)
        converted_row = {'Date': row['Date'], 'Distance':f'{converted_distance:.2f}{distance_target_unit}', 'Reading': f"{converted_temp:.2f}{temperature_target_unit}"}
        converted_rows.append(converted_row)


    with open(output_filename, 'w', newline='') as csvfile:
        fieldnames = ['Date', 'Distance', 'Reading']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(converted_rows)

if __name__ == "__main__":
    input_filename = "distance.csv"
    output_filename = "converted_distances.csv"
    distance_target_unit = 'm'
    temperature_target_unit = '°C'
    main6(input_filename, output_filename, distance_target_unit, temperature_target_unit)