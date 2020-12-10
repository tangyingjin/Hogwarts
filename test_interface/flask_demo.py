from flask import Flask, session, request, Request, make_response

app = Flask(__name__)
request: Request
app.secret_key = "key"


@app.route("/request", methods=['POST', 'GET'])
def hello():
    query = request.args
    post = request.form
    return f"query: {query}\n" \
           f"post: {post}"


@app.route("/session")
def session_handle():
    for k, v in request.args.items():
        session[k] = v
    resp = make_response({k: v for k, v in session.items()})
    for k, v in request.args.items():
        resp.set_cookie(f"cookie_{k}", v)
    return resp

# 运行命令
#window:set;linux:export
# export FLASK_APP=demo.py
# flask run

# 在终端terminal的当前目录下执行：set FlASK_APP=flask_demo.py
# flask run
# 网页访问http://127.0.0.1:5000/request?a=1&b=2
# Flask是python的web框架

