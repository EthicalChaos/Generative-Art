import yaml

class Entity(yaml.YAMLObject):
    yaml_tag = u'!Layer'

    def __init__(self, layer, required):
        self.layer = layer
        self.required = required
    
    def __repr__(self) -> str:
        return f"Layer type: {self.layer}, required: {self.required}"
        

