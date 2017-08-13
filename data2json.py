import json

if __name__ == '__main__':
    data = {
        'level1': []
    }
    with open('data.txt') as in_f:
        for line in in_f:
            line_list = list(line)
            data['level1'].append(line_list)
    with open('data.json', 'w') as data_json:
        json.dump(data, data_json, indent=2)