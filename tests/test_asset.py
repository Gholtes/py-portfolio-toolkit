import pandas as pd

from context import py_portfolio_opt

def test_asset_attributes():
    aa = py_portfolio_opt.core.AssetAttributes()
    # Check defaults
    assert(aa.get_attribute("industry")=="unspecified")
    # check setter and getter behavior
    aa.set_attribute("industry", "Finance")
    assert(aa.get_attribute("industry")=="Finance")
    # Check what core attributes exist
    core_attr = aa.list_core_attributes()
    for key in ["industry", "asset_class", "country", "region", "liquidity"]:
        assert(key in core_attr)

    # check custom attributes
    aa.set_attribute("custom_1", "abc")
    assert(aa.get_attribute("custom_1")=="abc")
    custom_attr = aa.list_custom_attributes()
    for key in ["custom_1"]:
        assert(key in custom_attr)

    # check all attr method
    attr = aa.list_attributes()
    for key in ["custom_1", "industry"]:
        assert(key in attr)

def test_asset():
    a = py_portfolio_opt.core.Asset("A1")
    assert(a.id == "A1")
    # Check that the asset has no history or assumptions
    assert(a.returns.is_valid == False)
    assert(a.assumptions.is_valid == False)
    # Add a return dataset
    a.returns.set_returns(pd.Series([1,2,3]))
    assert(a.returns.is_valid == True)
    assert(a.returns.returns.iloc[0] == 1)
    # Add assumptions
    a.assumptions.set_assumptions(1,2)
    assert(a.assumptions.return_assumption == 1)
    assert(a.assumptions.volitility_assumption == 2)
    # Add attribute
    a.attributes.set_attribute("asset_class", "equity")
    assert(a.attributes.get_attribute("asset_class")=="equity")

if __name__ == "__main__":
    test_asset_attributes()
    test_asset()