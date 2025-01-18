from lxml import etree
import requests
if __name__ == "__main__":
    url = "https://career.cic.tsinghua.edu.cn/xsglxt/f/jyxt/anony/viewDzxzph/9457952"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36"
    }
    response = requests.post(url=url, headers=headers)
    print(response.text)
    tree = etree.HTML(response.text)
    body = tree.xpath('/html/body/div[@class="modal-body"]/table/tr[1]/th/text()')
    # for child in body:
    #     print(child.tag)
    print(body)