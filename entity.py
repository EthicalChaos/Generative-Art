import yaml


class Entity(yaml.YAMLObject):
    yaml_tag = u'!Entity'

    def __init__(self, entity, required):
        self.entity = entity
        self.required = required
    
    def __repr__(self) -> str:
        return f"Entity type: {self.entity}, required: {self.required}"
        

