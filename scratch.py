# Required Libraries
import os
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import psutil
import ipex_llm as ipex  # Using ipex_llm specifically for large language models
from torch.quantization import quantize_dynamic

# Define Paths
model_path = "./llama3_model"
optimized_model_path = "./llama3_optimized_model"

# Resource Monitoring Function
def monitor_resources(stage=""):
    print(f"\n{stage}")
    print(f"CPU usage: {psutil.cpu_percent()}%")
    print(f"Memory usage: {psutil.virtual_memory().percent}%")
    print(f"Available memory: {psutil.virtual_memory().available // (1024 ** 2)} MB")
    print(f"Swap usage: {psutil.swap_memory().percent}%")

# Load and Optimize Model
def load_and_optimize_model():
    # Check if the optimized model already exists
    if os.path.exists(optimized_model_path):
        print("Loading optimized model...")
        model = AutoModelForCausalLM.from_pretrained(optimized_model_path)
    else:
        print("Loading and optimizing model for the first time...")
        model = AutoModelForCausalLM.from_pretrained(model_path)

        # Apply dynamic quantization and ipex_llm optimization
        model = quantize_dynamic(model, {torch.nn.Linear}, dtype=torch.qint8)
        model = ipex.optimize(model.eval())  # Using ipex_llm's optimize for LLMs
        
        # Save optimized model for future use
        model.save_pretrained(optimized_model_path)

    return model

# Generate Text Function
def generate_text(prompt, tokenizer, model):
    inputs = tokenizer(prompt, return_tensors="pt")
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=100)
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

# Main Execution
if __name__ == "__main__":
    # Initialize and load tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = load_and_optimize_model()

    # Monitor resources before and after text generation
    prompt = "What is AI?"
    monitor_resources("Resources before running generate_text function:")
    print(generate_text(prompt, tokenizer, model))
    monitor_resources("Resources after running generate_text function:")
