import pandas as pd

class Asset:
    def __init__(self, asset_id):
        self.id = asset_id
        self.attributes = AssetAttributes()
        self.returns_history = AssetReturnTimeSeries()
        self.assumptions = AssetAssumptions()
        pass

class AssetAttributes:
    def __init__(self):
        # Core attributes and their default values
        self.core_attribute_keys = ["industry", "asset_class", "country", "region", "liquidity"]
        default_value_str = "unspecified"
        self.industry = default_value_str
        self.asset_class = default_value_str
        self.country = default_value_str
        self.region = default_value_str
        self.liquidity = 1 # Assume 100% liquid
        # Custom attributes
        self.custom_attributes = {}
    
    def set_attribute(self, name, value):
        if name in self.__dict__:
            self.__dict__[name] = value
        else:
            self.custom_attributes[name] = value

    def get_attribute(self, name):
        if name in self.__dict__:
            return self.__dict__[name]
        elif name in self.custom_attributes:
            return self.custom_attributes[name]
        
    def list_core_attributes(self):
        return self.core_attribute_keys
    
    def list_custom_attributes(self):
        return list(self.custom_attributes.keys())
    
    def list_attributes(self):
        attr = self.list_core_attributes()
        attr.extend(self.list_custom_attributes())
        return attr

class AssetReturnTimeSeries:
    def __init__(self):
        self.returns = None
        self.is_valid = False
    
    def set_returns(self, returns_history: pd.Series):
        self.returns = returns_history
        self.is_valid = True

class AssetAssumptions:
    def __init__(self):
        self.return_assumption = None
        self.volitility_assumption = None
        self.is_valid = False
    
    def set_assumptions(self, return_value: float, volitility_value: float):
        self.return_assumption = return_value
        self.volitility_assumption = volitility_value
        self.is_valid = True
    
    def get_assumptions(self):
        return self.return_assumption, self.volitility_assumption
