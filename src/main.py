# Name: Christopher Staib |  Student ID: #001174711
import Utils
import PackageSorter
import Truck
import TrackTime

"""
Whole program
Space Complexity: O(N)
Time Complexity: O(N^3)
"""


def main():
    # create hashtable for packages
    pkg_hash = Utils.generate_package_hash()
    # create distance list
    dist_values = Utils.load_distance_file()
    # create new PackageSorter object with hashtable and distance list generated previously
    pkg_sorter = PackageSorter.PackageSorter(dist_values, pkg_hash)
    # create track times for truck starting time
    truck1_start_time = TrackTime.TrackTime("8:00")
    truck2_start_time = TrackTime.TrackTime("9:05")
    # create trucks
    truck1 = Truck.Truck(1, truck1_start_time)
    truck2 = Truck.Truck(2, truck2_start_time)
    input_option = None
    # run simulation
    print("*******************Simulation*******************")
    pkg_sorter.run_simulation(truck1, truck2)
    print("************************************************")
    """
    Space Complexity: O(N)
    Time Complexity: O(N^2)
    For rest of code below
    """
    while input_option != "q":
        print("Please Select an Option Below:")
        print("Press 1 to view the status or info of a package.")
        print("Press 2 to view the total mileage of all trucks.")
        print("Press q to quit.")

        input_option = input("Option: ")
        # option to view package info/status
        if input_option == "1":
            print()
            print("Package Menu:")
            print("Press 1 to view the status of all packages at a specific time")
            print("Press 2 to view the status of a specific package at a specific time")
            print("Press 3 to view the information of a specific package")
            input_package_type = input("Option: ")

            # view statuses of all packages
            if input_package_type == "1":
                print()
                print("Please input a time below in military time after 8:00")
                input_time = input("Time (H:MM) or (HH:MM): ")
                user_time = TrackTime.TrackTime(input_time)
                print("************************************************")
                for i in range(len(pkg_hash.array)):
                    user_package = pkg_hash.get(i)
                    print("Package Id:", user_package.get_pkg_id())
                    user_package.print_time_loaded()
                    user_package.print_time_delivered()

                    if user_time < user_package.get_time_loaded():
                        status = "At Hub."
                    elif user_time < user_package.get_time_delivered() or user_time == user_package.get_time_loaded():
                        status = "On route."
                    else:
                        status = "Delivered."
                    print("Status at", input_time + ":", "Package", i + 1, "is", status)
                    print()
                print("************************************************")
                print()

            # view status of any package
            elif input_package_type == "2":
                print()
                print("Please input a time below in military time after 8:00")
                input_time = input("Time (H:MM) or (HH:MM): ")
                user_time = TrackTime.TrackTime(input_time)
                print("Please input a package ID (1-40)")
                input_id = input("Package ID: ")
                # check time input and check conditions to determine if at hub, on route, or delivered
                user_package = pkg_hash.get(int(input_id) - 1)
                print("************************************************")
                print("Package Id:", user_package.get_pkg_id())
                user_package.print_time_loaded()
                user_package.print_time_delivered()

                if user_time < user_package.get_time_loaded():
                    status = "At Hub."
                elif user_time < user_package.get_time_delivered() or user_time == user_package.get_time_loaded():
                    status = "On route."
                else:
                    status = "Delivered."
                print("Status at", input_time + ":", "Package", input_id, "is", status)
                print("************************************************")

            # view info of a package
            elif input_package_type == "3":
                print()
                print("Please input a package ID (1-40)")
                input_id = input("Package ID: ")
                display_pkg = pkg_hash.get(int(input_id) - 1)
                display_pkg.print_all_information()
            else:
                print()
                print("**ERROR**: Invalid option, please read and select from the current options.")
                print()

        # option to view mileage for trucks
        elif input_option == "2":
            print()
            print("Mileage Menu:")
            print("Press 1 to view total mileage for Truck 1")
            print("Press 2 to view total mileage for Truck 2")
            print("Press 3 to view total mileage for both trucks")
            input_mileage_option = input("Option: ")
            print()
            if input_mileage_option == "1":
                print("************************************************")
                print("Total mileage of truck 1:", truck1.get_mileage())
                print("************************************************")
            elif input_mileage_option == "2":
                print("************************************************")
                print("Total mileage of truck 2:", truck2.get_mileage())
                print("************************************************")
            elif input_mileage_option == "3":
                print("************************************************")
                print("Total mileage of both trucks:", truck1.get_mileage() + truck2.get_mileage())
                print("************************************************")
            else:
                print("**ERROR**: Invalid option, please read and select from the current options.")
            print()
        # print error if user types in an incorrect input
        else:
            print("**ERROR**: Invalid option, please read and select from the current options.")


if __name__ == '__main__':
    main()
