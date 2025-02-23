# from transformers import pipeline

# # Load the summarization pipeline with the BART model
# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# def summarize_text(text):
#     """Summarizes the input text using the BART model."""
#     text = text[:]  # Truncate if too long
#     # Generate the summary
#     summary = summarizer(text, max_length=200, min_length=75, do_sample=False)
#     return summary[0]['summary_text']


from transformers import BartForConditionalGeneration, BartTokenizer

# Load BART Model & Tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

def summarize_text(text , max_output=200):
    """Summarizes the input text using the BART model."""
    if not text or len(text.split())< 100:
        return text
    text = text[:]  # Truncate if too long
    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", truncation=False)
    summary_ids = model.generate(inputs, max_length=max_output, min_length=100, length_penalty=2.0, num_beams=4, early_stopping=True)
    return tokenizer.decode(summary_ids[0], skip_special_tokens=True)