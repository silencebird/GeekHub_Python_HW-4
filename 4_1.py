import os
import re

if not(os.path.exists('reports')):
    os.makedirs('reports')

# regular expressions
regex_condition = re.compile(r'WARNING|ERROR|CRITICAL')
regex_date = re.compile(r'^\d\d\d\d-(0?[1-9]|1[0-2])-(0?[1-9]|[12][0-9]|3[01]) (00|[0-9]|1[0-9]|2[0-3]):([0-9]|[0-5][0-9]):([0-9]|[0-5][0-9]).+?')
regex_description = re.compile(r'((?<=WARNING)|(?<=ERROR)|(?<=CRITICAL)).*?$')

#init walues
counter = 0
un = {}

# function <unique_line> will create dict with unique descriptions
def unique_line(description):
    if description not in un:
        un[description] = {}
        un[description]['qty'] = 1
        un[description]['description'] = descript
        un[description]['marker'] = marker
        un[description]['date'] = date
    else:
        un[description]['qty'] += 1

# create all_data.csv (separetor - ";")
with open('./openerp-server.txt', 'rt') as f:
        with open('./reports/all_data.csv', 'w') as output:
                output.write('Line_id' + '; ' + 'Marker' + ';' + 'Date_time' + '; ' + 'Description' + '\n')

                for line in f:
                    if regex_condition.search(line):
                        date = regex_date.search(line).group(0)
                        marker = regex_condition.search(line).group(0)
                        descript = regex_description.search(line).group(0).lstrip().split(" ", 1)[1]
                        unique_line(descript)
                        output.write(str(counter)+'; '+marker+';'+date+'; '+descript+'\n')
                    counter += 1

# create unique.csv (separetor - ";")
with open('./reports/unique.csv', 'w') as unique:
    unique.write('Count' + '; ' + 'Marker' + ';' + 'Date_time' + '; ' + 'Description' + '\n')
    for item in un:
        unique.write(str(un[item]['qty']) + '; ' + str(un[item]['marker']) + ';' + str(un[item]['date']) + '; ' + str( un[item]['description']) + '\n')


