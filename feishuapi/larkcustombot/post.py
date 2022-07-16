

def content_text(text, un_escape=False):
    content_text = {
        "tag": "text",
        "text": text,
        "un_escape": un_escape
    }

    return content_text


def content_a(href, text):

    content_a = {
        "tag": "a",
        "href": href,
        "text": text
    }
    return content_a


def content_at(user_id, user_name):

    content_at = {
        "tag": "at",
        "user_id": user_id,
        "user_name": user_name
    }

    return content_at


def content_imag(image_key, width=None, height=None):
    content_imag = {
        "tag": "img",
        "image_key": image_key,
        "width": width,
        "height": height
    }
    return content_imag
