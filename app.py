import os,glob, fnmatch
from flask import Flask, request, render_template, redirect, request,session,Response,logging,Blueprint,url_for,request,jsonify,abort,make_response
from flask_sqlalchemy import SQLAlchemy
import flask
from moviepy.editor import *
# import json


# from datetime import timedelta
# from config import secret_key
# from datetime import datetime
# import glob
# from time import sleep
# import time
# import asyncio
# from tqdm import tqdm
# import subprocess
# import sys
# import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/edit_videos")
def edit_videos():
    clip = VideoFileClip("https://azuresquarevfiles.blob.core.windows.net/videoacademyfiles/Test%20title%20of%20project_11/20201119025223586.mp4")
    # clip = VideoFileClip("./static/projects/{0}/{1}/Clips/{2}".format(u_id,proj_name,video_file))
    clip1 = clip.subclip(5,10)
    # clip1.save_frame("D:/Python projects/home/static/projects/{1}/{0}/subclips/Thumbnail/{2}.jpg".format(proj_id,user_id,sub_id) , t=end_time)
    # clip1.write_videofile("outVideos1.mp4")
    clip1 = VideoFileClip("outVideos.mp4")
    clip2 = VideoFileClip("outVideos1.mp4")
    video = concatenate_videoclips([clip1,clip2])
    video.write_videofile('final.mp4')

# edit_videos()     

     
if __name__ == '__main__':
    app.run(debug=True)
