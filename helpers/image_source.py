import base64
import mimetypes

def create_image_message(image_path):
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()

        base64_encoded_data = base64.b64encode(binary_data)

        base64_string = base64_encoded_data.decode('utf-8')

        mime_type, _ = mimetypes.guess_type(image_path)

        image_block = {
            "type": "image",
            "source" : {
                "type" : "base64",
                "media_type" : mime_type,
                "data" : base64_string
            }
        }
        
        return image_block