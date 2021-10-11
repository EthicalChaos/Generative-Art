import yaml
import os

class Layer(yaml.YAMLObject):
    yaml_tag = u'!Layer'

    def __init__(self, layer, required):
        self.layer = layer
        self.required = required
        self.path =  os.path.join('assets/', layer)
        self.variations = sorted([variation for variation in os.listdir(self.path)])

        if required is False:
            self.variations = [None] + self.variations
    
    def __repr__(self) -> str:
        return f"Layer type: {self.layer}, required: {self.required}, type{type(self.required)}"
        

