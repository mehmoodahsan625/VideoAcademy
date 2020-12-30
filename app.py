import os,glob, fnmatch
from flask import Flask, request, render_template, redirect, request,session,Response,logging,Blueprint,url_for,request,jsonify,abort,make_response

import flask
from moviepy.editor import *
import pyodbc

app = Flask(__name__)


cnxn_str = ("DRIVER={SQL Server};"
            "Server=WIN-2K8ESS\WIN2K8ESS;"
            "Database=VideoAcademy;"
            "UID=sa;"
            "PWD=ess@123;")

cnxn = pyodbc.connect(cnxn_str)
cursor = cnxn.cursor()



@app.route("/")
def index():
    cursor.execute(''' SELECT * FROM projectvideoclips WHERE VideoId = 61 ''')
    results = cursor.fetchall()
    # name = results.StartTime
    # name1 = results.EndTime
    # print(name,name1)
    for x in results:
        print(x.StartTime,x.EndTime)
    return render_template('index.html')


@app.route("/edit_videos")
def edit_videos():
    time = []
    cursor.execute(''' SELECT * FROM projectvideos WHERE id = 2 ''') 
    data = cursor.fetchone()
    vid_id = data.Url


    cursor.execute(''' SELECT * FROM projectvideoclips WHERE VideoId = 58 ''')
    results = cursor.fetchall()
    # name = results.StartTime
    # name1 = results.EndTime
    # print(name,name1)
    # for x in results:
        # print(x.StartTime,x.EndTime)

    # clip = VideoFileClip("{0}".format(vid_id))
    clip = VideoFileClip("https://azuresquarevfiles.blob.core.windows.net/videoacademyfiles/Test%20title%20of%20project_11/20201119025223586.mp4")
    # clip = VideoFileClip("./static/projects/{0}/{1}/Clips/{2}".format(u_id,proj_name,video_file))
    for x in results:
        clip1 = clip.subclip(float(x.StartTime),float(x.EndTime))
        time.append(clip1)
    # clip1.save_frame("D:/Python projects/home/static/projects/{1}/{0}/subclips/Thumbnail/{2}.jpg".format(proj_id,user_id,sub_id) , t=end_time)
    # clip1.write_videofile("outVideos1.mp4")
    # clip1 = VideoFileClip("outVideos.mp4")
    # clip2 = VideoFileClip("outVideos1.mp4")
    video = concatenate_videoclips([*time])
    video.write_videofile('final.mp4')

edit_videos()     

     
if __name__ == '__main__':
    app.run(debug=True)
