from time import sleep

def test_downpayment(setup, teardown):
    setup.find_element_by_id("cdownpayment").clear()
    setup.find_element_by_id("cdownpayment").send_keys(40)
    sleep(5)

def test_downpayment_2(setup, teardown):
    setup.find_element_by_id("cdownpayment").clear()
    setup.find_element_by_id("cdownpayment").send_keys(40)
    sleep(5)
