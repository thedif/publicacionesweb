from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    posts = []
    for key in request.files:
        if key.startswith('image_'):
            idx = key.split('_')[1]
            image = request.files[key]
            copy_text = request.form.get(f'copy_{idx}', '')
            if image.filename:
                posts.append((image, copy_text))

    if not posts:
        return 'No se subieron imágenes', 400

    pdf = FPDF()
    temp_dir = tempfile.mkdtemp()
    idx = 1
    for image, text in posts:
        pdf.add_page()
        ext = os.path.splitext(image.filename)[1]
        img_path = os.path.join(temp_dir, f'image_{idx}{ext}')
        image.save(img_path)
        pdf.image(img_path, x=10, y=10, w=100)
        pdf.set_xy(10, 120)
        pdf.set_font('Arial', size=12)
        pdf.multi_cell(0, 10, text)
        idx += 1

    pdf_path = os.path.join(temp_dir, 'plan.pdf')
    pdf.output(pdf_path)

    return send_file(pdf_path, as_attachment=True, download_name='plan_publicaciones.pdf')

if __name__ == '__main__':
    app.run(debug=True)
