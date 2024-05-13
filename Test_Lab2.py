import Lab2

def test_find_min_max():
    user_input = [23, 56, 73, 90, 12, 35, 83, 52, 61]
    all_temps = [float(num) for num in user_input]

    test_min_max = [12, 90]

    min_max = Lab2.find_min_max(all_temps)

    assert (test_min_max == min_max)

def test_calc_average():
    user_input = [23, 56, 73, 90, 12, 35, 83, 52, 61]
    all_temps = [float(num) for num in user_input]
    arr_len = len(user_input)
    
    test_average_temp = sum(user_input) / arr_len

    average_temp = Lab2.calc_average(all_temps)

    assert (test_average_temp == average_temp)

def test_find_median():
    user_input = [23, 56, 73, 90, 12, 35, 83, 52, 61]
    all_temps = [float(num) for num in sorted(user_input)]

    test_median_temp = 56.0

    median_temp = Lab2.find_median(all_temps)

    assert (test_median_temp == median_temp)
