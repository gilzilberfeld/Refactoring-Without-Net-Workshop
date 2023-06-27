
class RefactoringExamples(object):
    def __init__(self):
        self.field = False
        self.result = 0

    def if_example(self):
        if self.field:
            self.result = 4
        else:
            self.result = 6

    # Guard statements (early return) can reduce Arrow Code complexity
    def guard_example(self):
        if self.field:
            self.result = 4
            return
        self.result = 6

    # Condition inversion can help readabilty and simplification
    def inverted_if_example(self):
        if not self.field:
            self.result = 6
        else:
            self.result = 4

    # Switching the order of conditions can help find common code
    def switched_conditions_example_1(self):
        if self.field:
            if self.other_field:
                self.result = 4
        else:
            self.result = 6

    def switched_conditions_example_2(self):
        if self.other_field:
            if self.field:
                self.result = 4
        else:
            self.result = 6

    # Method extraction can help remove noise
    # inlining can help re-ordering the code
    def extracted_and_inlined_example(self):
        self.result = self.some_method()

    def some_method(self):
        return "reafctoring " + "without a net"
