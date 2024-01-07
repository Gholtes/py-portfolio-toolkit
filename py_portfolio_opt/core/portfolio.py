import pandas as pd

class Portfolio:
    def __init__(self):
        self.weights_raw = {} # Dict of timestamp: PortfolioSnapshot, as input
        pass

    def get_weights(self, date=None):
        dates = list(self.weights_raw.keys())
        if date == None:
            # use latest
            date = max(dates)
            data_date = date # Key in weights_raw
        else:
            # find latest date in weights_raw that is <= date
            # TODO: A binary search would be faster here...
            data_date = min(dates) # in case that date < min date, we want to assume that the first allocation is valid
            for d in dates:
                if d <= date:
                    data_date = d
                else:
                    break
        return self.weights_raw[data_date].weights
    
    def add_snapshot(self, snapshot, date, override=False):
        if date in self.weights_raw and not override:
            raise KeyError(f"Date {date} already has a snapshot, set override to True to override existing data")
        self.weights_raw[date] = snapshot

    # Loaders

    def from_csv(self, path, mode="wide"):
        if mode == "wide":
            df = pd.read_csv(path, parse_dates=True, index_col=0)
            for date, weights in df.iterrows():
                snapshot = PortfolioSnapshot(weights.to_dict())
                self.add_snapshot(snapshot, date)
        else: 
            raise ValueError(f"Mode should be one of ['wide']")
        


class PortfolioSnapshot:
    def __init__(self, weights):
        sum_weights = sum([v for v in weights.values()])
        if sum_weights != 1:
            raise ValueError(f"Sum of weights is {sum_weights}, it should be 1")
        self.weights = weights # dict of AssetID: Weight

def create_composite_portfolio(portfolios: [Portfolio], weights: [float]) -> Portfolio:
    # we need to combine the weights_raw from each portfolio by weight, at every timestep
    # This assumes static weights oveer time.
    return Portfolio()