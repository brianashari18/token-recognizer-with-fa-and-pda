from helper.recognize_k import Recognize_K
from helper.recognize_o import Recognize_O
import SP_recognizer

class TokenRecognizer:
    def __init__(self):
        self.subject_recognizer = SP_recognizer.SubjectRecognizer()
        self.predikat_recognizer = SP_recognizer.PredikatRecognizer()
        self.object_recognizer = Recognize_O()
        self.keterangan_recognizer = Recognize_K()

    def set_token(self, sentence):
        tokens = []
        words = sentence.split()
        i = 0
        while i < len(words):
            word = words[i]
            if self.subject_recognizer.is_subject(word):
                tokens.append("S")
                i += 1
            elif self.predikat_recognizer.is_predikat(word):
                tokens.append("P")
                i += 1
            elif self.object_recognizer.recognize(word):
                tokens.append("O")
                i += 1
            else:
                found_keterangan = False
                for j in range(2, len(words) - i + 1):
                    phrase = " ".join(words[i : i + j])
                    if self.keterangan_recognizer.recognize(phrase):
                        tokens.append("K")
                        i += j
                        found_keterangan = True
                        break
                if not found_keterangan:
                    tokens.append("UNKNOWN")
                    i += 1
        return tokens