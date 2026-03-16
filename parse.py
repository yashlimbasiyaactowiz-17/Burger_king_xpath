from util import read_json_zip_files
import json
from db_config import create, insert_into_db
from concurrent.futures import ThreadPoolExecutor # FOR BATCHES
import os
from parsel import Selector
from util import read_html_file


path = r"C:\Users\yash.limbasiya\Desktop\Projects\restaurent\Burger_king\Burger King Locator _ Ahmedabad _ Fast Food Restaurant.html"

table_name = "burger_king"


def prsel(raw_html: str):
    sel = Selector(raw_html)
    create(table_name)
    rows = []
    for store in sel.xpath("//div[@class='store-info-box']"):
        item = {}
        id = store.xpath("normalize-space(.//li[@class = 'outlet-phone']//a/@onclick)").get()
        item["restarent_id"] = id.split(",")[-1].replace("'","").replace(")","").strip()
        item["restaurant_name"] = store.xpath("normalize-space(.//li[@class='outlet-name']//a/text())").get()
        item["slug"] = store.xpath("normalize-space(.//li[@class='outlet-name']//a/@href)").get()
        item["address"] = store.xpath("normalize-space(.//li[@class='outlet-address']//span/text())").get()
        item["phone_number"] = store.xpath("normalize-space(.//li[@class='outlet-phone']//a/text())").get()
        item["hours"] = store.xpath("normalize-space(.//li[contains(@class,'outlet-timings')]//span/text())").get()
        rows.append(item)

    # print(address)
    # print(rows)

    
    return rows


def main():
    raw = read_html_file(path)
    data = prsel(raw)
    for i in data:
        insert_into_db(table_name, data=i)


if __name__ == "__main__":
    main()
