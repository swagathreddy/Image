from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import io
import base64

model_id = "stabilityai/sd-turbo"  # Lightweight fast model

device = "cuda" if torch.cuda.is_available() else "cpu"

pipe = StableDiffusionPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32,
    safety_checker=None
)
pipe = pipe.to(device)
pipe.enable_attention_slicing()

def generate_image_base64(prompt: str):
    print("[ImageGen] Prompt:", prompt)
    with torch.inference_mode():
        image = pipe(prompt, num_inference_steps=15, guidance_scale=5.0).images[0]

    buffered = io.BytesIO()
    image.save(buffered, format="PNG")
    base64_img = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return base64_img
