from lxml import html,etree
with open('bk_data.html') as f:
    data = f.read()
tree = html.fromstring(data)

for i in tree.xpath('//div[@class="store-info-box"]'):
    # print(etree.tostring(i, encoding='utf8', method='html').decode('utf8'))
    print(i.xpath(".//ui/following-sibling::li*/text()"))