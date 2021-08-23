import PackageInfo as Pkg
import Utils


class PackageSorter:
    def __init__(self, distance_values: [], pkg_hash):
        self.distance_values = distance_values
        self.pkg_hash = pkg_hash

    def sort_packages(self, pkgs_to_be_delivered):
        """
        Method takes in a list of all packages left to be delivered and sorts into lists with deadlines and without.
        It further decides if packages need to be pre-loaded for their route based on constraint priority. If no packages
        are on high priority, the method changes to take in and factor further packages into routes based on shortest path
        needed to take to deliver all packages. Each time run, the method returns temporary routes with a package list to
        give to the trucks to deliver. List of all packages is updated each time.
        :param pkgs_to_be_delivered:
        :return temp_route1, temp_route2:

        Space Complexity: O(N)
        Time Complexity: O(N^2)
        """
        # Sort will cherry pick packages by constraints manually and load first time around, otherwise nearest neighbour
        pkgs_with_dd = []
        pkgs_without_dd = []
        temp_route1 = []
        temp_route2 = []
        # packages are pre-loaded based off Deadline Delivery first, packages are decided in order based on same location
        # prevents unnecessary backtracking to deliver to an address that has already been visited
        pre_load_temp_route1 = [15, 16, 34, 14, 19, 20, 21, 31, 32, 13, 39, 8, 30, 4, 40, 1]
        pre_load_temp_route2 = [25, 26, 6, 7, 29, 5, 37, 38]

        # creating lists for packages with and without delivery deadlines
        """
        Space Complexity: O(N)
        Time Complexity: O(N)
        """
        for pkg in pkgs_to_be_delivered:
            if pkg.get_deadline() != "EOD":
                pkgs_with_dd.append(pkg)
            else:
                pkgs_without_dd.append(pkg)

        """
        ***REQUIREMENT A***
        Main Adjusting part of algorithm is based on if there are priority packages still left to deliver. If all are accounted for
        continue to just decide what is the most efficient path by distance. Greedy Algorithm as we are assuming deadline is the most important
        constraint to decide what to change for.

        From lines 51 to 131
        Space Complexity: O(N)
        Time Complexity: O(N^2)
        """
        if len(pkgs_with_dd) > 0:
            # preloading trucks 1 and 2 with packages based on constraints and bundled to optimize for location
            # assigns pre-loaded routes manually to temporary routes, route 2 still needs to have more packages before leaving
            # truck 2 has delayed packages and will not leave until 9:05
            for pre_load_1 in pre_load_temp_route1:
                temp_route1.append(self.pkg_hash.get(pre_load_1 - 1))

            for pre_load_2 in pre_load_temp_route2:
                temp_route2.append(self.pkg_hash.get(pre_load_2 - 1))

            # remove from pkgs with and without dd lists to update
            for temp_pkg in temp_route1:
                if temp_pkg in pkgs_without_dd:
                    pkgs_without_dd.remove(temp_pkg)
                else:
                    pkgs_with_dd.remove(temp_pkg)
            for temp_pkg2 in temp_route2:
                if temp_pkg2 in pkgs_with_dd:
                    pkgs_with_dd.remove(temp_pkg2)
                else:
                    pkgs_without_dd.remove(temp_pkg2)

            # have to make a temporary list to sort next closest packages by distance to last package already in temp route
            # for truck 2, remove package 9 for now so it will get updated later
            for pkg_without_dd_check in pkgs_without_dd:
                if pkg_without_dd_check.get_pkg_id() == '9':
                    pkgs_without_dd.remove(pkg_without_dd_check)

            pkgs_without_dd_sort = []
            pkgs_without_dd_sort += pkgs_without_dd
            pkgs_without_dd_sort.insert(0, temp_route2[-1])

            """
            ***REQUIREMENT A***
            Implementation of a Nearest Neighbour Algorithm by determining which location is closest with a package. Decides
            to make the closest location the next destination to visit. 
            """
            # selection sort to decide what is the optimal path based on distance for order of packages to be delivered
            for pkg_index in range(len(pkgs_without_dd_sort) - 1):
                # start at index 0 and compare to every index after
                smallest_distance = 99
                smallest_distance_pkg = None
                pkg_index_key = pkgs_without_dd_sort[pkg_index].get_key()
                pkg_index_location = Utils.match_pkg_to_distance(self.distance_values, self.pkg_hash, pkg_index_key)

                for pkg_next_index in range(pkg_index + 1, len(pkgs_without_dd_sort)):

                    # match location to pkg in pkgs_without_dd
                    pkg_next_index_key = pkgs_without_dd_sort[pkg_next_index].get_key()
                    pkg_next_index_location = Utils.match_pkg_to_distance(self.distance_values, self.pkg_hash,
                                                                          pkg_next_index_key)
                    # plug distances into get_distance
                    get_distance_result = Utils.get_distance(self.distance_values, pkg_index_location,
                                                             pkg_next_index_location)
                    # find minimum from distance
                    if get_distance_result < smallest_distance:
                        smallest_distance = get_distance_result
                        smallest_distance_pkg = pkg_next_index
                pkgs_without_dd_sort[pkg_index + 1], pkgs_without_dd_sort[smallest_distance_pkg] = pkgs_without_dd_sort[smallest_distance_pkg], pkgs_without_dd_sort[pkg_index + 1]

            # adding sorted by distance packages remaining to temp_route 2 to fill up truck2
            for y in range(1, len(pkgs_without_dd_sort)):
                if len(temp_route2) < 16:
                    temp_route2.append(pkgs_without_dd_sort[y])

            # update list based off of what packages are remaining for next pickup/delivery
            for pkg_cleanup in temp_route2:
                if pkg_cleanup in pkgs_without_dd:
                    pkgs_without_dd.remove(pkg_cleanup)

            # remove packages on truck routes accounted for from pkgs_to_be_delivered list
            for pkg_remove_route1 in temp_route1:
                if pkg_remove_route1 in pkgs_to_be_delivered:
                    pkgs_to_be_delivered.remove(pkg_remove_route1)
            for pkg_remove_route2 in temp_route2:
                if pkg_remove_route2 in pkgs_to_be_delivered:
                    pkgs_to_be_delivered.remove(pkg_remove_route2)
            # return temp_routes
            return temp_route1, temp_route2

        # no priority packages left, continue

        else:
            """
            From lines 133 to 
            Space Complexity: O(N)
            Time Complexity: O(N^2)
            """
            # update package #9 because by this time the address should be corrected
            pkg_9 = self.pkg_hash.get(8)
            pkg_9.set_address("410 S State St")
            pkg_9.set_city("Salt Lake City")
            pkg_9.set_state("UT")
            pkg_9.set_zip("84111")

            # create dummy package for hub separate from hash table to add to list to sort
            hub_dummy_package = Pkg.Package(['99', 'HUB', 'Salt Lake City', 'UT', '84107', 'EOD', '0'])

            # have to make a temporary list to sort next closest packages by distance to hub
            # for truck 2
            pkgs_without_dd_sort = [hub_dummy_package]
            pkgs_without_dd_sort += pkgs_without_dd

            """
            ***REQUIREMENT A***
            Implementation of a Nearest Neighbour Algorithm by determining which location is closest with a package. Decides
            to make the closest location the next destination to visit. 
            """
            # determine closest route from hub with current list of packages
            for pkg_index in range(len(pkgs_without_dd_sort) - 1):
                # start at index and compare to every index after

                smallest_distance = 99
                smallest_distance_pkg = None
                if pkg_index == 0:
                    pkg_index_location = 0
                else:
                    pkg_index_key = pkgs_without_dd_sort[pkg_index].get_key()
                    pkg_index_location = Utils.match_pkg_to_distance(self.distance_values, self.pkg_hash, pkg_index_key)

                for pkg_next_index in range(pkg_index + 1, len(pkgs_without_dd_sort)):

                    # match location to pkg in pkgs_without_dd
                    pkg_next_index_key = pkgs_without_dd_sort[pkg_next_index].get_key()
                    pkg_next_index_location = Utils.match_pkg_to_distance(self.distance_values, self.pkg_hash,
                                                                          pkg_next_index_key)
                    # plug distances into get_distance
                    get_distance_result = Utils.get_distance(self.distance_values, pkg_index_location,
                                                             pkg_next_index_location)
                    # find minimum from distance
                    if get_distance_result < smallest_distance:
                        smallest_distance = get_distance_result
                        smallest_distance_pkg = pkg_next_index
                pkgs_without_dd_sort[pkg_index + 1], pkgs_without_dd_sort[smallest_distance_pkg] = pkgs_without_dd_sort[smallest_distance_pkg], pkgs_without_dd_sort[pkg_index + 1]

            # fill up route until length of route is 16
            for y in range(1, len(pkgs_without_dd_sort)):
                if len(temp_route2) < 16:
                    temp_route2.append(pkgs_without_dd_sort[y])

            # remove from pkgs_without_dd if in route 2, updating packages that are left
            for pkg_cleanup in temp_route2:
                if pkg_cleanup in pkgs_without_dd:
                    pkgs_without_dd.remove(pkg_cleanup)

            # remove from main package list : pkgs_to_be_delivered, updating packages that are left
            for pkg_remove_route2 in temp_route2:
                if pkg_remove_route2 in pkgs_to_be_delivered:
                    pkgs_to_be_delivered.remove(pkg_remove_route2)

            # return temp_routes
            return temp_route1, temp_route2

    def load_trucks(self, pkgs_to_be_delivered, truck1, truck2):
        """
        Method returns nothing, but sets both trucks' routes to be routes that were determined in the main sort.
        :param pkgs_to_be_delivered:
        :param truck1:
        :param truck2:
        :return:

        Space Complexity: O(N)
        Time Complexity: O(N^2)
        calls method that has a Time Complexity of O(N^2)
        """
        # sort packages to load up trucks
        truck1_route, truck2_route = self.sort_packages(pkgs_to_be_delivered)
        # set routes of truck objects to returns from sort method
        print()
        print("Loading trucks...")
        truck1.route = truck1_route
        truck2.route = truck2_route
        # set all statuses of packages in truck routes to on route
        truck1.update_load_time_on_packages()
        truck2.update_load_time_on_packages()

    def deliver_packages(self, truck):
        """
        Method creates a route list that uses hub as starting and end point. Determines distance from one point to the next,
        delivering packages and updating their status while keeping track of the distance for current truck and its total mileage.
        :param truck:
        :return total_mileage_route:
        Space Complexity: O(N)
        Time Complexity: O(N^2)
        In loop, calls helper method which also loops.
        """
        hub_index = 0
        total_mileage_route = 0

        # calling matching method from helper class to figure out where on the distance table the address for the package is
        beginning_index_route = Utils.match_pkg_to_distance(self.distance_values, self.pkg_hash, truck.route[0].get_key())
        end_index_route = Utils.match_pkg_to_distance(self.distance_values, self.pkg_hash, truck.route[-1].get_key())
        # calling distance method from helper class to determine distance between 2 locations
        starting_distance_route = Utils.get_distance(self.distance_values, hub_index, beginning_index_route)
        ending_distance_route = Utils.get_distance(self.distance_values, end_index_route, hub_index)

        total_mileage_route += starting_distance_route
        """
        Following loop gets distance between first and second package in route, sets first package in route to delivered,
        then pops off the first item from route.
        """
        for pkg_index in range(len(truck.route) - 1):
            temp_index1_route = Utils.match_pkg_to_distance(self.distance_values, self.pkg_hash, truck.route[0].get_key())
            temp_index2_route = Utils.match_pkg_to_distance(self.distance_values, self.pkg_hash, truck.route[1].get_key())
            current_distance_route1 = Utils.get_distance(self.distance_values, temp_index1_route, temp_index2_route)

            float_time = total_mileage_route / truck.speed
            truck.route[0].update_time_delivered(float_time)

            total_mileage_route += current_distance_route1
            truck.route[0].set_status("Delivered")
            truck.route.pop(0)
        # update time delivered for last package in route
        float_time = total_mileage_route / truck.speed
        truck.route[0].update_time_delivered(float_time)
        # pop last package off
        truck.route.pop(0)
        total_mileage_route += ending_distance_route

        return total_mileage_route

    def run_simulation(self, truck1, truck2):
        # empty lists for list of all packages, then ones to be distributed to routes, and mileage values
        """
        The run_simulation method is the main method of the PackageSorter Class. It uses methods above to help sort pkgs,
        load trucks, and deliver packages. The lists uses to complete the mentioned methods are instantiated and populated
        here. The method takes in 2 truck objects to complete the package deliveries.
        :param truck1:
        :param truck2:
        Space Complexity: O(N)
        Time Complexity: O(N^3)
        In while loop, calls method that has time complexity of O(N^2)
        """
        pkgs_to_be_delivered = []
        truck1_total_miles_travelled = 0
        truck2_total_miles_travelled = 0
        print("Truck 1 Beginning start time:")
        truck1.start_time.print_time()

        print("Truck 2 Beginning start time:")
        truck2.start_time.print_time()

        # populate pkgs to pkgs_be_delivered list from package hash table
        for key in range(len(self.pkg_hash.array)):
            pkgs_to_be_delivered.append(self.pkg_hash.get(key))

        # Main loop of simulation : Repeats itself until all packages are delivered
        while len(pkgs_to_be_delivered) > 0:
            # load trucks 1 and 2 to have next routes of packages to deliver
            self.load_trucks(pkgs_to_be_delivered, truck1, truck2)

            # comprehensions for testing/printing to see current route status
            route1_ids = [aux_route1.get_pkg_id() for aux_route1 in truck1.get_route()]
            route2_ids = [aux_route2.get_pkg_id() for aux_route2 in truck2.get_route()]
            print("route1", route1_ids)
            print("route2", route2_ids)
            print()

            # deliver packages - truck1
            print("Delivering packages...")
            if len(truck1.get_route()) != 0:
                # determine current & total miles travelled by truck 1 by deliver method, adds time travelled to truck
                truck1_current_miles_travelled = self.deliver_packages(truck1)
                truck1.start_time.add_time(truck1_current_miles_travelled / truck2.speed)
                truck1_total_miles_travelled += truck1_current_miles_travelled
            # deliver packages - truck2
            if len(truck2.get_route()) != 0:
                # determine current & total miles travelled by truck 2 by deliver method, adds time travelled to truck
                truck2_current_miles_travelled = self.deliver_packages(truck2)
                truck2.start_time.add_time(truck2_current_miles_travelled / truck2.speed)
                truck2_total_miles_travelled += truck2_current_miles_travelled
        # keep track of total mileage on trucks
        truck1.set_mileage(truck1_total_miles_travelled)
        truck2.set_mileage(truck2_total_miles_travelled)
        # print to see EOD time for each truck
        print()
        print("Truck 1 End Time")
        truck1.print_start_time()
        print("Truck 2 End Time")
        truck2.print_start_time()
