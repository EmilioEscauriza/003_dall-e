from dotenv import load_dotenv
import os
from openai import OpenAI
import requests
from PIL import Image
from io import BytesIO

# Load api key from .env file
load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

# Create client
client = OpenAI(api_key=openai_api_key)

# input prompt
with open("prompt.txt", "r", encoding="utf-8") as file:
    prompt = file.readlines()[0]

# Generate image
response = client.images.generate(
    model="dall-e-3",
    prompt=prompt,
    size="1792x1024",
    n=1,
)

# Download and save image
image_url = response.data[0].url
image_data = requests.get(image_url).content

# Optional: view in script
img = Image.open(BytesIO(image_data))
img.show()  # This opens the image in the system default viewer

# Optional: save to file
# Generate a filename like "card_1.png", "card_2.png", etc.
i = 1
while os.path.exists(f"output_images/card_{i}.png"):
    i += 1
filename = f"output_images/card_{i}.png"

# Save image to that file
with open(filename, "wb") as f:
    f.write(image_data)

print(f"Saved as {filename}")