""""
This file searches for duplicate colors.
It returns a list of colors and the sectors they are used for. 
This is only an issue if sectors are adjascent to each other.

Create a new file in the Input folder called 'Positions_VG.json'. 
This file should be a json of the VG-key "Positions". I included an example of its contents. You should copy it from the VG repo (not beta)

"""
import json
def find_duplicate_json_strings(data):
    unique_values = {}  # Dictionary to store unique string values and their associated keys
    duplicate_values = {}  # Dictionary to store duplicate values and their associated keys

    def process_json(obj, parent_key=''):
        if isinstance(obj, dict):
            for key, value in obj.items():
                new_key = f"{parent_key}.{key}" if parent_key else key
                process_json(value, new_key)
        elif isinstance(obj, list):
            for i, element in enumerate(obj):
                new_key = f"{parent_key}[{i}]"
                process_json(element, new_key)
        elif isinstance(obj, str):
            if obj in unique_values:
                if obj in duplicate_values:
                    duplicate_values[obj].append(parent_key)
                else:
                    duplicate_values[obj] = [unique_values[obj], parent_key]
            else:
                unique_values[obj] = parent_key

    process_json(data)
    
    # Filter out values with only one occurrence
    duplicate_values = {key: value for key, value in duplicate_values.items() if len(value) > 1}
    
    return duplicate_values

# Example JSON data
json_data = {}

with open('Input/Positions_VG.json') as f:
    positions = json.load(f)["positions"]

for key in positions:
    json_data[key] = positions[key]["colours"][0]["hex"]

duplicates = find_duplicate_json_strings(json_data)

for value, keys in duplicates.items():
    print(f"Color {value} found for: {keys}")
