from time import sleep

def test_loan_term(setup, teardown):
    setup.find_element_by_id("cloanterm").clear()
    setup.find_element_by_id("cloanterm").send_keys(40)
    sleep(5)


def test_loan_term_2(setup, teardown):
    setup.find_element_by_id("cloanterm").clear()
    setup.find_element_by_id("cloanterm").send_keys(40)
    sleep(5)