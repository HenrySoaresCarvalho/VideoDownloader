try:
    from pytube import YouTube
    from flask import Flask,jsonify,send_file

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

if __name__ == "__main__":
    app.run(debug=True)
