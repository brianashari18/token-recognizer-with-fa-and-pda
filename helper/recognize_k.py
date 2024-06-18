class Recognize_K:
    def __init__(self):
        # Definisi transisi state untuk mesin keadaan terbatas (finite state machine)
        self.transitions = {
            0: {"d": 1},
            1: {"i": 2},
            2: {" ": 3},
            3: {"r": 4, "k": 5},
            4: {
                "u": 6,
            },
            5: {
                "o": 9,
                "a": 10,
            },
            6: {
                "m": 7,
            },
            7: {"a": 8},
            8: {"h": 100},
            9: {"s": 100},
            10: {
                "n": 11,
                "m": 14,
            },
            11: {"t": 12},
            12: {"i": 13},
            13: {"n": 100},
            14: {"a": 15, "p": 16},
            15: {"r": 100},
            16: {"u": 17},
            17: {"s": 100},
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
