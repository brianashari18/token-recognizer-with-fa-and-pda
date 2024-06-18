from helper.recognize_k import Recognize_K
from helper.recognize_o import Recognize_O
from helper.recognize_s import Recognizer_S
from helper.recognize_p import Recognizer_P


class TokenRecognizer:
    def set_token(self, sentence):
        tokens = []
        words = sentence.split()
        i = 0
        while i < len(words):
            word = words[i].lower()
            if Recognizer_S().is_subject(word):
                tokens.append("S")
                i += 1
            elif Recognizer_P().is_predikat(word):
                tokens.append("P")
                i += 1
            elif Recognize_O().recognize(word):
                tokens.append("O")
                i += 1
            else:
                found_keterangan = False
                for j in range(2, len(words) - i + 1):
                    phrase = " ".join(words[i : i + j])
                    if Recognize_K().recognize(phrase.lower()):
                        tokens.append("K")
                        i += j
                        found_keterangan = True
                        break
                if not found_keterangan:
                    tokens.append("UNKNOWN")
                    i += 1
        return tokens
