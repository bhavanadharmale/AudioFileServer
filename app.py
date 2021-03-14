import datetime
import os
from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import logging
import json
from sqlalchemy import delete

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+pymysql://root:@localhost/flask"
app.config['SECRET_KEY'] = "random"

db = SQLAlchemy(app)


class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    songName = db.Column(db.String(100))
    durationSec = db.Column(db.Integer)
    uploadedTime = db.Column(db.DateTime, default=datetime.datetime.utcnow)


    def __init__(self, id, songName, durationSec, uploadedTime):
        self.id = id
        self.songName = songName
        self.durationSec = durationSec
        self.uploadedTime = uploadedTime

class Podcast(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    podcastName = db.Column(db.String(100))
    durationSec = db.Column(db.Integer)
    uploadedTime = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    host = db.Column(db.String(100))
    participants = db.Column(db.String(100))

    def __init__(self, id, podcastName, durationSec, uploadedTime, host, participants=None):
        self.id = id
        self.podcastName = podcastName
        self.durationSec = durationSec
        self.uploadedTime = uploadedTime
        self.host = host
        self.participants = participants

class Audiobook(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    author = db.Column(db.String(100))
    narrator = db.Column(db.String(100))
    durationSec = db.Column(db.Integer)
    uploadedTime = db.Column(db.DateTime, default=datetime.datetime.utcnow)


    def __init__(self, id, title, author, narrator, durationSec, uploadedTime):
        self.id = id
        self.title = title
        self.author = author
        self.narrator = narrator
        self.durationSec = durationSec
        self.uploadedTime = uploadedTime


def getClassName(audioFileType):
    if audioFileType == "Song":
        return Song
    elif audioFileType == "Podcast":
        return Podcast
    elif audioFileType == "Audiobook":
        return Audiobook

@app.route('/create/<audioFileType>', methods=['POST'])
def create(audioFileType):

    if request.method == "POST":
        request_data = request.get_json()
        id = int(request_data["ID"])
        result = getClassName(audioFileType).query.filter_by(id=id).all()

        if not result:
            if audioFileType == "Song":
                songName = request_data["songName"]
                durationSec = int(request_data["durationSec"])
                uploadedTime =datetime.datetime.utcnow()
                insertionOp = Song(id, songName, durationSec, uploadedTime)
                db.session.add(insertionOp)
                db.session.commit()

                return "Action is successful: 200 OK"

            elif audioFileType == "Podcast":
                podcastName = request_data["podcastName"]
                durationSec = int(request_data["durationSec"])
                uploadedTime = datetime.datetime.utcnow()
                host = request_data["host"]
                participants = request_data["participants"]
                insertionOp = Podcast(id, podcastName, durationSec, uploadedTime, host, participants)
                db.session.add(insertionOp)
                db.session.commit()

                return "Action is successful: 200 OK"

            elif audioFileType == "Audiobook":
                title = request_data["title"]
                author = request_data["author"]
                narrator = request_data["narrator"]
                durationSec = int(request_data["durationSec"])
                uploadedTime = datetime.datetime.utcnow()
                insertionOp = Audiobook(id, title, author, narrator, durationSec, uploadedTime)
                db.session.add(insertionOp)
                db.session.commit()

                return "Action is successful: 200 OK"

            return "Any error: 500 internal server error"
        else:
            return "The request is invalid: 400 bad request"
    else:
        return "Any error: 500 internal server error"


@app.route('/delete/<audioFileType>/<audioFileID>', methods=['POST'])
def delete(audioFileType, audioFileID):
    if request.method == "POST":
        audioFileID = int(audioFileID)
        result = getClassName(audioFileType).query.filter_by(id=audioFileID).all()
        if result:
            r = getClassName(audioFileType).query.filter_by(id=audioFileID).delete()
            db.session.commit()
            return "Action is successful: 200 OK"
        else:
            return "The request is invalid: 400 bad request"
    else:
        return "Any error: 500 internal server error"


@app.route('/update/<audioFileType>/<audioFileID>', methods=['POST'])
def update(audioFileType, audioFileID):
    if request.method == "POST":
        audioFileID = int(audioFileID)
        request_data = request.get_json()
        result = getClassName(audioFileType).query.filter_by(id=audioFileID).all()
        if result:
            if audioFileType == "Song":

                for x in result:
                    if "songName" in request_data.keys():
                        songName = request_data["songName"]
                    else:
                        songName = x.songName

                    if "durationSec" in request_data.keys():
                        durationSec = int(request_data["durationSec"])
                    else:
                        durationSec = int(x.durationSec)

                r = getClassName(audioFileType).query.filter_by(id=audioFileID).update({Song.songName:songName, Song.durationSec:durationSec},
                                                                  synchronize_session=False)
                db.session.commit()

                return "Action is successful: 200 OK"

            elif audioFileType == "Podcast":

                for x in result:
                    if "podcastName" in request_data.keys():
                        podcastName = request_data["podcastName"]
                    else:
                        podcastName = x.podcastName

                    if "durationSec" in request_data.keys():
                        durationSec = int(request_data["durationSec"])
                    else:
                        durationSec = int(x.durationSec)

                    if "host" in request_data.keys():
                        host = request_data["host"]
                    else:
                        host = x.host

                    if "participants" in request_data.keys():
                        participants = request_data["participants"]
                    else:
                        participants = x.participants



                getClassName(audioFileType).query.filter_by(id=audioFileID).update({Podcast.podcastName: podcastName,
                                                                   Podcast.durationSec: durationSec,
                                                                   Podcast.host: host,
                                                                   Podcast.participants: participants},
                                                                  synchronize_session=False)
                db.session.commit()
                return "Action is successful: 200 OK"

            elif audioFileType == "Audiobook":

                for x in result:
                    if "title" in request_data.keys():
                        title = request_data["title"]
                    else:
                        title = x.title

                    if "author" in request_data.keys():
                        author = request_data["author"]
                    else:
                        author = x.author

                    if "narrator" in request_data.keys():
                        narrator = request_data["narrator"]
                    else:
                        narrator = x.narrator

                    if "durationSec" in request_data.keys():
                        durationSec = int(request_data["durationSec"])
                    else:
                        durationSec = int(x.durationSec)

                getClassName(audioFileType).query.filter_by(id=audioFileID).update({Audiobook.title: title,
                                                                   Audiobook.author: author,
                                                                   Audiobook.narrator: narrator,
                                                                   Audiobook.durationSec: durationSec},
                                                                  synchronize_session=False)
                db.session.commit()
                return "Action is successful: 200 OK"

        else:
            return "The request is invalid: 400 bad request"

    else:
        return "Any error: 500 internal server error"


@app.route('/get/<audioFileType>', methods=['POST'])
@app.route('/get/<audioFileType>/<audioFileID>', methods=['POST'])
def getData(audioFileType, audioFileID=False):
    if request.method == "POST":

        if audioFileID:
            result = getClassName(audioFileType).query.filter_by(id=audioFileID).all()
        else:
            result = getClassName(audioFileType).query.all()

        if result:
            outputList = list()
            if audioFileType == 'Song':

                for x in result:
                    outputDict = dict()
                    outputDict["ID"] = x.id
                    outputDict["songName"] = x.songName
                    outputDict["durationSec"] = x.durationSec
                    date_time = x.uploadedTime.strftime("%m/%d/%Y, %H:%M:%S")
                    outputDict["uploadedTime"] = date_time
                    outputList.append(outputDict)

            elif audioFileType == 'Podcast':

                for x in result:
                    outputDict = dict()
                    outputDict["ID"] = x.id
                    outputDict["podcastName"] = x.podcastName
                    outputDict["durationSec"] = x.durationSec
                    date_time = x.uploadedTime.strftime("%m/%d/%Y, %H:%M:%S")
                    outputDict["uploadedTime"] = date_time
                    outputDict["host"] = x.host
                    outputDict["participants"] = x.participants
                    outputList.append(outputDict)

            elif audioFileType == 'Audiobook':
                for x in result:
                    outputDict = dict()
                    outputDict["ID"] = x.id
                    outputDict["title"] = x.title
                    outputDict["author"] = x.author
                    outputDict["narrator"] = x.narrator
                    outputDict["durationSec"] = x.durationSec
                    date_time = x.uploadedTime.strftime("%m/%d/%Y, %H:%M:%S")
                    outputDict["uploadedTime"] = date_time
                    outputList.append(outputDict)
            return json.dumps(outputList)
        else:
            return "The request is invalid: 400 bad request"

    return "500 internal server error"


if __name__ == '__main__':
    db.create_all()
    app.run()
