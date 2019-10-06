from copy import deepcopy


def courses_to_take(course_to_pre_reqs):
    if not course_to_pre_reqs:
        return []
    for course in course_to_pre_reqs:
        ret = list()
        if not course_to_pre_reqs[course]:
            print(course_to_pre_reqs)
            ret.append(course)
            next_pre_reqs = deepcopy(course_to_pre_reqs)
            del next_pre_reqs[course]
            if not next_pre_reqs:
                return ret
            for c in next_pre_reqs:
                if course in next_pre_reqs[c]:
                    next_pre_reqs[c].remove(course)
            extra = courses_to_take(next_pre_reqs)
            if extra is not None:
                return ret + extra
    return None


def main():
    courses = {
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': []
    }
    assert courses_to_take(courses) == ['CSC100', 'CSC200', 'CSC300']
    prereqs = {
        'CSC400': ['CSC200'],
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': []
    }
    assert courses_to_take(prereqs) == ['CSC100', 'CSC200', 'CSC400', 'CSC300']
    prereqs = {
        'CSC400': ['CSC300'],
        'CSC300': ['CSC100', 'CSC200'],
        'CSC200': ['CSC100'],
        'CSC100': ['CSC400']
    }
    assert not courses_to_take(prereqs)


if __name__ == '__main__':
    main()
