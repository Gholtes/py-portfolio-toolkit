import pandas as pd

from context import py_portfolio_opt

def test_portfolio():
    # create a new portfolio
    p = py_portfolio_opt.core.Portfolio()
    # Create a snapshots
    s1 = py_portfolio_opt.core.PortfolioSnapshot({"A1":0.5, "A2":0.5})
    p.add_snapshot(s1, pd.to_datetime("1/1/2023"))

    s2 = py_portfolio_opt.core.PortfolioSnapshot({"A1":0.1, "A2":0.9})
    p.add_snapshot(s2, pd.to_datetime("1/6/2023"))
    # weights on a date should be as at that date
    w1 = p.get_weights(pd.to_datetime("1/1/2023"))
    assert[w1["A1"]==0.5]
    # Weights before the first snapshot are the first snapshot's
    w1 = p.get_weights(pd.to_datetime("1/12/2022"))
    assert[w1["A1"]==0.5]
    # weights between dates should be the last valid data
    w1 = p.get_weights(pd.to_datetime("1/4/2023"))
    assert[w1["A1"]==0.5]
    # no date should yield latest data
    w1 = p.get_weights()
    assert[w1["A1"]==0.1]

def test_from_csv():
    path = "tests/files/portfolio_weights.csv"
    p = py_portfolio_opt.core.Portfolio()
    p.from_csv(path)
    # Test load
    w1 = p.get_weights(pd.to_datetime("1/6/2023"))
    assert[w1["A1"]==0.4]

if __name__ == "__main__":
    test_portfolio()
    test_from_csv()