class Recognize_O:
    def __init__(self):
        # Definisi transisi state untuk mesin keadaan terbatas (finite state machine)
        self.transitions = {
            0: {
                "g": 1,
                "b": 4,
                "p": 7,
                "f": 12,
                "m": 15,
            },
            1: {"a": 2},
            2: {"m": 3},
            3: {"e": 100},
            4: {"u": 5},
            5: {"k": 6},
            6: {"u": 100},
            7: {"i": 8},
            8: {"a": 9},
            9: {"n": 11},
            11: {"o": 100},
            12: {"i": 13},
            13: {"l": 14},
            14: {"m": 100},
            15: {"a": 16},
            16: {"k": 17},
            17: {"a": 18},
            18: {"n": 19},
            19: {"a": 20},
            20: {"n": 100},
        }
        self.final_state = 100

    def recognize(self, word):
        curr_state = 0  # Inisialisasi state awal
        for letter in word:
            if (
                curr_state in self.transitions
                and letter in self.transitions[curr_state]
            ):
                curr_state = self.transitions[curr_state][
                    letter
                ]  # Pindah ke state berikutnya
            else:
                curr_state = (
                    -1
                )  # Jika tidak ada transisi yang sesuai, set state ke -1 (state tidak valid)

        return (
            curr_state == self.final_state
        )  # Mengembalikan True jika state terakhir adalah state final (kata dikenali)
