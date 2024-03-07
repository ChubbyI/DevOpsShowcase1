import os
import PyPDF2
import shutil
from deep_translator import GoogleTranslator
from deep_translator.exceptions import LanguageNotSupportedException



def copy_read_and_translate_pdf(source_path, dest_dir):
    
     # Get input file from user
    source_path = input("Enter the path to the input PDF file: ")
    if not os.path.isfile(source_path):
        print("Error: Input file not found.")
        return
    
    # Get destination directory from user
    dest_dir = input("Enter the destination directory: ")
    if not os.path.isdir(dest_dir):
        print("Error: Destination directory not found.")
        return
    
    # Get output language from user
    output_lang = input("Enter the output language (e.g., 'es' for Spanish): ")
    
    try:
        # Check if the output language is supported by Google Translate
        GoogleTranslator.validate_language(output_lang)
    except LanguageNotSupportedException:
        print(f"Error: Language '{output_lang}' is not currently supported by Google Translate.")
        return
    # copy the pdf file
    
    source_name = os.path.basename(source_path)
    dest_name = sourcename.replace('.pdf', '_spanish.pdf')
    dest_path = os.path.join(dest_dir, dest_name)
    shutil.copyfile(source_path, dest_path)

    
    # Open the copied pdf file
    
    with open(dest_path, 'rb') as file:
        pdf_reader = pyPDF2.PdfFileReader(file)

        #Read each page and extract the text
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()

        
            sentences = text.split('\n')

            translated_text = []

            # Translate each sentence or standalone word
            for sentence in sentences:
                words = sentences.split()
                translated_words = []

                for word in words:
                    # translate standalone words
                    if len(word.split()) == 1:
                        translated_word = GoogleTranslator(source='auto', target='es').translate(word)
                        translated_words.append(translated_word)
                    # translate whole sentence
                    else:
                        translated_sentence = GoogleTranslator(source='auto', target='es').translate(sentence)
                        translated_word.append(translated_sentence)

                        break
                
                translated_text.append(''.join(translated_words))
            
            # Process and print translated text
            print("Translated Text (Page {}):".format(page_num + 1))
            print(translated_text)
            print("\n" * 3)  # Print three line breaks after each page
            
# Example usage:
copy_read_and_translate_pdf()            