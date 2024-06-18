class Recognizer_S:
    def __init__(self):
        # Definisi transisi state untuk mesin keadaan terbatas (finite state machine)
        self.transitions = {
            "saya": {
                0: {"s": 1},
                1: {"a": 2},
                2: {"y": 3},
                3: {"a": 100},
            },
            "kami": {
                0: {"k": 1},
                1: {"a": 2},
                2: {"m": 3},
                3: {"i": 100},
            },
            "anda": {
                0: {"a": 1},
                1: {"n": 2},
                2: {"d": 3},
                3: {"a": 100},
            },
            "kita": {
                0: {"k": 1},
                1: {"i": 2},
                2: {"t": 3},
                3: {"a": 100},
            },
            "dia": {
                0: {"d": 1},
                1: {"i": 2},
                2: {"a": 100},
            },
        }
        self.final_state = 100

    def recognize(self, word, fsm_transitions):
        curr_state = 0  # Inisialisasi state awal
        for letter in word:
            if curr_state in fsm_transitions and letter in fsm_transitions[curr_state]:
                curr_state = fsm_transitions[curr_state][
                    letter
                ]  # Pindah ke state berikutnya
            else:
                curr_state = (
                    -1
                )  # Jika tidak ada transisi yang sesuai, set state ke -1 (state tidak valid)
                break

        return (
            curr_state == self.final_state
        )  # Mengembalikan True jika state terakhir adalah state final (kata dikenali)

    def is_subject(self, word):
        for subject, fsm_transitions in self.transitions.items():
            if self.recognize(word, fsm_transitions):
                return True
        return False
