import re
import streamlit as st


def highlight_words(text, words_to_highlight, highlight_color = 'yellow'):
    """Highlight specified words in the text with the specified color."""
    match_counts = {}
    for word in words_to_highlight:
        pattern = r'\b' + re.escape(word.strip()) + r'\b'  # New line
        pattern = re.compile(pattern, re.IGNORECASE)  # Modify the pattern to be case-insensitive
        # Find all matches to count them
        matches = pattern.findall(text)
        match_counts[word] = len(matches)
        text = re.sub(pattern, f"<span style='background-color:{highlight_color}'>{word}</span>", text)
    return text, {word: count for word, count in match_counts.items() if count > 0}


def main():
    text = "Java is a programming language. Kafka is a distributed streaming platform. GCP is a cloud platform."

    words_to_highlight = ["Java", "Kafka", "GCP", "ing", " streaming"]
    highlight_color = "yellow"

    st.title("Text Highlighter")

    st.markdown("Original Text:")
    st.write(text)

    highlighted_text = highlight_words(text, words_to_highlight, highlight_color)

    st.markdown("Highlighted Text:")
    st.markdown(highlighted_text, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
