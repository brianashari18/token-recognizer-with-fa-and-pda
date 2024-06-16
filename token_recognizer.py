class TokenRecognizer:
    def __init__(self):
        self.subject = ["saya", "kami", "anda", "kita", "dia"]
        self.predicate = ["bermain", "membaca", "belajar", "menonton", "membeli"]
        self.object = ["game", "buku", "algoritma", "film", "makanan"]
        self.keterangan = [
            "di rumah",
            "di ruang duduk",
            "pada malam hari",
            "di kamar",
            "di kantin",
        ]

    def recognize_S(self, word):
        transition = {0: {"subject": 1}}

        initial_state = 0
        current_state = initial_state
        if word in self.subject:
            current_state = transition[current_state]["subject"]

        return current_state == 1

    def recognize_P(self, word):
        transition = {0: {"predicate": 1}}

        initial_state = 0
        current_state = initial_state
        if word in self.predicate:
            current_state = transition[current_state]["predicate"]

        return current_state == 1

    def recognize_O(self, word):
        transition = {0: {"object": 1}}

        initial_state = 0
        current_state = initial_state
        if word in self.object:
            current_state = transition[current_state]["object"]

        return current_state == 1

    def recognize_K(self, word):
        transition = {0: {"keterangan": 1}}

        initial_state = 0
        current_state = initial_state
        if word in self.keterangan:
            current_state = transition[current_state]["keterangan"]

        return current_state == 1

    def set_token(self, sentence):
        tokens = []
        words = sentence.split()
        i = 0
        while i < len(words):
            word = words[i]
            if self.recognize_S(word):
                tokens.append("S")
                i += 1
            elif self.recognize_P(word):
                tokens.append("P")
                i += 1
            elif self.recognize_O(word):
                tokens.append("O")
                i += 1
            else:
                found_keterangan = False
                for j in range(2, len(words) - i + 1):
                    phrase = " ".join(words[i : i + j])
                    if self.recognize_K(phrase):
                        tokens.append("K")
                        i += j
                        found_keterangan = True
                        break
                if not found_keterangan:
                    tokens.append("")
                    i += 1
        return tokens
