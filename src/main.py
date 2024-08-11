

API="AIzaSyAVE_Ie7OOl_Bbiq5FDrvB2p_mtVbPJrGM"

import time
import google.generativeai as genai
import PIL.Image

genai.configure(api_key=API)

def generate_content_with_retry(model, prompt, image, max_retries=3, delay=60):
    for attempt in range(max_retries):
        try:
            response = model.generate_content([prompt, image])
            return response.text
        except Exception as e:
            if "RATE_LIMIT_EXCEEDED" in str(e) and attempt < max_retries - 1:
                print(f"Rate limit exceeded. Waiting for {delay} seconds before retrying...")
                time.sleep(delay)
            else:
                raise e

try:
    img = PIL.Image.open('vue-project/chickern.jpg')
    print("Image loaded successfully")
    
    model = genai.GenerativeModel(model_name="gemini-1.5-flash")
    result = generate_content_with_retry(model, "What is in this photo?", img)
    print(result)
except Exception as e:
    print(f"An error occurred: {str(e)}")