import csv
import json

class FileConverter:
    def __init__(self):
        pass

    def csv_to_json(self, csv_file_path: str, json_file_path: str):
        data = []
        
        with open(csv_file_path, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)
        
        with open(json_file_path, mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        
        print(f"CSV convertido a JSON y guardado en {json_file_path}")

    def json_to_csv(self, json_file_path: str, csv_file_path: str):
        with open(json_file_path, mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        
        headers = data[0].keys()
        
        with open(csv_file_path, mode='w', encoding='utf-8', newline='') as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerows(data)
        
        print(f"JSON convertido a CSV y guardado en {csv_file_path}")

converter = FileConverter()
csv_file = "datos.csv"
json_file = "datos.json"

converter.csv_to_json(csv_file, json_file)

converter.json_to_csv(json_file, csv_file)
