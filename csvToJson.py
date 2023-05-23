import csv
import json

jsonFilePath = 'mental_health_faq.json'
intents = []

with open('mental_health_faq.csv', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        tag = row['Question_ID']
        pattern = row['Questions']
        response = row['Answers']

        intent = {
            'tag': tag,
            'patterns': pattern,
            'responses': response
        }

        intents.append(intent)

data = {'intents': intents}

with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(data, ensure_ascii=False, indent=4))
