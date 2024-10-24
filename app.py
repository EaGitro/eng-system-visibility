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
    data = "/data/"
    suff = ".jsonl"
    prod = "product"
    test = "test"
    visi = f"{data}/visi/visi-"
    visitest = f"{visi}-{test}-data-"
    visiprod = f"{visi}-{prod}-data-"


@app.route("/health")
def health():
    return "ok"


@app.route("/visibility/post/<string:uid>", methods=["POST"])
def visibility_post(uid):
    if request.args.get("mode") == "test" :
        datapath = pathes.visitest + uid + pathes.suff
    if uid == "":
        return {"error": {"type": "InvalidPath", "message": f"The path '/visibility/post/{uid}' is invalid."}}, 404
    
    
    datapath = pathes.visiprod + uid + pathes.suff


    req = request.json
    with open(datapath, mode="a", encoding="utf-8") as f:
        json.dump(req, f,  ensure_ascii=False)
        f.write("\n")
    
    return req


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5050, debug=True)