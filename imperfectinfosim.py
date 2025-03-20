import random
import sys
import matplotlib.pyplot as p1
import math
import termcolor

def average(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum/len(list)


def max(list):
    max = 0
    for i in list:
        if(i > max):
            max = i
    return max

qualities = list()
#qualities = [2.0,1.9,1.8, 1.7,1.7,1.7,1.7,1.6,1.5,1.4,1.3,1.2] #numerical representation of qualities for the good
qualities = [2.0,1.9,1.8, 1.7,1.7,1.7,1.7,1.6,1.5,1.4,1.3,1.2]
demand_curve_price = [2000, 1900,  1800, 1700, 1600, 1500, 1400, 1300, 1200, 1000]
demand_curve_quant = [ 0, 1  ,  2   , 4   , 6  , 8  , 9,  11, 12 , 14]

demand_curve_real_price_per_unit_buyers = []
init_quals_size_list = []
price_per_unit_quality_sellers = 800 #PS
supply_curve = []
demand_curve = []
pb_list = []
max_quantity_supplied = len(qualities)



for c in range(0,len(qualities)):
    average_val = average(qualities)
    PB_value = price_per_unit_quality_sellers*max(qualities)/average_val #MINIMUM price per unit of value the buyer is willing to spend in order to prevent a seller from exiting the market.
    pb_list.append(PB_value)
    supply_curve.append(max(qualities)*price_per_unit_quality_sellers)
    init_quals_size_list.append(len(qualities))
    for x in range(0,len(demand_curve_quant)):
        if(demand_curve_quant[x] == len(qualities)): #is the coorosponding index in demand_curve_price
            # termcolor.cprint(str((demand_curve_price[x])),'yellow')
            # termcolor.cprint(str(average_val),'blue')
            # termcolor.cprint(str(demand_curve_price[x]/average_val),'red')
            demand_curve_real_price_per_unit_buyers.append(demand_curve_price[x]/average_val)
    print(str(round(average_val,2)) + "    :    " + str(round(PB_value,2)) + "    :     "+str(len(qualities)))
    del qualities[0]
    

demand_curve_quant_adjusted = []
for k in demand_curve_quant:
    if(k<= max_quantity_supplied and k != 0):
        demand_curve_quant_adjusted.append(k)
demand_curve_real_price_per_unit_buyers.reverse() #reversed because higher quantity values are added first to the list, but demand_curv_quant_adjusted is not greatest to least, but least to greatest


# fig = p1.figure()
# ax = p1.axes(projection ='3d')
# ax.scatter3D(init_quals_size_list, supply_curve, supply_curve, 'green')
# ax.set_title('Plot of Trajectory over time interval')
# p1.show()

p1.scatter(init_quals_size_list, supply_curve, color = "RED", linewidth=2) #supply curve
p1.scatter(demand_curve_quant, demand_curve_price, color = "BLUE", linewidth=2) #demand curve
p1.plot(init_quals_size_list, supply_curve, color = "RED", linewidth=2, label = "Supply Curve") #supply curve
p1.plot(demand_curve_quant, demand_curve_price, color = "BLUE", linewidth=2, label = "Demand Curve") #demand curve

print(demand_curve_quant_adjusted)
print(demand_curve_real_price_per_unit_buyers)
p1.scatter(init_quals_size_list, pb_list, color = "GREEN", linewidth=2) #minimum value from buyers per unit of value nessecary to prevent market collapse
p1.scatter(demand_curve_quant_adjusted,demand_curve_real_price_per_unit_buyers, color = "MAGENTA", linewidth=2) #derived value per unit of value nessecary to prevent market collapse
p1.plot(init_quals_size_list, pb_list, color = "GREEN", linewidth=2, label = "Minimum Demand Price per unit quality without seller exit/ Market Quality") #minimum value from buyers per unit of value nessecary to prevent market collapse
p1.plot(demand_curve_quant_adjusted,demand_curve_real_price_per_unit_buyers, color = "MAGENTA", linewidth=2, label = "Demand Curve Price per unit quality / Market Quality") #derived value per unit of value nessecary to prevent market collapse
p1.legend()
p1.show()