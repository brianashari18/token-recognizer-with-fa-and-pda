class SubjectRecognizer:
    def __init__(self):
        # Definisi transisi state untuk mesin keadaan terbatas (finite state machine)
        self.transitions = {
            'saya': {
                0: {'s': 1},
                1: {'a': 2},
                2: {'y': 3},
                3: {'a': 100},
            },
            'kami': {
                0: {'k': 1},
                1: {'a': 2},
                2: {'m': 3},
                3: {'i': 100},
            },
            'anda': {
                0: {'a': 1},
                1: {'n': 2},
                2: {'d': 3},
                3: {'a': 100},
            },
            'kita': {
                0: {'k': 1},
                1: {'i': 2},
                2: {'t': 3},
                3: {'a': 100},
            },
            'dia': {
                0: {'d': 1},
                1: {'i': 2},
                2: {'a': 100},
            }
        }
        self.final_state = 100

    def recognize(self, word, fsm_transitions):
        curr_state = 0  # Inisialisasi state awal
        for letter in word:
            if curr_state in fsm_transitions and letter in fsm_transitions[curr_state]:
                curr_state = fsm_transitions[curr_state][letter]  # Pindah ke state berikutnya
            else:
                curr_state = -1  # Jika tidak ada transisi yang sesuai, set state ke -1 (state tidak valid)
                break

        return curr_state == self.final_state  # Mengembalikan True jika state terakhir adalah state final (kata dikenali)

    def is_subject(self, word):
        for subject, fsm_transitions in self.transitions.items():
            if self.recognize(word, fsm_transitions):
                return True
        return False
    


class PredikatRecognizer:
    def __init__(self):
        # Definisi transisi state untuk mesin keadaan terbatas (finite state machine)
        self.transitions = {
            'bermain': {
                0: {'b': 1},
                1: {'e': 2},
                2: {'r': 3},
                3: {'m': 4},
                4: {'a': 5},
                5: {'i': 6},
                6: {'n': 100},
            },
            'membaca': {
                0: {'m': 1},
                1: {'e': 2},
                2: {'m': 3},
                3: {'b': 4},
                4: {'a': 5},
                5: {'c': 6},
                6: {'a': 100},
            },
            'belajar': {
                0: {'b': 1},
                1: {'e': 2},
                2: {'l': 3},
                3: {'a': 4},
                4: {'j': 5},
                5: {'a': 6},
                6: {'r': 100},
            },
            'menonton': {
                0: {'m': 1},
                1: {'e': 2},
                2: {'n': 3},
                3: {'o': 4},
                4: {'n': 5},
                5: {'t': 6},
                6: {'o': 7},
                7: {'n': 100},
            },
            'membeli': {
                0: {'m': 1},
                1: {'e': 2},
                2: {'m': 3},
                3: {'b': 4},
                4: {'e': 5},
                5: {'l': 6},
                6: {'i': 100},
            }
        }
        self.final_state = 100

    def recognize(self, word, fsm_transitions):
        curr_state = 0  # Inisialisasi state awal
        for letter in word:
            if curr_state in fsm_transitions and letter in fsm_transitions[curr_state]:
                curr_state = fsm_transitions[curr_state][letter]  # Pindah ke state berikutnya
            else:
                curr_state = -1  # Jika tidak ada transisi yang sesuai, set state ke -1 (state tidak valid)
                break

        return curr_state == self.final_state  # Mengembalikan True jika state terakhir adalah state final (kata dikenali)

    def is_predikat(self, word):
        for predikat, fsm_transitions in self.transitions.items():
            if self.recognize(word, fsm_transitions):
                return True
        return False
    
