from copy import deepcopy

def courses_to_take(course_to_prereqs):
    if not course_to_prereqs:
        return []
    for course in course_to_prereqs:
        ret = list()
        if not course_to_prereqs[course]:
            print(course_to_prereqs)
            ret.append(course)
            nextprereqs = deepcopy(course_to_prereqs)
            del nextprereqs[course]
            if not nextprereqs:
                return ret
            for c in nextprereqs:
                if course in nextprereqs[c]:
                    nextprereqs[c].remove(course)
            extra = courses_to_take(nextprereqs)
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
