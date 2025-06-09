class Question:
    def __init__(self, text, options, correct_option):
        self.text = text
        self.options = options  # dict: {'a': 'option text', 'b': 'option text', ...}
        self.correct_option = correct_option.lower()

    def ask(self):
        print(self.text)
        for key in sorted(self.options.keys()):
            print(f"  {key}) {self.options[key]}")

        while True:
            answer = input("Choose an option (a/b/c/d): ").strip().lower()
            if answer in self.options:
                return answer == self.correct_option
            else:
                print("Invalid option. Please enter a, b, c, or d.")