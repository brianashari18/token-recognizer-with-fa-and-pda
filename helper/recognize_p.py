class Recognizer_P:
    def __init__(self):
        # Definisi transisi state untuk mesin keadaan terbatas (finite state machine)
        self.transitions = {
            0: {'b': 1, 'm': 7},
            1: {'e': 2},
            2: {'r': 3, 'l': 9},
            3: {'m': 4},
            4: {'a': 5},
            5: {'i': 6},
            6: {'n': 100},  # "bermain"
            7: {'e': 8},
            8: {'m': 16, 'n': 22},
            9: {'a': 10},
            10: {'j': 11},
            11: {'a': 12},
            12: {'r': 100},  # "belajar"
            16: {'b': 17},
            17: {'a': 18},
            18: {'c': 19},
            19: {'a': 100},  # "membaca"
            22: {'o': 23},
            23: {'n': 24},
            24: {'t': 25},
            25: {'o': 26},
            26: {'n': 100},  # "menonton"
            18: {'e': 19},
            19: {'l': 20},
            20: {'i': 100}   # "membeli"
        }
        self.final_state = 100

    def recognize(self, word):
        curr_state = 0  # Inisialisasi state awal
        for letter in word:
            if curr_state in self.transitions and letter in self.transitions[curr_state]:
                curr_state = self.transitions[curr_state][letter]  # Pindah ke state berikutnya
            else:
                curr_state = -1  # Jika tidak ada transisi yang sesuai, set state ke -1 (state tidak valid)
                break

        return curr_state == self.final_state  # Mengembalikan True jika state terakhir adalah state final (kata dikenali)

    def is_predikat(self, word):
        return self.recognize(word)