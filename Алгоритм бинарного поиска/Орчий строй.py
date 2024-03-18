from typing import List, Set, Dict


def count_max_values(orc_growth: List[str], orc_growth_dict_on_left: Dict[str, int], expected_growth_set: Set[str],
                     len_orc_growth: int, orc_growth_dict: Dict[str, int]) -> Dict[str, int]:
    maxim: Dict[str, int] = dict()

    for exp_height in expected_growth_set:
        maxim[exp_height] = 0

    for position in range(1, len(orc_growth) + 1):
        height = orc_growth[position - 1]
        orc_growth_dict_on_left[height] += 1
        if height in expected_growth_set:
            cur_value = orc_growth_dict_on_left[height] * (
                    len_orc_growth - position - (orc_growth_dict[height] - orc_growth_dict_on_left[height]))
            maxim[height] = max(maxim[height], cur_value)

    return maxim


def find_max_value_of_function(orc_growth: List[str], expected_growth_set: Set[str], len_orc_growth: int) -> (
        Dict)[str, int]:
    orc_growth_dict: Dict[str, int] = dict()
    orc_growth_dict_on_left: Dict[str, int] = dict()

    for height in orc_growth:
        if height not in orc_growth_dict:
            orc_growth_dict[height] = 1
            orc_growth_dict_on_left[height] = 0
        else:
            orc_growth_dict[height] += 1

    maxim = count_max_values(orc_growth, orc_growth_dict_on_left, expected_growth_set, len_orc_growth, orc_growth_dict)

    return maxim


def main():
    orc_growth = input().split()
    expected_growth = input().split()
    expected_growth_set = set(expected_growth)
    len_orc_growth = len(orc_growth)

    maxim = find_max_value_of_function(orc_growth, expected_growth_set, len_orc_growth)
    result = [str(maxim[exp_height]) for exp_height in expected_growth]

    print(" ".join(result))


if __name__ == '__main__':
    main()
