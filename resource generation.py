"""
Simulator for resource generation with upgrades
"""

import simpleplot
import math
import codeskulptor
codeskulptor.set_timeout(20)


def resources_vs_time(upgrade_cost_increment, num_upgrade):
    """
    Build function that performs unit upgrades with specified cost increments
    """
    current_time = 1.0
    total_resources_generated = 1
    upgrade_cost = 1
    current_resource_generation_rate = 1
    output = ([])
    
    for i_loop in range(0, num_upgrade):

        output.append ([current_time, total_resources_generated]) 
        upgrade_cost += upgrade_cost_increment
        current_resource_generation_rate += 1
        upgrade_time_need = upgrade_cost / current_resource_generation_rate 
        current_time += upgrade_time_need
        total_resources_generated += upgrade_cost
    return output

def test():
    """
    Testing code for resources_vs_time
    """
    data1 = resources_vs_time(0, 20)
    data2 = resources_vs_time(0.5, 30)
    data3 = resources_vs_time(1, 40)
    data4 = resources_vs_time(2, 50)
    print data1
    print data2
    simpleplot.plot_lines("Growth", 600, 600, "time", "total resources", [data1, data2, data3, data4])

test()


# Sample output from the print statements for data1 and data2
#[[1.0, 1], [1.75, 2.5], [2.41666666667, 4.5], [3.04166666667, 7.0], [3.64166666667, 10.0], [4.225, 13.5], [4.79642857143, 17.5], [5.35892857143, 22.0], [5.91448412698, 27.0], [6.46448412698, 32.5], [7.00993867244, 38.5], [7.55160533911, 45.0], [8.09006687757, 52.0], [8.62578116328, 59.5], [9.15911449661, 67.5], [9.69036449661, 76.0], [10.2197762613, 85.0], [10.7475540391, 94.5], [11.2738698286, 104.5], [11.7988698286, 115.0]]
#[[1.0, 1], [2.25, 3.5], [3.58333333333, 7.5], [4.95833333333, 13.0], [6.35833333333, 20.0], [7.775, 28.5], [9.20357142857, 38.5], [10.6410714286, 50.0], [12.085515873, 63.0], [13.535515873, 77.5]]




