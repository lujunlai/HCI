#encoding=utf8
from flask import Flask,render_template,request#,jsonify
from flask_cors import *
import requests
from bs4 import BeautifulSoup
import pickle
from match import match
import json
#import sys
#reload(sys)
#sys.setdefaultencoding('utf8')
app = Flask(__name__)
CORS(app,supports_credentials=True)
cookie=None
input = open('curriculum.pkl', 'rb')
curriculum = pickle.load(input)
id=None
input.close()
info=None
@app.route('/',methods=['GET','POST'])
def login():
    global cookie
    global curriculum
    global info
    global id
    if request.method=="GET":
        return render_template("lo_gin.html")
    elif request.method=="POST" and request.form.get("PASSWORD") and request.form.get("ID") and request.form.get("CHECKCODE"):
        id=request.form.get("ID")
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
            return "0;"+response.text.split("\n")[0]
        url = "http://jwbinfosys.zju.edu.cn/xscj.aspx"

        querystring = {"xh": request.form.get("ID")}

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-datainfo; name=\"__VIEWSTATE\"\r\n\r\ndDw0NzAzMzE4ODg7dDw7bDxpPDE+Oz47bDx0PDtsPGk8Mj47aTw1PjtpPDI1PjtpPDI3PjtpPDQxPjtpPDQzPjtpPDQ1PjtpPDQ3Pjs+O2w8dDx0PDt0PGk8MTg+O0A8XGU7MjAwMS0yMDAyOzIwMDItMjAwMzsyMDAzLTIwMDQ7MjAwNC0yMDA1OzIwMDUtMjAwNjsyMDA2LTIwMDc7MjAwNy0yMDA4OzIwMDgtMjAwOTsyMDA5LTIwMTA7MjAxMC0yMDExOzIwMTEtMjAxMjsyMDEyLTIwMTM7MjAxMy0yMDE0OzIwMTQtMjAxNTsyMDE1LTIwMTY7MjAxNi0yMDE3OzIwMTctMjAxODs+O0A8XGU7MjAwMS0yMDAyOzIwMDItMjAwMzsyMDAzLTIwMDQ7MjAwNC0yMDA1OzIwMDUtMjAwNjsyMDA2LTIwMDc7MjAwNy0yMDA4OzIwMDgtMjAwOTsyMDA5LTIwMTA7MjAxMC0yMDExOzIwMTEtMjAxMjsyMDEyLTIwMTM7MjAxMy0yMDE0OzIwMTQtMjAxNTsyMDE1LTIwMTY7MjAxNi0yMDE3OzIwMTctMjAxODs+Pjs+Ozs+O3Q8dDxwPHA8bDxEYXRhVGV4dEZpZWxkO0RhdGFWYWx1ZUZpZWxkOz47bDx4eHE7eHExOz4+Oz47dDxpPDg+O0A8XGU756eLO+WGrDvnn6075pqRO+aYpTvlpI8755+tOz47QDxcZTsxfOenizsxfOWGrDsxfOefrTsxfOaakTsyfOaYpTsyfOWkjzsyfOefrTs+Pjs+Ozs+O3Q8cDw7cDxsPG9uY2xpY2s7PjtsPHdpbmRvdy5wcmludCgpXDs7Pj4+Ozs+O3Q8cDw7cDxsPG9uY2xpY2s7PjtsPHdpbmRvdy5jbG9zZSgpXDs7Pj4+Ozs+O3Q8QDA8Ozs7Ozs7Ozs7Oz47Oz47dDxAMDw7Ozs7Ozs7Ozs7Pjs7Pjt0PEAwPDs7Ozs7Ozs7Ozs+Ozs+O3Q8cDxwPGw8VGV4dDs+O2w8WkpEWDs+Pjs+Ozs+Oz4+Oz4+Oz7NejJ8ZzJ5XL04LXHW1/APGcDaBg==\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Button2\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'cache-control': "no-cache",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        }

        response = requests.request("POST", url, data=payload, headers=headers, params=querystring,cookies=cookie)
        soup=BeautifulSoup(response.text,'html.parser')
        info=soup.find(id="Table1")
        scorelist=info.next_sibling.next_sibling.find_all("tr")
        dict = {}
        dict=add(dict,scorelist[1:])
        result=match(curriculum,dict)
        return "1;"+json.dumps(result)
        #print dict
        #print sum(dict.values())

        #return info.prettify()+info.next_sibling.next_sibling.prettify()
    else:
        return render_template("lo_gin.html")

@app.route('/CheckCode',methods=['GET','POST'])
def CheckCode():
    global cookie
    url = "http://jwbinfosys.zju.edu.cn/CheckCode.aspx"

    headers = {
        'cache-control': "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    }

    response = requests.request("GET", url, headers=headers)
    cookie=response.cookies
    return response.content

@app.route('/info',methods=['GET','POST'])
def search():
    global info
    if info:
        return render_template('info.html',s=info.prettify()+"\n"+info.next_sibling.next_sibling.prettify())
    else:
        return ''

@app.route('/check',methods=['GET','POST'])
def check():
    global cookie
    global id
    # if cookie:
    #     return json.dumps(dict(cookie))
    # else:
    #     return ''
    if cookie and id:
        # url = "http://jwbinfosys.zju.edu.cn/xscxbm.aspx"
        # querystring = {"xh": id}
        # headers = {
        #     'cache-control': "no-cache",
        #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        # }
        # response = requests.request("GET", url, headers=headers, params=querystring,cookies=cookie)
        if request.method == "POST" and request.form.get("DropDownList1") and request.form.get("What"):
            url = "http://jwbinfosys.zju.edu.cn/xscxbm.aspx"

            querystring = {"xh": id}

            payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-datainfo; name=\"__VIEWSTATE\"\r\n\r\ndDwxOTk4MDIzMTIxOztsPENoZWNrQm94MTs+PmUsjUsgXHtqC5Iro8/RjQSpD4QW\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Dropdownlist_gx1\"\r\n\r\nlike\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"DropDownList1\"\r\n\r\n" + request.form.get(
                "DropDownList1") + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"TextBox1\"\r\n\r\n" + request.form.get(
                "What") + "\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"Button5\"\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
            headers = {
                'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
                'cache-control': "no-cache",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            }

            response = requests.request("POST", url, data=payload, headers=headers, params=querystring, cookies=cookie)
            soup=BeautifulSoup(response.text,'html.parser')
            s=soup.find("div",class_='mainframe').prettify()
            s=s.replace("html_kc","http://jwbinfosys.zju.edu.cn/html_kc")
            s = s.replace("tpml", "http://jwbinfosys.zju.edu.cn/tpml")
            s=s.replace("xsxjs.aspx",'choose')
            return s
        elif request.method=="GET":
            return render_template('search.html')
        else:
            return ''
        #return render_template('search.html')
    else:
        return ''

@app.route('/choose',methods=['GET','POST'])
def choose():
    global cookie
    url = "http://jwbinfosys.zju.edu.cn/xsxjs.aspx"
    querystring = request.args
    headers = {
        'cache-control': "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    }
    if request.method=="GET":
        response = requests.request("GET", url, headers=headers, params=querystring,cookies=cookie)
    #return response.text
        s=response.text
        s=s.replace('src="','src="http://jwbinfosys.zju.edu.cn/')
        s=s.replace("src='", "src='http://jwbinfosys.zju.edu.cn/")
        s=s.replace("href='", "href='http://jwbinfosys.zju.edu.cn/")
        s = s.replace('href="', 'href="http://jwbinfosys.zju.edu.cn/')
        return s
    else:
        return ''

@app.route('/ajax/zjdx.AjaxForm,zjdx.ashx', methods=['GET', 'POST'])
def make():
    global cookie
    url = "http://jwbinfosys.zju.edu.cn/ajax/zjdx.AjaxForm,zjdx.ashx"
    querystring = request.args
    headers = {
        'cache-control': "no-cache",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    }
    if request.method=="POST":
        form=request.form
        response = requests.request("POST", url,data=request.data , headers=headers,params=querystring, cookies=cookie)
        return response.text
    else:
        return ''

@app.route('/close',methods=['GET','POST'])
def close():
    global cookie
    global info
    global id
    cookie=None
    info=None
    id=None
    return ''

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
    app.run(host='0.0.0.0',debug=True,threaded=True)
