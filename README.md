# Email Summarizer & Smart Reply Generator
An AI-powered tool that summarizes emails and generates context-aware smart replies using Natural Language Processing (NLP) techniques. Built with Python and powered by transformer models, this application helps users save time by understanding and responding to emails more efficiently.

# Features
Email Summarization – Generates concise summaries of long emails using transformer-based models.

Smart Reply Generator – Suggests intelligent, context-based replies based on email summaries.

Web Interface – Easy-to-use frontend with interactive input.

Fast & Lightweight – Optimized for performance on both CPU and GPU.

Transformer-Based Models – Built using Hugging Face Transformers, specifically DistilBART for summarization and T5 for reply generation.

# Tech Stack
Python

Transformers (BERT/T5/PEGASUS, DistilBART for summarization, T5 for text generation)

Hugging Face 🤗

Flask / Streamlit (for frontend)

HTML/CSS/JS (if applicable)

Git & GitHub for version control

# Getting Started
1. Clone the repository

git clone https://github.com/Jyoshita-Gopalakrishnan/Email-Summarizer-Smart-Reply-Generator.git
cd Email-Summarizer-Smart-Reply-Generator
2. Install the required dependencies
Make sure you have Python 3.7+ installed. Then, install the required packages using pip:


pip install -r requirements.txt
3. Run the Streamlit app
Start the Streamlit app by running the following command:


streamlit run app.py
This will launch the app in your default browser. You can then upload your email text files to summarize and generate replies.

# Usage
Upload Email: Upload a .txt file containing a raw email.

Summarize Email: Click the "Summarize" button to generate a summary of the email using DistilBART.

Generate Reply: After summarizing the email, click the "Generate Reply" button to generate a professional reply based on the email summary using T5.

