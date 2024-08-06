from werkzeug.utils import secure_filename
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
from PIL import Image, ImageDraw, ImageFont
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from forms import UploadForm
# with Image.open("./images/Capture.png") as img:
#     img = img.resize((800, 600))  # Adjust the size as needed
#     img.save("./images/Capture_resized.png")


# font_path = 'Roboto-Regular.ttf'
# font_size = 72
# myFont = ImageFont.truetype("arial.ttf", 36)
# img = Image.open('./images/Capture_resized.png')
# I1 = ImageDraw.Draw(img)
# I1.text((400, 300),  "Watermark!!", font=myFont, fill=(0, 0, 0))
# img.show()
# img.save("./images/Capture_watermarked.png")


# def add_watermark(input_image_path, output_image_path, watermark_text):
#     # Open the original image
#     original = Image.open(input_image_path)
#     width, height = original.size

#     # Make the image editable
#     txt = Image.new('RGBA', original.size, (255, 255, 255, 0))

#     # Choose a font and size
#     # You can use a different font if desired
#     font = ImageFont.truetype("arial.ttf", 36)

#     # Initialize ImageDraw
#     draw = ImageDraw.Draw(txt)

#     # Position the text at the bottom right corner
#     text_width, text_height = draw.textsize(watermark_text, font)
#     x = width - text_width - 10
#     y = height - text_height - 10

#     # Add the text to the image
#     draw.text((x, y), watermark_text, fill=(255, 255, 255, 128), font=font)

#     # Combine the original image with the watermark
#     watermarked = Image.alpha_composite(original.convert('RGBA'), txt)

#     # Save the result
#     watermarked.convert('RGB').save(output_image_path, "PNG")


# # Example usage
# input_image_path = "./images/Capture.png"
# output_image_path = "./images/Capture_watermarked.png"
# watermark_text = "Wenqian's Water Mark"

# add_watermark(input_image_path, output_image_path, watermark_text)


# app.py or main.py

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'uploads')
app.config['SAVE_FOLDER'] = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), 'saved')
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB max file size

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        file = form.image.data
        print(file)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('upload_success', filename=filename))
    return render_template('index.html', form=form)


@app.route('/upload_success')
def upload_success():
    filename = request.args.get('filename')
    with Image.open(f"{app.config['UPLOAD_FOLDER']}/{filename}") as img:
        img = img.resize((800, 600))  # Adjust the size as needed
        # img.save("./images/Capture_resized.png")

        font_path = 'Roboto-Regular.ttf'
        font_size = 72
        myFont = ImageFont.truetype("arial.ttf", 36)
        # img = Image.open('./images/Capture_resized.png')
        I1 = ImageDraw.Draw(img)
        I1.text((400, 300),  "Watermark!!", font=myFont, fill=(0, 0, 0))
        # img.show()
        img_path = f"{app.config['SAVE_FOLDER']}{filename}"
        img.save(f"{app.config['SAVE_FOLDER']}/{filename}")
        return render_template('success.html', image_path=img_path, filename=filename)


@app.route('/download/<filename>')
def download(filename):
    # if not current_user.is_authenticated:
    #     return app.login_manager.unauthorized()
    file_path = f"{app.config['SAVE_FOLDER']}"
    print(f"Serving file from: {file_path}")
    return send_from_directory(file_path,
                               filename)


if __name__ == "__main__":
    app.run(debug=True)
