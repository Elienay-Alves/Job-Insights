#from src.pre_built.counter import count_ocurrences


def test_counter():
   'return the ammount of ocurrencies of words'
    result = count_ocurrences('data/jobs.csv', 'python')
    assert result == 1639