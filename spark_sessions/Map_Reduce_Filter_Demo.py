orders_data = open('E:\\Big_Data\\Itversity\\data-master\\retail_db\\orders\\part-00000','r').read().splitlines()
orders_items = open('E:\\Big_Data\\Itversity\\data-master\\retail_db\\order_items\\part-00000','r').read().splitlines()

# print(orders_data[:10])
# print(orders_items[:10])
######################################## Filter ##########################################################################################
def myfilter(orders):
    orderFiltered = []
    for order in orders:
        if (order.split(',')[-1] == "COMPLETE"):
            orderFiltered.append(order)
    return orderFiltered


def myfilter(c, f):
    newC = []
    for i in c:
        if (f(i)):
            newC.append(i)
    return newC

#Named Function
def condition(i):
    return i.split(',')[-1] == "COMPLETE"


# orderFiltered = myfilter(orders_data,condition )
orderFiltered = myfilter(orders_data,lambda o:o.split(',')[-1] == "COMPLETE"  )
Date_orderFiltered = myfilter(orders_data,lambda o:o.split(',')[1] == "2013-07-25 00:00:00.0"  )
orderId_order_ItemsFiltered = myfilter(orders_items,lambda o: int(o.split(',')[1]) == 8  )
# print(orderFiltered[:10])
# print(Date_orderFiltered[:10])
# print(orderId_order_ItemsFiltered)

######################################## MAP #############################################################################################
# Extracting order id and order status from order data
ordermap = []
# for orders in orders_data:
#     ordermap.append((int(orders.split(',')[0]),orders.split(',')[-1]))
# print(ordermap[:10])

# Extracting year and month from order date
# for orders in orders_data:
#     ordermap.append(orders.split(',')[1][:7])
# print(ordermap[:10])

# Extracting orderid and order_subtotal from order_items file
# for items in orders_items:
#     ordermap.append((int(items.split(',')[1]),float(items.split(',')[-1])))
# print(ordermap[:10])


def myMap(c, f):             # This function takes "collection" and "function" as arguments
    newC = []
    for i in c:
        newC.append(f(i))    # f(i) is the getOrderIdandStatus(order)
    return newC

# Named Function
def getOrderIdandStatus(order):
    return (int(order.split(",")[0]), order.split(",")[3])

orderIdandStatus = myMap(orders_data,getOrderIdandStatus)
# print(orderIdandStatus[:10])

#UnNamed Function

orderIdandStatus = myMap(orders_data,lambda order: (int(order.split(",")[0]), order.split(",")[3]))
Year_Date_orders = myMap(orders_data,lambda order: order.split(",")[1][:7])
orderid_subtotal_items = myMap(orders_items,lambda order_item: (int(order_item.split(",")[0]),float(order_item.split(',')[-2])))
# print(orderIdandStatus[:10])
# print(Year_Date_orders[:10])
# print(orderid_subtotal_items[:10])

#@ Note : The number of records of input collections and the transformed records will not change when we apply MAP

######################################## REDUCE ##########################################################################################
#Reduce (on filtered and mapped order items subtotal based on order_id)

#Typically in Reduce, if the input data is not the expected format to aggregate we have to transform the data and do the aggregations

# From our example of __orderitems__data, we cannot perform the aggregation operation(+) on two strings (for ex, calculating the sum of subtotals)
# therefore, we are typecasting into the float and do the arithemetic operation

def getOrderItemFiltered(orderitems, orderid):
    orderItemFiltered = []
    for orderitem in orderitems:
        if (int(orderitem.split(',')[1]) == orderid):
            orderItemFiltered.append(orderitem)
    return orderItemFiltered

def getOrderItemsMap(orderItemFiltered):
    OrderItemsMap = []
    for orderitem in orderItemFiltered:
        OrderItemsMap.append(float(orderitem.split(',')[-2]))
    return OrderItemsMap

Filtered_order_items = getOrderItemFiltered(orders_items,2)
OrderItemsMap = getOrderItemsMap(Filtered_order_items)
# print(Filtered_order_items[:10])
# print(OrderItemsMap)

# Find the total revenue of the Filtered_order_items ?
totalrevenue = OrderItemsMap[0]
for OrderItemsSubtotal in OrderItemsMap[1:]:
    totalrevenue += OrderItemsSubtotal
# print("Total Revenue of order_items with order id 2 is : ",totalrevenue)

# Find the minimum revenue of the Filtered_order_items ?
minrevenue = OrderItemsMap[0]
for OrderItemsSubtotal in OrderItemsMap[1:]:
    minrevenue = minrevenue if (minrevenue < OrderItemsSubtotal) else OrderItemsSubtotal

# print(minrevenue)

# Find the maximum revenue of the Filtered_order_items ?
maxrevenue = OrderItemsMap[0]
for OrderItemsSubtotal in OrderItemsMap[1:]:
    maxrevenue = maxrevenue if (maxrevenue > OrderItemsSubtotal) else OrderItemsSubtotal

# print(maxrevenue)

#Reduce FUnction:
def myReducefunc(c, f):
    first_element = c[0]
    for i in c[1:]:
        first_element = f(first_element,i)
    return first_element
Total_revenue = myReducefunc(OrderItemsMap, lambda i,j : i + j)
# print(Total_revenue)
minium_revenue = myReducefunc(OrderItemsMap, lambda i,j : i if (i < j) else j)
# print(minium_revenue)
max_revenue = myReducefunc(OrderItemsMap, lambda i,j : i if (i > j) else j)
# print(max_revenue)

###############################################By using python's default Filter, MAP and REDUCE methods###############################
# We can leverage the python's filter method to filter the records

orders_complete = filter(lambda o: o.split(",")[-1] == 'COMPLETE', orders_data)
# print(list(orders_complete)[:10])

orderid_complete = filter(lambda oi: int(oi.split(",")[1]) == 2, orders_items)
order_item_subtotal = map(lambda oi: float(oi.split(",")[-2]), orderid_complete)
# print(list(orderid_complete))
# print(list(order_item_subtotal))

import functools as ft
order_item_subtotal_SUM = ft.reduce(lambda r, k: r + k, order_item_subtotal)
# print(order_item_subtotal_SUM)

#********************************************************************** ITERTOOlS  ***************************************************************
# MAP, Reduce, FIlter by using Itertools

#********************************************************************** PANDAS  ***************************************************************
import pandas as pd
order_items_path = 'E:\\Big_Data\\Itversity\\data-master\\retail_db\\order_items\\part-00000'
df_order_item = pd.read_csv(order_items_path, header=None, names= ['order_items_id','order_id','order_item_product_id','orderitem_quantity',
                                                                    'order_item_subtotal','order_item_product_price'])
print(df_order_item.head())
print(df_order_item[['order_id','order_item_subtotal']].head())

print(df_order_item.groupby('order_id')['order_item_subtotal'].sum())