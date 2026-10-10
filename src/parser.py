import json
from pathlib import *
#path = Path("../config.json ")
#print(path.exists())

def parser(path):
    path = Path(path)
    if not path.exists():
        raise Exception("specified path does not exist.")
    if not path.is_file():
        raise Exception("specified path is not a file.")
    
    try: 
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            print(data["targets"])
    except json.JSONDecodeError:
        raise Exception("file is not a json file.")
    except Exception as e:
        raise Exception(f"an error: {e} occured. ")
    
parser("../main.py")