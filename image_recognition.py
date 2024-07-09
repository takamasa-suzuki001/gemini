
import os
import json
from config import GeminiAPI
from pdf2image import convert_from_path

if __name__ == "__main__":
    gapi = GeminiAPI(__file__)

    def pdf_to_png(pdf_path: str, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        pages = convert_from_path(pdf_path)

        for i, page in enumerate(pages):
            if i in range(5, 7):
                image_name = f"page_{i+1}.png"
                image_path = os.path.join(output_dir, image_name)
                page.save(image_path, "PNG")

    output_dir = os.path.join(gapi.files_dir, "output_pngs/")
    pdf_to_png(gapi.pdf_path, output_dir=output_dir)
    files = [
        gapi.upload_to_gemini(os.path.join(output_dir, "page_6.png"), mime_type="image/png"),
        gapi.upload_to_gemini(os.path.join(output_dir, "page_7.png"), mime_type="image/png")
    ]

    response = gapi.send_message(files)
    json_str = response.text.replace("json", "").replace("```", "")
    print(json_str)
    print(f"beneficial owner 1 full name : {json.loads(json_str)["beneficial_owner_1"]["full_name"]}")