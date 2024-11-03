from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "meta-llama/Meta-Llama-3-8B"

# Download and save the model locally
model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir="./llama3_model")
tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir="./llama3_model")

# Save the model and tokenizer to a specific directory
model.save_pretrained("./llama3_model")
tokenizer.save_pretrained("./llama3_model")
