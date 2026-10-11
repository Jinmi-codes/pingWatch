import json

from checks import Target
from pathlib import *
#path = Path("../config.json ")
#print(path.exists())

def config_handler(path):
    path = Path(path)
    if not path.exists():
        raise Exception("specified path does not exist.")
    if not path.is_file():
        raise Exception("specified path is not a file.")
    
    try: 
        with open(path, 'r') as json_file:
            data = json.load(json_file)
            return target_handler(data)
    except json.JSONDecodeError:
        raise Exception("file is not a json file.")
    except Exception as e:
        raise Exception(f"an error: {e} occured. ")
    
def target_handler(data):
    valid_targets = []
    if not "targets" in data:
        raise Exception("config error. Targets weren't specified.")
    targets = data["targets"]
    for target in targets:
        if not "name" in target:
            print("A Name is required for a valid target. An entry was skipped.")
            continue
        if not "url" in target:
            print("A URL is required for a valid target. An entry was skipped.")
            continue
        valid_targets.append(Target(name=target["name"], url=target["url"]))
            
    return valid_targets

            
            
               
    
config_handler("../config.json")