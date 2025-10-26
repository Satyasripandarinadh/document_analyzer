from src.ocr import extract_text_from_pdf
from src.nlp_processing import summarize_text_llm, extract_resume_data

file_path = "data/sample.pdf"

# Step 1: OCR text extraction
ocr_text = extract_text_from_pdf(file_path)

# Step 2: Summarization
summary_result = summarize_text_llm(ocr_text)

# Step 3: Resume extraction (optional)
if "resume" in ocr_text.lower() or "curriculum vitae" in ocr_text.lower():
    resume_result = extract_resume_data(ocr_text)
else:
    resume_result = {"resume_analysis": "Not a resume document."}

# Step 4: Save output
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("--- OCR Text ---\n")
    f.write(ocr_text + "\n\n")
    f.write("--- Summary ---\n")
    f.write(summary_result["summary"] + "\n\n")
    f.write("--- Resume Analysis ---\n")
    f.write(resume_result["resume_analysis"])

print("✅ Document processed successfully! Check output.txt")
