import os
import random

import yaml


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

    def variation_count(self):
        return len(self.variations)
    
    def get_random_varation(self):
        random_index = random.randint(0, self.variation_count()-1)
        return os.path.join(self.path, self.variations[random_index])

