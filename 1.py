
if __name__=="__main__":
    import requests
    url = "http://jwbinfosys.zju.edu.cn/CheckCode.aspx"

    headers = {
        'cache-control': "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Connection": "keep - alive"
    }

    response = requests.request("GET", url, headers=headers)

    print response.text