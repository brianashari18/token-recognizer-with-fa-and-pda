import streamlit as st
from token_recognizer import (
    TokenRecognizer,
)  # Assuming token_recognizer is a custom module
from validation import Validation  # Assuming validation is a custom module
from stack import Stack  # Assuming stack is a custom module

subject = ["saya", "kami", "anda", "kita", "dia"]
predicate = ["bermain", "membaca", "belajar", "menonton", "membeli"]
object = ["game", "buku", "piano", "film", "makanan"]
keterangan = [
    "di rumah",
    "di kampus",
    "di kos",
    "di kamar",
    "di kantin",
]


def main():
    """
    Main function to run the Token Recognition application.
    """

    st.set_page_config(
        page_title="Token Recognition App",
        page_icon="",
    )

    with st.sidebar:
        st.title("Navigation")
        selected_page = st.radio("Go to", ("Home", "Token Recognition", "About Us"))

    if selected_page == "Home":
        st.title("Welcome to the Token Recognition App")
        st.image("./hero.png", use_column_width=True)
        st.write(
            """
            This app allows you to tokenize and validate sentences based on predefined rules.
            Navigate to the "Token Recognition" page to get started.
            """
        )

    elif selected_page == "Token Recognition":
        st.title("Token Recognition and Sentence Validation")
        entered_sentence = st.text_input("Enter a sentence to tokenize and validate:")

        if entered_sentence:
            token_stack = Stack()
            token_recognizer = TokenRecognizer()
            validator = Validation(token_stack)

            tokens = token_recognizer.set_token(sentence=entered_sentence)
            st.write(f"Tokens: {tokens}")

            is_valid = validator.validate(tokens=tokens)
            if is_valid:
                st.success(f"'{entered_sentence}' is valid.")
            else:
                st.error(f"'{entered_sentence}' is not valid.")

        else:
            st.info(
                "Please enter a sentence to begin the tokenization and validation process."
            )

        st.subheader("Dictionary")
        st.write(
            """
            Below is the dictionary of words used for token recognition.
            """
        )

        st.markdown("##### Subjects")
        st.write("\n".join([f"- {word}" for word in subject]))

        st.markdown("##### Predicates")
        st.write("\n".join([f"- {word}" for word in predicate]))

        st.markdown("##### Objects")
        st.write("\n".join([f"- {word}" for word in object]))

        st.markdown("##### Keterangan")
        st.write("\n".join([f"- {word}" for word in keterangan]))

    elif selected_page == "About Us":
        st.title("About Us")
        st.write(
            """
            This application was created to demonstrate the use of token recognition with Finite Automata and sentence validation with Push Down Automata.
            It allows users to input sentences and check their validity based on specific grammatical rules.

            ### Developed by:
            - Althaf Rizqullah
            - Brian Anashari
            - Evelyn Emery Dahayu
            """
        )


if __name__ == "__main__":
    main()
