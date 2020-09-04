import os
import secrets

from flask import current_app
from PIL import Image

from flask_mail import Message
from flaskblog import mail, celery_app


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, "static/profile_pics", picture_fn
    )

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn


@celery_app.task
def send_reset_email(email, url):
    msg = Message(
        "Password Reset Request", sender="noreply@demo.com", recipients=[email]
    )
    msg.body = f"""To reset your password, visit the following link:
{url}

If you did not make this request then simply ignore this email and no changes will be made.
"""
    mail.send(msg)

