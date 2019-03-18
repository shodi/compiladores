class Parser:
    def __init__(self, f):
        self.file_instance = f
        self.lookahead = self.file_instance.read(1)
    
    def match(self, t):
        try:
            if self.lookahead == t:
                self.lookahead = self.file_instance.read(1)
            else:
                raise Exception
        except Exception as e:
            raise e

    def term(self):
        try:
            num = int(self.lookahead)
            print(num, end='', flush=True)
            self.match(self.lookahead)
        except Exception:
            raise Exception

    def expr(self):
        try:
            self.term()
            while True:
                if self.lookahead == '+':
                    self.match('+')
                    self.term()
                    print('+', end='', flush=True)
                elif self.lookahead == '-':
                    self.match('-')
                    self.term()
                    print('-', end='', flush=True)
                else:
                    return
        except Exception as e:
            raise e

if __name__ == '__main__':
    with open('./test.txt', 'r') as f:
        parser = Parser(f)
        parser.expr()
        print('\n')