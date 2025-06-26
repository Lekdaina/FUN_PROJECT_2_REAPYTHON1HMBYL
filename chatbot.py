from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import pipeline

# Load model hanya sekali
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

# Pipeline chatbot
chatbot = pipeline("text-generation", model=model, tokenizer=tokenizer)

def get_response(user_input):
    try:
        inputs = tokenizer.encode(user_input + tokenizer.eos_token, return_tensors="pt")
        output = model.generate(inputs, max_length=1000, pad_token_id=tokenizer.eos_token_id)
        reply = tokenizer.decode(output[:, inputs.shape[-1]:][0], skip_special_tokens=True)
        return reply
    except Exception as e:
        return f"❌ Terjadi error: {e}"