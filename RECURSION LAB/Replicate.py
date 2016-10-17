def replicate_iter(number_of_times, inputs):
    if((not isinstance(number_of_times, int)) or (not isinstance(inputs, (int, float, str)))):
            raise ValueError("Invalid arguments passed")
    elif(number_of_times <= 0):
            return []
    else:
            array = []
            for x in range(number_of_times):
                    array.append(inputs)
            return array


def replicate_recur(number_of_times, inputs):
    if((not isinstance(number_of_times, int)) or (not isinstance(inputs, (int, float, str)))):
            raise ValueError("Invalid arguments passed")
    elif(number_of_times <= 0):
            return []
    else:
            return ([inputs] + replicate_recur((number_of_times - 1), inputs)) 