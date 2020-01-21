orderfile = open('E:\\Big_Data\\Itversity\\data-master\\retail_db\\orders\\part-00000','r').read().splitlines()
# print(orderfile[:10])
# l = (orderfile[:10])                                                   # to print the items line by line
# print("\n".join(l))

# orderfile.sort(key= lambda s: int(s.split(",")[2]))                       # Sort can be performed only on the list
# print(orderfile[:10])

# print(sorted(orderfile,key= lambda s: int(s.split(",")[2]))[:10])                        # sorted returns the new list and does not affect the original list
# print(sorted(orderfile, key=lambda s: int(s.split(",")[2]), reverse= True)[:10])         # sorted can be performed on any collection(list, set and dict)

# for i in orderfile[:10]:                          # Print all the iterable elements from top 10 entries
#     print(i)

# for i in orderfile[:10]:                          # Using split function extract the order id's
#     print(str(int(i.split(',')[0])))

# for i in orderfile[:10]:                          # sing split function extract the date
#     print(i.split(',')[1])

##problem 1:
# Get all order status from orders data (looping through the list)
# and add it to the set
s = set([])
# help(s)
# for i in orderfile[:10]:
#     s.add(i.split(',')[-1])
# print(s)

##problem 2: create a function to get the revenue for a given order_id in orders_items file

orders_item_file = open('E:\\Big_Data\\Itversity\\data-master\\retail_db\\order_items\\part-00000','r').read().splitlines()
# print(orders_item_file[:10])
#
# for i in orders_item_file[:10]:
#     print(i.split(',')[-2])

def getOrderReveues(orderitems, orderid):
    orderRevenue = 0.0
    for orderitem in orderitems:
        if int(orderitem.split(',')[1]) == orderid:
            orderRevenue += float(orderitem.split(',')[-2])
            # print(orderitem.split(',')[-2])
    return orderRevenue

# print(getOrderReveues(orders_item_file,2))

##problem 3: create a function to get the revenue for each order_id in orders_items file

def getRevenueforOrders(orderItems):
    revenuePerorder = {}                             # storing the final result of, order id and corresponding revenue into dictionary
    for orderItem in orderItems:
        orderItemTuple = (int(orderItem.split(',')[1]), float(orderItem.split(',')[-2]))   # Created tuple to store the intermediate value n each iteration
        if(revenuePerorder.get(orderItemTuple[0])):  # If the key already exist in revenuePerorder {} then,
            revenuePerorder[orderItemTuple[0]] += orderItemTuple[1] # Extract the value and add it to the orderItemTuple[1]
        else:                                        # Else(if the key is not present in {})
            revenuePerorder[orderItemTuple[0]] = orderItemTuple[1]  # add the order id(key) and subtotal(value) to {}
    return revenuePerorder

revenueperorder = getRevenueforOrders(orders_item_file)
# print(revenueperorder)

##problem 4: create a function to get daily revenue using orders which are completed or closed and order items

#4.1. Get daily revenues of completed and closed orders
# 4.2 Develop a function to get completed and closed orders
# 4.3 Extract order id and date for complted and closed orders
# 4.4 Join with order_items, get order item subtotal and aggregate revenue for each day

def getCompletedorders(orders):
    filted_orders = []
    for order in orders:
        # if (order.split(',')[-1] == 'CLOSED' or order.split(',')[-1] == 'COMPLETE'):  # Either of the statements can be used
        if (order.split(',')[-1] in ('CLOSED', 'COMPLETE')):
            filted_orders.append(order)
    return filted_orders



def getDictforComleteOrders(orders):
    orders_dict = {}
    for order in orders:
        order_attributes = order.split(',')
        if (order_attributes[-1] in ('CLOSED', 'COMPLETE')):
            orders_dict[int(order_attributes[0])] = order_attributes[1]
    return orders_dict


def getOrderIDandDateDict(orders):
    orderIdandDateDict = {}
    for order in orders:
        order_attributes = order.split(',')             #Doesn't require the if else block as we have already filtered to extract the filtered dict
        orderIdandDateDict[int(order_attributes[0])] = order_attributes[1]
    return orderIdandDateDict


def getDailyRevenues(orderIdandDateDic, orders):
    dailyRevenues = {}
    for order in orders:
        orderitemTuple = (int(order.split(',')[1]), float(order.split(',')[4]))
        if (orderIdandDateDic.get(orderitemTuple[0])):     # if the lookup (order id in orderIdandDateDict & order id in orderitemTuple)is successful
            orderDate = orderIdandDateDic[orderitemTuple[0]]
            if(dailyRevenues.get(orderDate)):                  # if the "key" order date exists in the dailyRevenues dict,
                dailyRevenues[orderDate] += orderitemTuple[1]  # Then, Extract the "value" of that order date and add it up with the orderitemTuple[1]
            else:
                dailyRevenues[orderDate] = orderitemTuple[1]
    return dailyRevenues



filted_orders = getCompletedorders(orderfile)
dict_orders = getDictforComleteOrders(orderfile)
orderIdandDateDict = getDictforComleteOrders(filted_orders)
dailyRevenues = getDailyRevenues(orderIdandDateDict,orders_item_file)

for i in list(dailyRevenues.items())[:10]:
    print(i)

# print(filted_orders)
print(len(dict_orders))
print(len(orderIdandDateDict))