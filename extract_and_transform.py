import json
from config import GeminiAPI
import pymupdf

if __name__ == "__main__":
    gapi = GeminiAPI(__file__)

    def pdf_to_text(pdf_path: str):
        with open(pdf_path, 'rb') as f:
            reader = pymupdf.open(f)
            text = ""
            for page in reader[5:7]:
                text += page.get_text() + "\n"
        return text

    pdf_str = pdf_to_text(gapi.pdf_path)

    response = gapi.send_message(pdf_str=pdf_str)
    json_str = response.text.replace("json", "").replace("```", "")
    print(json_str)
    print(f"beneficial owner 1 full name : {json.loads(json_str)['beneficial_owner_1']['full_name']}")