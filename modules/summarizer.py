from transformers import pipeline

# Initialize the summarizer and reply generator
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
generator = pipeline("text2text-generation", model="google/flan-t5-base")

def summarize_email(text: str) -> str:
    try:
        input_length = len(text.split())
        max_length = min(input_length // 2, 100)  # Adjust based on input length
        result = summarizer(text, max_length=max_length, min_length=20, do_sample=False)
        return result[0]['summary_text']
    except Exception as e:
        return f"Error in summarization: {str(e)}"

def generate_reply(summary: str) -> str:
    prompt = (
        "You are an email assistant. Read the following summary of an email "
        "and write a professional and helpful reply.\n\n"
        f"Email Summary:\n{summary}\n\n"
        "Reply:"
    )
    
    try:
        result = generator(prompt, max_length=150, num_return_sequences=1)
        return result[0]["generated_text"].split("Reply:")[-1].strip()
    except Exception as e:
        return f"Error in reply generation: {str(e)}"
