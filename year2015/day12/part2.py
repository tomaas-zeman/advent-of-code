import json

def run(data: list[str], is_test: bool):
    obj = json.loads(data[0])

    def recs(obj):
        if isinstance(obj, int):
            return obj
        elif isinstance(obj, list):
            return sum(map(recs, obj))
        elif isinstance(obj, dict):
            if "red" in obj.values():
                return 0
            return sum(map(recs, obj.values()))
        else:
            return 0
    
    return recs(obj)
