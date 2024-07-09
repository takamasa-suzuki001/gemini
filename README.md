# Gemini API for Application Form

## 1. Build the image
```docker build . -t gemini```

## 2. Create an .env file in the project root directory and add an API Key of Gemini API
```
touch .env
```
```
GEMINI_API_KEY=<GEMINI_API_KEY>
```

## 3. Edit prompt texts as you want to try in the ```/prompt``` directory

## 4. Execute the script which you want to try
### when executing extract_and_transform.py
```
docker run \
  -v ./files/output_pngs:/app/files/output_pngs \
  -v ./prompts:/app/prompts \
  -it gemini
  extract_and_transform.py
```
or
```
docker run \
  -v ./files/output_pngs:/app/files/output_pngs \
  -v ./prompts:/app/prompts \
  -it gemini
```

### when executing image_recognition.py
```
docker run \
  -v ./files/output_pngs:/app/files/output_pngs \
  -v ./prompts:/app/prompts \
  -it gemini
  image_recognition.py
```