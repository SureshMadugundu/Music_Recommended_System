from flask import Flask,request,url_for,render_template,send_from_directory,flash, redirect
from jinja2 import Markup
import numpy as np
import pandas as pd
import pickle
import os


df1=pickle.load(open('df1.pkl','rb'))

similarity=pickle.load(open('similarity.pkl','rb'))


def recommendation(song):
    idx=df1[df1['song']==song].index[0]
    distances=sorted(list(enumerate(similarity[idx])),reverse=False,key=lambda x:x[1])
    songs=[]
    for i in distances[1:20]:
        songs.append(df1.iloc[i[0]].song)
        
    return songs


app=Flask(__name__)

@app.route('/')





def index():
    names=list(df1['song'].values)
    return render_template('index1.html',name=names)


@app.route('/recom',methods=["POST","GET"])
def mysong():
    user_song=request.form['names']
    songs= recommendation(user_song)

    return render_template('index1.html',songs=songs)


@app.route('/audio/<path:filename>')
def serve_audio(filename):
    audio_folder = 'static/audio_files'  # Update with the actual path to your audio folder
    return send_from_directory(audio_folder,filename)



@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return redirect(request.url)
    
    file = request.files['file']
    
    if file.filename == '':
        return redirect(request.url)
    
    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        return 'File uploaded successfully!'





if __name__ == '__main__':
    app.run(debug=True)
