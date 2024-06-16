import token_recognizer
import validation
import stack
import streamlit as st


def main():
    # sentences = [
    #     "saya bermain game di kamar",
    #     "kami membaca buku",
    #     "anda belajar algoritma",
    #     "kita menonton film",
    #     "dia membeli makanan",
    #     "saya bermain",
    #     "saya membaca",
    #     "anda",
    #     "aku membaca buku",
    #     "menonton",
    # ]

    # s = stack.Stack()
    # tr = token_recognizer.TokenRecognizer()
    # v = validation.Validation(s)

    # # sentence = input("Masukkan kalimat: ")
    # # token = tr.set_token(sentence=sentence)
    # # is_valid = v.validate(tokens=token)

    # # if is_valid:
    # #     print("Kalimat anda valid")
    # # else:
    # #     print("Kalimat anda tidak valid")

    # for sentence in sentences:
    #     token = tr.set_token(sentence=sentence)
    #     is_valid = v.validate(tokens=token)

    #     print(token)
    #     if is_valid:
    #         print(f"Kalimat '{sentence}': valid")
    #     else:
    #         print(f"Kalimat '{sentence}': tidak valid")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Token Recognition", "About Us"])

    if page == "Home":
        st.title("Welcome to the Token Recognition App")
        st.write(
            "This app allows you to tokenize and validate sentences based on predefined rules."
        )

    elif page == "Token Recognition":
        st.title("Token Recognition and Sentence Validation")

        sentence = st.text_input("Enter sentence:")

        if sentence:
            s = stack.Stack()
            tr = token_recognizer.TokenRecognizer()
            v = validation.Validation(s)

            token = tr.set_token(sentence=sentence)
            st.write(f"Tokens: {token}")
            is_valid = v.validate(tokens=token)

            if is_valid:
                st.success(f"'{sentence}' is valid")
            else:
                st.error(f"'{sentence}' is not valid")

    elif page == "About Us":
        st.title("About Us")
        st.write(
            """
        This application was created to demonstrate the use of token recognition and sentence validation using a finite state machine.
        It allows users to input sentences and check their validity based on specific grammatical rules.
        
        Developed by:
        
            - Althaf Rizqullah
            - Brian Anashari
            - Evelyn Emery Dahayu
        """
        )


if __name__ == "__main__":
    main()
