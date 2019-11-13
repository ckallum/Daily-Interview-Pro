def flatten_dictionary(d):
    result_dict = {}
    helper(d, "", result_dict)
    return result_dict


def helper(current_dict, current, results):
    for k, v in current_dict.items():
        if type(v) == dict:
            helper(v, current + k + ".", results)
        else:
            results[current + k] = v


def main():
    d = {
        'a': 1,
        'b': {
            'c': 2,
            'd': {
                'e': 3
            }
        }
    }
    assert (flatten_dictionary(d)) == {'a': 1, 'b.c': 2, 'b.d.e': 3}


if __name__ == '__main__':
    main()
