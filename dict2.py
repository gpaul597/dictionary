from typing import Dict


Dict = {}
print("Empty Dictionary: ")
print(Dict)

Dict[0] = 'Geeks'
Dict[2] = 'For'
Dict[3] = '1'
print("\nDictionary after adding 3 elements:")
print(Dict)

Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 element: ")
print(Dict)

Dict[2] = 'welcome'
print("\nUpdated key value: ")
print(Dict)

Dict[5] = {'Nested' :{'1' : 'life', '2': 'Geeks'}}
print("\nAdding a nested key: ")
print(Dict)
