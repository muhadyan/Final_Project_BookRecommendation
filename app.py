from flask import Flask, render_template, request, send_from_directory
import save_model as sm

app = Flask(__name__)

@app.route('/', methods = ['POST', 'GET'])
def home():
    if request.method == 'POST':
        return render_template('home.html')
    else:
        return render_template('home.html')

@app.route('/rekomendasi', methods = ['POST', 'GET'])
def rekomendasi():
    if request.method == 'POST':
        input = request.form

        favorit = sm.buku_favorit(input['judul']).iloc[0]
        img_fav = favorit['image_url']

        rek_buku = sm.rekomendasi_buku(input['judul'])
        img_buku = []
        for i in rek_buku:
            img_buku.append(i['image'])

        rek_genre = sm.rekomendasi_genre(input['judul'])
        img_genre = []
        for i in rek_genre:
            img_genre.append(i['image'])
        
        rek_author = sm.rekomendasi_author(input['judul'])
        img_author = []
        for i in rek_author:
            img_author.append(i['image'])

        return render_template('rekomendasi.html',
            input=input, favorit=favorit, img_fav=img_fav,
            len_gen=len(rek_genre), rek_genre=rek_genre, img_genre=img_genre,
            rek_author=rek_author, img_author=img_author,
            rek_buku=rek_buku, img_buku=img_buku)

@app.route('/images/<path:path>')
def static_file(path):
    return send_from_directory('images', path)

if __name__ == "__main__":
    app.run(debug=True)