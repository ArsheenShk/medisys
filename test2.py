import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfFileReader(file)
        num_pages = reader.numPages
        for page_num in range(num_pages):
            page = reader.getPage(page_num)
            text += page.extractText()
    return text

def answer_question(text, question):
    # Simple keyword matching
    # You can replace this with more sophisticated NLP techniques
    # such as semantic similarity or machine learning models
    match = re.search(r"\b{}\b".format(re.escape(question)), text, re.IGNORECASE)
    if match:
        return text[match.start():match.end()]
    else:
        return "Sorry, I couldn't find an answer to that question."

def main():
    pdf_path = input("Enter the path to the PDF file: ")
    text = extract_text_from_pdf(pdf_path)
    while True:
        question = input("Ask a question (type 'exit' to quit): ")
        if question.lower() == "exit":
            break
        answer = answer_question(text, question)
        print("Answer:", answer)

if __name__ == "__main__":
    main()
