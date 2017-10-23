import requests
import csv
import io

def get_gSheet(file_id):
    headers={}
    headers["User-Agent"]= "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:22.0) Gecko/20100101 Firefox/22.0"
    headers["DNT"]= "1"
    headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    headers["Accept-Encoding"] = "deflate"
    headers["Accept-Language"]= "en-US,en;q=0.5"

    url = "https://docs.google.com/spreadsheets/d/{0}/export?format=csv".format(file_id)

    r = requests.get(url)

    sio = io.StringIO( r.text, newline=None)
    reader = csv.reader(sio, dialect=csv.excel)
    return reader

def get_headers(row):
    cols = []
    for col in row:
        cols.append(col)
    return cols

def get_row_data(row, headers):
    data = {}
    i = 0
    for col in row:
        data[headers[i]] = col
        i = i +1
    return data
