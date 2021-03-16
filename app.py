from pytube import YouTube
import os
import random
from flask import Flask,request,jsonify,send_file

app = Flask(__name__)
files = []

@app.route("/")
def home():
	return jsonify({
		"creator":"Henry Soares de Carvalho",
		"Version": 0.1,
		"name":"Simple Video Downloader API"
	})

@app.route("/video/info",methods=["POST"])
def get_info():
	try:
		req = request.get_json()
		yt = YouTube(req["link"])
		return jsonify({
			"video_name": yt.title,
			"video_views": yt.views,
			"author":yt.author
		})
	except:
		return jsonify({
			"message":"error"
		})

@app.route("/video/download",methods=["POST"])
def download_file():
	try:
		req = request.get_json()
		yt = YouTube(req["link"])
		ys = yt.streams.first()
		file_name = file_namer()
		ys.download(filename=file_name,output_path="./videos")

		return jsonify({
			"status":"Downloaded",
			"video_id": file_name
		})
	except:
		return jsonify({"status":"failed"})

@app.route("/video/get/<video_id>")
def get_video(video_id):
	return send_file(f"./videos/{video_id}.mp4")

def download(link:str)-> dict:
	try:
		yt = YouTube(link)
		ys = yt.streams.get_highest_resolution()
		ys.download("")

		return {"message":"sucess","status":200}
	except:
		return {"message":"failed"}

@app.route("/video/delete/<video_id>", methods=["DELETE"])
def delete_video(video_id):
	os.remove(f"./videos/{video_id}.mp4")
	return jsonify({
		"message":"sucess"
	})

def file_namer() -> str:
	template = ""
	for i in range(0,12):
		template = f"{random.randint(0,9)}" + template
	
	return template

if __name__ == "__main__":
	app.run(debug=True)