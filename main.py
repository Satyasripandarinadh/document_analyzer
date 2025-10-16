from src.ocr import extract_text_from_pdf
from src.nlp_processing import summarize_via_llm

file_path = "data/sample_resume.pdf"

# 1️⃣ Extract text using OCR
ocr_text = extract_text_from_pdf(file_path)
print("\n--- OCR Text ---\n", ocr_text)



# 2️⃣ Summarize using LLM
summary = summarize_via_llm(ocr_text)
print("\n--- Summary ---\n", summary)
