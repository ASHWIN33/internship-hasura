from __future__ import print_function
from flask import Flask,render_template, redirect, abort, url_for ,make_response,request
import random,sys,requests,json

app =Flask(__name__)
#task 1
@app.route('/')
def index():
    return 'Hello World - Ashwin'

#task 2
@app.route('/authors',methods=['post','get'])
def authors():
    #task 2.1
    post = requests.get("https://jsonplaceholder.typicode.com/posts")
    #task 2.2
    author = requests.get("https://jsonplaceholder.typicode.com/users")
    #task 2.3
    #a = len(author)
    #b = len(post)
    name = []
    count = []
    for x in range(0,10):
        name.append(0)
        count.append(0)
    for x in range(0,10):
        name[x] = author.json()[x]['name']
        id= author.json()[x]['id']
        for y in range(0,100):
            user_id = post.json()[y]['userId']
            if id == user_id:
                count[x] = count[x] + 1
    return render_template('author.html',name=name,count=count)

#task 3
@app.route('/setcookie')
def setcookie():
    detail = make_response('setting cookie')
    detail.set_cookie('name', 'ashwin', 'age', '19')
    detail.set_cookie('age', '19')
    return detail

#task 4
@app.route('/getcookies')
def getcookie():
    name = request.cookies.get('name')
    age = request.cookies.get('age')
    return "<h1>name=%s"%name+"<br>age=%s </h1>" %age

#task 5
@app.route('/robots.txt')
def robots():
    rand = random.randrange(1,3,1)
    if rand == 1:
        return abort(401)
    else:
        return redirect("http://httpbin.org/deny")

#task 6
@app.route('/image')
@app.route('/html')
def bad():
    return render_template('image.html')

#task 7
@app.route('/input')
def input():
    return render_template('login.html')
@app.route('/final',methods=['post','get'])
def final():
    if request.method == 'GET':
        return 'send post request'
    else:
        name = request.form['name']
        log = open('log.txt', 'a')
        log.write(name)
        log.close()
        print(name, file=sys.stderr)
        return 'look at the stdout and log.txt file'

if __name__ == '__main__':
    app.run('',8080,debug=True)
