import json
from pingwatch.enums import Status
from pingwatch.checks import Target
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
            return data
    except json.JSONDecodeError:
        raise Exception("file is not a json file.")
    except Exception as e:
        raise Exception(f"an error: {e} occured. ")
    
def target_handler(path):
    data = config_handler(path)
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

            
def info_builder(targets):
    if len(targets) <= 0:
        return 
    for target in targets:
        target.status_check()
        status = ""
        match target.status:
            case Status.SUCCESS:
                status = "UP"
            case Status.DEAD:
                status = "DOWN"
            case Status.BAD:
                status = "BAD REQUEST"
            case _:
                status = "Unknown request, can you firgure out why? XD"
                
        
        print(f"Name: {target.name}, Status: {status}  HTTP-Code:{target.http_code}, Time:{target.time}")
               
#try:
#    info_builder((target_handler("../config.json")))
#except Exception as e:
#    print(f"Fudge! {e} ")
    
    