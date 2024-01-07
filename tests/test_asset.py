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



if __name__ == "__main__":
    test_asset_attributes()