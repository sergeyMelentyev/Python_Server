import urllib.request
import csv
import json

'''Import all indexes from json as list'''
with open('index.json') as index_json:
    row_value = json.load(index_json)
    index = row_value['index']

'''Import all tags from json as dictionary'''
with open('tags.json') as tags_json:
    tags = json.load(tags_json)

'''Select required tags here'''
required_tags_key = ['s', 'n', 'a', 'y', 'b', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'j1', 'v']
header_names = ''

'''Sort all tags and get required'''
for key in required_tags_key:
    required_tags_name = tags[key]
    header_names += '{}, '.format(required_tags_name)
header_names += '\n'

'''Create index file with required tags'''
for index_each in index:
    file_name = '{}'.format(index_each) + '.csv'
    with open(file_name, 'w') as createHeader:
        createHeader.write(header_names)
        createHeader.close()
    '''Get all symbols from Nasdaq server'''
    url = 'http://www.nasdaq.com/screening/companies-by-industry.aspx?exchange={}&render=download'.format(index_each)
    request = urllib.request.urlopen(url)
    symbolSource = request.read()
    with open('sourceRowFile{}.csv'.format(index_each), 'wb') as createRowFile:
        createRowFile.write(symbolSource)
        createRowFile.close()

'''Create a final request'''
for index_final in index:
    index_file_name = 'sourceRowFile{}.csv'.format(index_final)
    with open(index_file_name, 'r') as name:
        each_row = csv.reader(name, delimiter=',', quotechar='|')
        for row in each_row:
            f_url = "http://download.finance.yahoo.com/d/quotes.csv?s={}&f={}{}{}{}{}{}{}{}{}{}{}{}{}&e=".format(row[0], required_tags_key[0], required_tags_key[1], required_tags_key[2], required_tags_key[3], required_tags_key[4], required_tags_key[5], required_tags_key[6], required_tags_key[7], required_tags_key[8], required_tags_key[9], required_tags_key[10], required_tags_key[11], required_tags_key[12])
            requestTicker = urllib.request.urlopen(f_url)
            requestTickerFile = requestTicker.read()
            file_name = '{}'.format(index_final) + '.csv'
            with open(file_name, 'ab') as finalTable:
                finalTable.write(requestTickerFile)
                finalTable.close()
