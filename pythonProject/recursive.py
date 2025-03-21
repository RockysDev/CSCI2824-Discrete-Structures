class Recursive:
    counter = 0
    
    def get_item_at_n(self, n):
        self.counter += 1

        ### Do not change anything above
        ### Start code below
        ### This function should return nth item in the sequence
        if n == 0:
            return 1
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n % 2 == 0:
            return 2 * self.get_item_at_n(n - 1) + self.get_item_at_n(n - 2)
        else:
            return self.get_item_at_n(n - 1) + 2 * self.get_item_at_n(n - 2)
