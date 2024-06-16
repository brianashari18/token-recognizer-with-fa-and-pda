import token_recognizer
import validation
import stack


def main():
    sentences = [
        "saya bermain game di kamar",
        "kami membaca buku",
        "anda belajar algoritma",
        "kita menonton film",
        "dia membeli makanan",
        "saya bermain",
        "saya membaca",
        "anda",
        "aku membaca buku",
        "menonton",
    ]

    s = stack.Stack()
    tr = token_recognizer.TokenRecognizer()
    v = validation.Validation(s)

    # sentence = input("Masukkan kalimat: ")
    # token = tr.set_token(sentence=sentence)
    # is_valid = v.validate(tokens=token)

    # if is_valid:
    #     print("Kalimat anda valid")
    # else:
    #     print("Kalimat anda tidak valid")

    for sentence in sentences:
        token = tr.set_token(sentence=sentence)
        is_valid = v.validate(tokens=token)

        print(token)
        if is_valid:
            print(f"Kalimat '{sentence}': valid")
        else:
            print(f"Kalimat '{sentence}': tidak valid")


if __name__ == "__main__":
    main()
