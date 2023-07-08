## 工厂模式
### 工厂方法

import json
import xml.etree.ElementTree as etree


class JSONConnector():

    def __init__(self, filepath) -> None:
        self.data = dict()
        with open(filepath, mode="r", encoding="utf-8") as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data
    
class XMLConnector:

    def __init__(self, filepath) -> None:
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree
    
def connector_factory(filepath):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError("cannot connect to {}".format(filepath))
    
    return connector

def connect_to(filepath):
    factory = None
    try:
        factory = connector_factory(filepath=filepath)
    except ValueError as e:
        print(e)

    return factory


def main():
    sqlite_factory = connect_to("./test.sq3")
    print(sqlite_factory)


main()