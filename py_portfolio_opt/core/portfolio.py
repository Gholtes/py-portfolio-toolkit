import pandas as pd

class Portfolio:
    def __init__(self):
        self.weights_raw = {} # Dict of timestamp: PortfolioSnapshot, as input
        pass

    def get_weights(date=None) -> PortfolioSnapshot:
        dates = list(self.weights_raw.keys())
        if date == None:
            # use latest
            date = max(dates)
            data_date = date # Key in weights_raw
        else:
            # find latest date in weights_raw that is <= date
            # TODO: A binary search would be faster here...
            for d in dates:
                if d <= date:
                    data_date = d
                else:
                    break
        return self.weights_raw[data_date]


class PortfolioSnapshot:
    def __init__(self):
        weights = {} # dict of AssetID: Weight


def create_composite_portfolio(portfolios: [Portfolio], weights: [float]) -> Portfolio:
    # we need to combine the weights_raw from each portfolio by weight, at every timestep
    # This assumes static weights oveer time.
    return Portfolio()