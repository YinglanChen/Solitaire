from cards import Card, Pack, Stock,Tableau, Foundations

class Game(object):
    def __init__(self, pack):
        self.pack = pack
        self.shuffle = pack.shuffle()
        # stock
        self.stock_count = 24
        stock_cards = self.shuffle[:self.stock_count]
        self.stock = Stock(stock_cards, self.stock_count)
        # tableau
        tableau_cards = self.shuffle[self.stock_count:]
        self.tableau = Tableau(tableau_cards)  
        self.foundations = Foundations()

    def draw(self):
        print("====== FOUNDATIONS ======")
        self.foundations.draw()
        
        print("====== TABLEAU ======")
        
        self.tableau.draw()
        print("====== STOCK ======")
        self.stock.draw_stock()

    def stock_next(self):
        self.stock.show_next()

    def stock_to_foundations(self):
        s = self.stock
        f = self.foundations
        if (s.count == 0):
            print("Illegal move. No cards in stock.")
            return
        elif (s.cursor == -1):
            print("Illegal move. No available card in stock. Please first draw a card from stock.")
        else:
            curr = s.stock[s.cursor]
            curr.suit_idx
            curr.num
            if (f.add(curr)): # success
                # remove curr card from stock
                s.remove()
            else: # fail
                return

    def stock_to_tabuleau(self, tc):
        s = self.stock
        t = self.tableau

        if (len(t.c[tc]) == 0):
            s_card = s.stock[s.cursor]
            if (s_card.num != 13):
                print("Illegal Move. Try to move non-K card to empty column")
            else:
                t.add(tc, s_card)
                s.remove()
        else:

            s_card = s.stock[s.cursor]
            t_card = t.c[tc][-1]

            if (self.isLegal(s_card, t_card)):
                t.add(tc, s_card)
                s.remove()
            else:
                print("Illegal Move. Two cards are not consecutive")
    
    def between_tabuleau(self, c1, r1, c2): 
        t = self.tableau
        card2 = t.c[c1][r1]

        if (len(t.c[c2]) == 0):
            if (card2.num != 13): 
                print("Illegal Move. Try to move non-K card to empty column")
                return
            else:  
                segment = t.c[c1][r1:]
                t.c[c1] = t.c[c1][:r1]
                t.c[c1][-1].hidden = False
                t.c[c2] += segment
                return

        card1 = t.c[c2][-1]
        
        if (self.isLegal(card2, card1)):
            segment = t.c[c1][r1:]
            t.c[c1] = t.c[c1][:r1]
            t.c[c1][-1].hidden = False
            t.c[c2] += segment
            return
        else:
            print("Illegal Move between tabuleau columns: ", card1, card2)
            return

    def tabuleu_to_foundations(self, col):
        t = self.tableau
        f = self.foundations
        if (len(t.c[col]) == 0):
            print("Illegal Move. Try to move cards from empty column. ")
            return
        # edge case: col empty
        card = t.c[col][-1]
        if (f.add(card)): # success
                # remove curr card from tableu
                t.c[col] = t.c[col][:-1]
                t.c[col][-1].hidden = False
        return



    def isLegal(self, card1, card2):
        if (card2.num - card1.num != 1): return False
        if ((card1.suit_idx + card2.suit_idx) % 2 != 1): return False
        return True


    def win(self): 
        s = self.stock
        t = self.tableau
        if (s.count > 0): return False
        if (t.isEmpty() or t.noHidden()): return True
        return False