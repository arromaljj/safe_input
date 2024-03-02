import torch  # Often needed for model usage 
from transformers import AutoModelForCausalLM, AutoTokenizer

# Customization Point 1: Access Token (if necessary)
# access_token = "hf_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"  # Replace with your Hugging Face token if required

# Load model and tokenizer
model = AutoModelForCausalLM.from_pretrained("cognitivecomputations/Wizard-Vicuna-13B-Uncensored", cache_dir="./.cache")
tokenizer = AutoTokenizer.from_pretrained("cognitivecomputations/Wizard-Vicuna-13B-Uncensored", cache_dir="./.cache")

# Ensure the model is on the appropriate device (CPU or GPU if available)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)



from fastapi import FastAPI, Body
from pydantic import BaseModel

class InputData(BaseModel):
    prompt: str


app = FastAPI()


def generate(prompt: str):
    inputs = tokenizer(prompt, return_tensors="pt").to(device)
    output = model.generate(**inputs, max_new_tokens=50, do_sample=True)
    generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

    return {"generated_text": generated_text }



@app.post("/") 
def generate_text(data: InputData = Body(...)):  
    prompt = data.prompt


    return {"generated": generate(prompt)}

if __name__ == '__main__':
    import uvicorn  
    uvicorn.run(app, host="0.0.0.0", port=8000)