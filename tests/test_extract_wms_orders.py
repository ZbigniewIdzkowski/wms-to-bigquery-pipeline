from extract_wms_orders import extract_orders_from_csv

def test_extract_orders_from_csv():
    data = extract_orders_from_csv("sample_orders.csv")
    assert isinstance(data, list)
    assert len(data) == 3
    assert data[0]["order_id"] == "A123"
    assert data[1]["qty"] == 5
