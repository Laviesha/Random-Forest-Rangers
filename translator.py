# from deep_translator import GoogleTranslator

# # Supported languages
# LANGUAGES = {
#     "english": "en",
#     "hindi": "hi",
#     "french": "fr",
#     "german": "de",
#     "spanish": "es"
# }

# def translate_text(text, target_language):
#     """
#     Translates given text to the target language.
#     :param text: The text to translate
#     :param target_language: Target language (e.g., 'hindi', 'french')
#     :return: Translated text
#     """
#     if target_language.lower() not in LANGUAGES:
#         print(f"⚠️ Language '{target_language}' not supported!")
#         return text  # Return original text if language not found

#     try:
#         translated_text = GoogleTranslator(source="auto", target=LANGUAGES[target_language]).translate(text)
#         return translated_text
#     except Exception as e:
#         print(f"❌ Translation Error: {e}")
#         return text  # Return original text in case of error

# # Example usage
# if __name__ == "__main__":
#     sample_text = "Hello! This is a test translation."
#     print("Hindi Translation:", translate_text(sample_text, "hindi"))
#     print("French Translation:", translate_text(sample_text, "french"))
