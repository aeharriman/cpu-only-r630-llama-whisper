from transformers import AutoModelForCausalLM, AutoTokenizer
import ipex_llm as ipex
import torch

def generate_text(prompt):
    model_path = "./llama3_model"  # Local path to your downloaded model
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)

    model = ipex.optimize(model.eval())

    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=100)

    return tokenizer.decode(outputs[0], skip_special_tokens=True)

if __name__ == "__main__":
    prompt = "What is artificial intelligence?"
    generated_text = generate_text(prompt)
    print(generated_text)
