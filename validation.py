class Validation:
    def __init__(self, stack):
        self.stack = stack
        self.current_state = "q0"

    def transition(self, token):
        if self.current_state == "q1":
            if token == "S":
                self.stack.push("S")
                self.current_state = "q2"

        elif self.current_state == "q2":
            if token == "P":
                self.stack.pop()
                self.current_state = "q3"

        elif self.current_state == "q3":
            if token == "O":
                self.current_state = "q4"

            if token == "K":
                self.current_state = "q5"

        elif self.current_state == "q4":
            if token == "K":
                self.current_state = "q5"

    def parse(self, tokens):
        self.stack.push("#")
        self.current_state = "q1"
        for token in tokens:
            self.transition(token)
        self.stack.pop()

        if self.current_state in ["q3", "q4", "q5"]:
            self.current_state = "q6"

    def validate(self, tokens):
        self.parse(tokens)
        return len(self.stack.stack) == 0 and self.current_state == "q6"
