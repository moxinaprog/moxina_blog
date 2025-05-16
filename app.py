
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

posts = [
    {
        'id': 1,
        'title': 'Flayerlar',
        'content': 'Bu yerda men yaratgan flayer dizaynlarini ko‘rishingiz mumkin. Har bir flayer muayyan maqsadga yo‘naltirilgan va grafik jihatdan yuksak darajada ishlab chiqilgan.',
        'created': datetime(2025, 5, 8),
        'image': 'post_images/rasm1.png'
    },
    {
        'id': 2,
        'title': 'Vizitkalar',
        'content': 'Vizitkalar — professional ko‘rinishingizning bir qismi. Bu postda men tayyorlagan vizitka namunalarini ko‘rishingiz mumkin. Minimalist va zamonaviy uslubda.',
        'created': datetime(2025, 5, 7),
        'image': 'post_images/rasm2.png'
    }
]

@app.context_processor
def inject_year():
    return {'current_year': datetime.now().year}

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    post = next((p for p in posts if p['id'] == post_id), None)
    if post:
        return render_template('post_detail.html', post=post)
    else:
        return "Post topilmadi", 404

if __name__ == '__main__':
    app.run(debug=True)
