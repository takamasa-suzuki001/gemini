import os
from dotenv import load_dotenv
import google.generativeai as genai

class GeminiAPI():
    def __init__(self, module_name: str):
        load_dotenv()
        genai.configure(api_key=os.environ["GEMINI_API_KEY"])

        self.base_dir = os.path.dirname(os.path.abspath(module_name))
        self.prompts_dir = os.path.join(self.base_dir, 'prompts')
        self.files_dir = os.path.join(self.base_dir, 'files')
        self.pdf_path = os.path.join(self.files_dir, "Institutional_Account_Application_Form.pdf")

        generation_config = {
            "temperature": 1,
            "top_p": 0.95,
            "top_k": 64,
            "max_output_tokens": 8192,
            "response_mime_type": "text/plain",
        }

        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-pro",
            generation_config=generation_config,
        )
        self.prompt_txt = os.path.splitext(os.path.basename(module_name))[0]
    
    def upload_to_gemini(self, path: str, mime_type=None):
        return genai.upload_file(path, mime_type=mime_type)
    
    def send_message(self, files=[], pdf_str=None):
        history = []
        if len(files) > 0:
            parts = []
            for f in files:
                parts.append(f)
            history.append({"role": "user", "parts": parts})
            
        self.chat_session = self.model.start_chat(history=history)
        prompt_path = os.path.join(self.prompts_dir, f"{self.prompt_txt}.txt")
        with open(prompt_path, "r") as p:
            prompt_content = p.read()
            if pdf_str:
                prompt_content += f"\n{pdf_str}"
            return self.chat_session.send_message(prompt_content)