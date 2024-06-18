class Recognizer_S:
    def __init__(self):
        # Definisi transisi state untuk mesin keadaan terbatas (finite state machine)
        self.transitions = {
            0: {'s': 1, 'k': 4, 'a': 7, 'd': 10},
            1: {'a': 2},
            2: {'y': 3},
            3: {'a': 100},  # "saya"
            4: {'a': 5, 'i': 12},
            5: {'m': 6},
            6: {'i': 100},  # "kami"
            7: {'n': 8},
            8: {'d': 9},
            9: {'a': 100},  # "anda"
            10: {'i': 11},
            11: {'a': 100},  # "dia"
            12: {'t': 13},
            13: {'a': 100},  # "kita"
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

    def is_subject(self, word):
        return self.recognize(word)