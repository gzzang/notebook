# @Time    : 2020/4/19 23:14
# @Author  : gzzang
# @File    : distance
# @Project : notebook


import geopy.distance

airport_min_lon = 116.573599
airport_max_lon = 116.626814
airport_min_lat = 40.047361
airport_max_lat = 40.108833

airport_min = (airport_min_lat, airport_min_lon)
airport_max = (airport_max_lat, airport_max_lon)
airport_distance = geopy.distance.distance(airport_min, airport_max).m
print(airport_distance)
