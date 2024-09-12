import json

class Data:
    def get_test_data(self):
        res = {'nombre':'Juan Pérez'}
        return json.dumps(res)