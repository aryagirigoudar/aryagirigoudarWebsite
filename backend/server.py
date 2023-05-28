from flask import Flask
from flask_cors import CORS
import data 

dataobj = data.get_from_my_profiles

server = Flask(__name__)

@server.route("/api/githubrepos", methods=["GET"])
def github_repos():
    return dataobj.get_data()

