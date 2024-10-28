import json
import os
import sys, re
from typing import Type, T, Any
from flask import Flask, g, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


def makeitconstant(srccls: Type[T]) -> T:
    """
    https://github.com/kamawanu/zenn.dev-kamawanu-codes/blob/main/python3s/constant.py
    """
    class _(srccls):
        def __setattr__(self, __name: str, __value: Any):
            ...
    return _()


@makeitconstant
class pathes:
    data = "./data"
    suff = ".jsonl"
    prod = "product"
    test = "test"
    visidir = f"{data}/visi/"
    visitestpref = f"visi-{test}-data-"
    visipref = f"visi-{prod}-data-"

    clickdir = f"{data}/click/"
    clicktestpref = f"click-{test}-data-"
    clickpref = f"click-{prod}-data-"


@app.route("/health")
def health():
    return "ok"


@app.route("/post/visibility/<string:uid>", methods=["POST"])
def post_visibility(uid):
    if request.args.get("mode") == "test" :
        datadir = pathes.visidir + uid + "/"
        datapath = datadir + pathes.visitestpref + uid + pathes.suff
    if uid == "":
        return {"error": {"type": "InvalidPath", "message": f"The path '/post/visibility/{uid}' is invalid."}}, 404
    
    datadir = pathes.visidir + uid + "/"
    datapath = datadir + pathes.visipref + uid + pathes.suff

    if not os.path.isdir(datadir):
        os.makedirs(datadir)

    req = request.json
    with open(datapath, mode="a", encoding="utf-8") as f:
        json.dump(req, f,  ensure_ascii=False)
        f.write("\n")
    
    return req


@app.route("/post/click/<string:uid>", methods=["POST"])
def post_click(uid):
    if request.args.get("mode") == "test" :
        datadir = pathes.clickdir + uid + "/"
        datapath = datadir + pathes.clicktestpref + uid + pathes.suff
    if uid == "":
        return {"error": {"type": "InvalidPath", "message": f"The path '/post/click/{uid}' is invalid."}}, 404
    
    
    datadir = pathes.clickdir + uid + "/"
    datapath = datadir + pathes.clickpref + uid + pathes.suff

    if not os.path.isdir(datadir):
        os.makedirs(datadir)
    req = request.json
    with open(datapath, mode="a", encoding="utf-8") as f:
        json.dump(req, f,  ensure_ascii=False)
        f.write("\n")
    
    return req


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)