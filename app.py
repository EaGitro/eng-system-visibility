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
    suff = "data.jsonl"
    prod = "product"
    test = "test"
    visi = f"{data}visi-"
    visitest = f"{visi}-{test}-{suff}"
    visiprod = f"{visi}-{prod}-{suff}"


@app.route("/health")
def health():
    return "ok"



@app.route("/visibility/post/<string:mode>", methods=["POST"])
def visibility_post(mode):
    if mode == "product":
        datapath = pathes.visiprod
    elif mode == "test":
        datapath = pathes.visitest
    else:
        return {"error": {"type": "InvalidPath", "message": f"The path '/visibility/post/{mode}' is invalid. Valid paths are '/visibility/post/product' or '/visibility/post/test'"}}, 404
    
    req = request.json
    with open(datapath, mode="a", encoding="utf-8") as f:
        json.dump(req, f,  ensure_ascii=False)
        f.write("\n")
    
    return req