# Helper class to process data from csv's

import csv
import PackageInfo
import HashTable


def generate_package_hash():
    """
    First pull information from CSV, make packages, from the packages, load into hashtable
    :return pkg_ht:
    Space Complexity: O(N)
    Time Complexity: O(N)
    """
    pkg_array = []
    with open('.\\src\\WGUPS Package File.csv') as pkg_csv_file:
        pkg_csv_reader = csv.reader(pkg_csv_file)
        for row in pkg_csv_reader:
            pkg = PackageInfo.Package(row)
            pkg_array.append((pkg.get_key(), pkg))
        pkg_ht = HashTable.HashTable(pkg_array)
        return pkg_ht


def load_distance_file():
    """
    Load csv into a list to use distance values for later.
    :return dist_array:
    Space Complexity: O(N)
    Time Complexity: O(N)
    """
    dist_array = []
    with open('.\\src\\WGUPS Distance Table.csv') as dist_csv_file:
        dist_csv_reader = csv.reader(dist_csv_file)
        for row in dist_csv_reader:
            dist_array.append(row)
        return dist_array


def get_distance(distance_list: [], index1: int, index2: int):
    """
    Function determines the distance from index1 to index2 in distance_list loaded earlier.
    :param distance_list:
    :param index1:
    :param index2:
    :return processed_distance_list[index2]:

    Space Complexity: O(N)
    Time Complexity: O(N)
    """
    processed_distance_list = list(distance_list[index1][2:-1])

    processed_distance_list.append(0.0)

    for next_location in range(index1 + 1, len(distance_list)):
        processed_distance_list.append(distance_list[next_location][index1 + 2])
    processed_distance_list = list(map(float, processed_distance_list))
    return processed_distance_list[index2]


def match_pkg_to_distance(distance_list: [], pkg_hash, pkg_key: int):
    """
    Method takes a packages key and finds out on the data from the distance_list which index it corresponds to.
    Sets up to be able to calculate distance in get_distance() method.
    :param distance_list:
    :param pkg_hash:
    :param pkg_key:
    :return distance_index:
    Space Complexity: O(N)
    Time Complexity: O(N)
    """
    distance_index = 0
    for distance in distance_list:
        if pkg_hash.get(pkg_key).get_address() == distance[1][:-8]:
            distance_index = distance_list.index(distance)
            break
    return distance_index
