from flask import Flask, render_template, request
import kissanimedl, config
app = Flask(__name__)
s = kissanimedl.Scraper()

@app.route('/', methods=['GET'])
def main():


@app.route('/', methods=['POST'])
def demontrateDownloads():
    url = request.form['url']
    data = s.GetEpisodeLinks(url)
    return render_template('post.html', )

@app.route('/downloaded')
def showDownloaded():
    
