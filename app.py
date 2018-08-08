from flask import Flask, render_template, request
import pafy


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("index.html")


@app.route("/info", methods = ['POST', 'GET'])
def download():
    if request.method == 'POST':
        url = request.form["url"]
        video = pafy.new(url)
        stream = video.streams
        st_url = []
        st_res = []
        st_ext = []
        st_size =[]


        for s in stream:
            st_url.append(s.url)
            st_res.append(s.resolution)
            st_ext.append(s.extension)
            st_size.append(s.get_filesize())


        return render_template('video.html', title=video.title, desc=video.description, author= video.author, img=video.thumb,li_do=zip(st_url,st_res,st_ext,st_size))


if __name__ == "__main__":

    port = int(os.environ.get("PORT", 33507))
    app.run(host='0.0.0.0', port=port)
