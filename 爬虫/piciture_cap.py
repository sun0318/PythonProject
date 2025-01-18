import requests
if __name__ == '__main__':
    # url = "https://kyfw.12306.cn/otn/leftTicket/query"
    url = "https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fc-ssl.duitang.com%2Fuploads%2Fitem%2F201707%2F11%2F20170711012158_2cBLZ.thumb.1000_0.jpeg&refer=http%3A%2F%2Fc-ssl.duitang.com&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=auto?sec=1727182282&t=1cdb3c5ac247fc3e866f9a3c27db1a44"
    response = requests.get(url=url).content
    with open("whale.jpg","wb") as fp:
        fp.write(response)


