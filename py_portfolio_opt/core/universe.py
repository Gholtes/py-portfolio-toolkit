

class Universe:
    def __init__(self, name: str):
        self.assets = {} #TODO: Should Universe store assets or just the ID?
        self.name = name

    def add_asset(self, asset):
        if asset.id in self.assets:
            raise ValueError(f"Asset with id {asset.id} already exists in the universe")
        self.assets[asset.id] = asset