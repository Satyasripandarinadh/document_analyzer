from src.ocr import extract_text_from_pdf
from src.nlp_processing import summarize_text_llm

file_path = "data/sample.pdf"

ocr_text = extract_text_from_pdf(file_path)
summary_result = summarize_text_llm(ocr_text)

with open("output.txt", "w", encoding="utf-8") as f:
    f.write("--- OCR Text ---\n")
    f.write(ocr_text + "\n\n")
    f.write("--- Summary ---\n")
    f.write(summary_result["summary"])

