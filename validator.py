import json
import os

__path__=os.path.dirname(__file__)
def validator(example, target):
    def load_json(json_object,type):
        try:
            print(os.path.join(__path__,json_object))
            with open(os.path.join(__path__,json_object)) as f:
                return json.loads(f.read())
                
        except Exception as e:
            print(f'Your {type} does not load')
            raise e

    example_json= load_json(example,'Example')
    target_json= load_json(target,'Target')
    issues=[]
    for k,v in example_json.items():
        if k not in target_json.keys():
            issues.append(f'Key Error, {k} not found in {target}')
            break
        if type(target_json[k])!=type(v):
            issues.append(f'Value Error, {k} data type ({type(target_json[k]).__name__}) does not match expected datatype of {type(v).__name__}')
    print(issues)
    if issues:
        raise Exception(f'Issues were found {issues}')
if __name__=='__main__':
    print('Hello')
    validator('example.json','target.json')