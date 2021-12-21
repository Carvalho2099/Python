from flask import Flask, request, redirect, url_for, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)


@app.route("/response")
def response():
    # headers = {
    #     "content-type": "text/html"
    # }
    # return Response("Uma resposta do servidor", 200, headers=headers)
    # return "Uma resposta do servidor"
    return render_template("response.html")


@app.route("/")
def index():
    return "<a href='/posts'>Posts</a>"\



@app.route("/redirect")
def func_redirect():
    return redirect(url_for("response"))


@app.route("/posts")
def posts():
    titulo = request.args.get('titulo')
    data = dict(
        path=request.path,
        referrer=request.referrer,
        content_type=request.content_type,
        method=request.method,
        titulo=titulo
    )
    return data


if __name__ == '__main__':
    app.run(debug=True)
