#!/usr/bin/python
#coding:utf-8
import tornado.ioloop
import tornado.web
from tornado import web,gen,httpclient
import StringIO
import base64
import face_recognition
import os
class Handler(tornado.web.RequestHandler):
    def get(self):
        self.render("facelogin.html")
class ImgHandler(tornado.web.RequestHandler):
    def post(self):
        myimg=self.get_argument('myimg')
        tmpimg = StringIO.StringIO(base64.b64decode(myimg))
        dyzimg = face_recognition.load_image_file(tmpimg)
        tmpcode = face_recognition.face_encodings(dyzimg)
        if not tmpcode :
            self.write('face')
            self.finish()
	else:
            path='/root/known_people/'
            imglib=os.listdir(path)
            imglabels=[]
            imgcode=[]
            for name in imglib:
                loadimg=face_recognition.load_image_file(path+name)
                loadcode = face_recognition.face_encodings(loadimg)
                imglabels.append(name[:-4]) 
                imgcode.append(loadcode[0])
            res=face_recognition.compare_faces(imgcode,tmpcode[0],0.4)
            if True in res:
	        location=res.index(True)
                self.write(imglabels[location])
            else:
	        self.write('Unknown')
def make_app():
    return tornado.web.Application([
        (r"/", Handler),
        (r"/saveImg", ImgHandler),
    ])
if __name__ == "__main__":
    app = make_app()
    app.listen(666)
    tornado.ioloop.IOLoop.current().start()
