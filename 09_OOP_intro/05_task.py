class Shop:
    def __init__(self, clothes = [], shoes = [] ):
        self.clothes = clothes
        self.shoes = shoes
    def try_on(self):
        return f'You are wearing now {self.shoes} and {self.clothes}'
    def browse(self):
        return  f'You are browsing for {self.clothes} and {self.shoes}'
    def purchase(self):
        return f'You added to your basket'
def main():
    sneakers = Shop('Adidas', 'Nike', 'Puma')
    coats = Shop('Versace','LV', 'Gant' )


if __name__ == '__main__':
    main()