try:
    from pytube import YouTube
    from flask import Flask,jsonify,request,send_file

except:
    from packageInstaller import package_installer
    depedencies = ["flask","pytube"]
    package_installer(depedencies)

from fileNamer import file_namer
import os

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "message":"Simple Download API with Flask and Pytube!",
        "creator":"Henry Soares de Carvalho",
        "version": 0.1
    })

@app.route("/video/info", methods=["POST"])
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
		file_name = file_namer(12)
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

@app.route("/video/delete/<video_id>", methods=["DELETE"])
def delete_video(video_id):
	os.remove(f"./videos/{video_id}.mp4")
	return jsonify({
		"message":"sucess"
	})

if __name__ == "__main__":
    app.run(debug=True)
