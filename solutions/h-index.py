from collections import defaultdict


def nlogn_h_index(publications):
    publications.sort(reverse=True)
    """
        Sort publications and reverse the list->first index = max value-> no publications with more citations than 
        the publication at that index.
        If the index+1 is larger or equal to the number of citations a publication has at that index-> there are 
        a larger or equal number of publications with that number of citations.
    """
    formatted_publications = [min(index + 1, value) for index, value in enumerate(publications)]
    return max(formatted_publications)


def n_h_index(publications):
    publications_dict = {x: 0 for x in range(1, len(publications) + 1)}
    for index, value in enumerate(publications):
        if value > len(publications):
            publications_dict[len(publications)] += 1
        else:
            publications_dict[value] += 1
    total_publications = 0
    """
        Iterating from back to front of publication dictionary, dictionary ranges from 1 to number of publications given
        as the maximum h-value is the number of publications provided. If the h-value is larger than the number 
        of publications that means there is that many publications that have citations equal to or larger than that     
        value which is impossible as there aren't that many publications given in the first place

        -> Each index in the dictionary contains the number of publications with equal to or more of that indexes value 
        of citations.  We create a running total of publications->once the running total is equal to or larger than the 
        index we are currently on, that means there are equal to or larger number of publications that have that indexes
        number of citations. This is then the maximum h-value. 
    """
    for index in range(publications, 0, -1):
        total_publications += publications_dict[index]
        if total_publications >= index:
            return index
    return 0


def main():
    assert nlogn_h_index([1, 0, 3, 3, 5]) == 3
    assert n_h_index([1, 0, 3, 3, 5]) == 3


if __name__ == '__main__':
    main()