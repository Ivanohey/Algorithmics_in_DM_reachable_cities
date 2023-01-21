from urllib.request import urlopen
from urllib.parse import quote, urlencode

origin_city = ""
dest_city = ""
# SELECT * FROM located: ['Geneva', 'GE', 'CH', 'Rhone', 'Lac Leman']
# SELECT * FROM City: ['Zurich', 'CH', 'ZH', '343106']
# SELECT * FROM Country: ['Switzerland', 'CH', 'Bern', 'BE', '41290', '7207060']
lat_origin, lon_origin = 0, 0
lat_dest, lon_dest = 0, 0
distance = abs(lat_origin - lat_dest) + abs(lon_origin - lon_dest)

def neighbors(city: str, country: str, d: float, s: float) -> set[(str,str)]:
    #Get all the rivers and lakes that are next to the city
    find_rivers(city, country)
    find_neighbor_cities(city, country)

#We define a function allowing to call the database by passing a SQL request
def query_db(sql_query):
    q = sql_query

    eq = quote(q)
    url = "http://kr.unige.ch/phpmyadmin/query.php?db=mondial&sql="+eq
    query_results = urlopen(url)
    result_list = []

    # iterate over the result rows
    for line in query_results :
        string_line = line.decode('utf-8').rstrip()
    # if the query had a syntax error or if the result is empty
    # there is nevertheless one empty line, ignore it
        if len(string_line) > 0:
        # put the column values in columns
            columns = string_line.split("\t")
            result_list.append(columns)
    query_results.close()
    return result_list

print(query_db("SELECT City FROM located WHERE River = 'Rhone'"))
