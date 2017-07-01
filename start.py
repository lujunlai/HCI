#encoding=utf8
from flask import Flask,render_template,request#,jsonify
from flask_cors import *
import requests
from bs4 import BeautifulSoup
app = Flask(__name__)
CORS(app,supports_credentials=True)
cookie=None
@app.route('/',methods=['GET','POST'])
def login():
    global cookie
    if request.method=="GET":
        return render_template("login.html")
    elif request.method=="POST" and request.form.get("PASSWORD") and request.form.get("ID") and request.form.get("CHECKCODE"):
        url = "http://jwbinfosys.zju.edu.cn/default2.aspx"
        print request.form.get("PASSWORD") , request.form.get("ID") , request.form.get("CHECKCODE")
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"TextBox1\"\r\n\r\n"+request.form.get("ID")+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"TextBox2\"\r\n\r\n"+request.form.get("PASSWORD")+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"TextBox3\"\r\n\r\n"+request.form.get("CHECKCODE")+"\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__VIEWSTATE\"\r\n\r\ndDwxNTc0MzA5MTU4Ozs+b5wKASjiu+fSjITNzcKuKXEUyXg=\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"__EVENTTARGET\"\r\n\r\nButton1\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Connection": "keep - alive"
        }

        response = requests.request("POST", url, data=payload, headers=headers,cookies=cookie)
        if response.text.startswith("<script"):
            return response.text.split("\n")[0]+render_template("login.html")
        url = "http://jwbinfosys.zju.edu.cn/xscj.aspx"

        querystring = {"xh": request.form.get("ID")}

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-datainfo; name=\"__VIEWSTATE\"\r\n\r\ndDw0NzAzMzE4ODg7dDw7bDxpPDE+Oz47bDx0PDtsPGk8Mj47aTw1PjtpPDI1PjtpPDI3PjtpPDQxPjtpPDQzPjtpPDQ1PjtpPDQ3Pjs+O2w8dDx0PDt0PGk8MTg+O0A8XGU7MjAwMS0yMDAyOzIwMDItMjAwMzsyMDAzLTIwMDQ7MjAwNC0yMDA1OzIwMDUtMjAwNjsyMDA2LTIwMDc7MjAwNy0yMDA4OzIwMDgtMjAwOTsyMDA5LTIwMTA7MjAxMC0yMDExOzIwMTEtMjAxMjsyMDEyLTIwMTM7MjAxMy0yMDE0OzIwMTQtMjAxNTsyMDE1LTIwMTY7MjAxNi0yMDE3OzIwMTctMjAxODs+O0A8XGU7MjAwMS0yMDAyOzIwMDItMjAwMzsyMDAzLTIwMDQ7MjAwNC0yMDA1OzIwMDUtMjAwNjsyMDA2LTIwMDc7MjAwNy0yMDA4OzIwMDgtMjAwOTsyMDA5LTIwMTA7MjAxMC0yMDExOzIwMTEtMjAxMjsyMDEyLTIwMTM7MjAxMy0yMDE0OzIwMTQtMjAxNTsyMDE1LTIwMTY7MjAxNi0yMDE3OzIwMTctMjAxODs+Pjs+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDx4eHE7eHExOz4+Oz47dDxpPDg+O0A8XGU756eLO+WGrDvnn6075pqRO+aYpTvlpI8755+tOz47QDxcZTsxfOenizsxfOWGrDsxfOefrTsxfOaakTsyfOaYpTsyfOWkjzsyfOefrTs+Pjs+Ozs+O3Q8cDw7cDxsPG9uY2xpY2s7PjtsPHdpbmRvdy5wcmludCgpXDs7Pj4+Ozs+O3Q8cDw7cDxsPG9uY2xpY2s7PjtsPHdpbmRvdy5jbG9zZSgpXDs7Pj4+Ozs+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8WkpEWDs+Pjs+Ozs+Oz4+Oz4+Oz7NejJ8ZzJ5XL04LXHW1/APGcDaBg==\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Button2\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Connection": "keep - alive"
        }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring,cookies=cookie)
        soup=BeautifulSoup(response.text,'html.parser')
        info=soup.find(id="Table1")
        scorelist=info.next_sibling.next_sibling.find_all("tr")
        dict={}
        dict=add(dict,scorelist[1:])
        print dict
        print sum(dict.values())

        return info.prettify()+info.next_sibling.next_sibling.prettify()
    else:
        return render_template("login.html")

@app.route('/CheckCode',methods=['GET','POST'])
def CheckCode():
    global cookie
    url = "http://jwbinfosys.zju.edu.cn/CheckCode.aspx"

    headers = {
        'cache-control': "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Connection": "keep - alive"
    }

    response = requests.request("GET", url, headers=headers)
    cookie=response.cookies
    return response.content


def add(dict,list):
    for x in list:
        name=x.find("td")
        mark=name.next_sibling.next_sibling.next_sibling
        score=mark.next_sibling
        if float(score.text)>0:
            if  dict.get(name.text.split("-")[3]) and  name.text.split("-")[3].startswith("401"):
                dict[name.text.split("-")[3]] += float(mark.text)
            else:
                dict[name.text.split("-")[3]]=float(mark.text)

    return dict


if __name__=="__main__":
    app.run(debug=True)