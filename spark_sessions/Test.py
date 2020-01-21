# def ReadData(datapath):
#     datafile = open('datapath','r')
#     dataStr = datafile.read()
#     datalist = dataStr.splitlines()
#     return datalist
#Orders = ReadData('E:\\Big_Data\\Itversity\\data-master\\retail_db\\orders\\part-00000','r')


help(dict)

revenuePerorder = {1: 299.98, 2: 579.98, 4: 699.85}
orderitem = '1,1,957,1,299.98,299.98'
orderItemTuple = (int(orderitem.split(',')[1]), float(orderitem.split(',')[-2]))
print(orderItemTuple)
#
print(revenuePerorder.get(orderItemTuple[0]))
#
# revenuePerorder[orderItemTuple[0]] += orderItemTuple[1]
#
revenuePerorder = {}
revenuePerorder[2] = "Hive"
# print(revenuePerorder)
# print(revenuePerorder.get(2))

