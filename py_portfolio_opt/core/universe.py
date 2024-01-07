
class Universe:
    def __init__(self, name: str):
        self.assets = {} #TODO: Should Universe store assets or just the ID?
        self.name = name

    def add_asset(self, asset):
        if asset.id in self.assets:
            raise ValueError(f"Asset with id {asset.id} already exists in the universe")
        self.assets[asset.id] = asset

    def has_member(self, asset_id):
        return asset_id in self.assets
    
    def list_assets(self):
        return list(self.assets.keys())
    
    # Loaders

    def from_csv(self, path):
        # Need to think about the CSV structure here, as it needs to hold some / all of:
        # Attributes
        # Assumptions
        # Returns
        # Maybe need to have seperate loaders for each?
