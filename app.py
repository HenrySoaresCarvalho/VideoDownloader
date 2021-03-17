try:
    from pytube import YouTube
    from flask import Flask,jsonify,request,send_file

except:
    from packageInstaller import package_installer
    depedencies = ["flask","pytube"]
    package_installer(depedencies)


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


if __name__ == "__main__":
    app.run(debug=True)
