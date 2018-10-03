import numpy as np

class Card(object):

    def __init__(self, id, num, suit_idx):
        self.suits = ["diamond", "club", "heart", "spade"]
        self.suits_symbols = ["♦", "♣", "♥", "♠"]
        self.id = id # 1 to 52
        self.num = num # "J" or "1"
        self.suit_idx = suit_idx
        self.suit = self.suits[self.suit_idx]
        self.suit_sym = self.suits_symbols[self.suit_idx]
        self.hidden = True

    def __repr__(self):
        if (self.num == 1): return self.suit + " A"
        if (self.num == 11): return self.suit + " J"
        if (self.num == 12): return self.suit + " Q"
        if (self.num == 13): return self.suit + " K"
        return self.suit + " " + str(self.num)
    
    def convert_num(self):
        if (self.num == 1): return "A"
        if (self.num == 11): return "J"
        if (self.num == 12): return "Q"
        if (self.num == 13): return "K"
        return str(self.num)

    def draw_card(self):
        # inner width: 4 spaces
        ceiling = "------\n"
        if (self.hidden): 
            row1 = "|" + "?" + "   |\n" 
        elif (self.num == 10):
            row1 = "|" + self.suit_sym + self.convert_num() + " |\n" 
        else: 
            row1 = "|" + self.suit_sym + self.convert_num() + "  |\n" 
        row2 = "|    |\n"
        row3 = "|    |\n"
        floor = "------\n"
        s = ceiling + row1 + row2 + row3 + floor
        print(s)

    def draw_row1(self):

        if (self.hidden): 
            row1 = "|" + "?" + "   |" 
        elif (self.num == 10):
            row1 = "|" + self.suit_sym + self.convert_num() + " |" 
        else: 
            row1 = "|" + self.suit_sym + self.convert_num() + "  |" 
        
        return row1
    
    def draw_row2(self):

        return "|    |"

    def draw_ceiling(self):
        return "------"



class Pack(object):
    def __init__(self):
        self.pack = [] # a pack of 52 cards
        for i in range(52):
            id = i # start with 0
            num = i // 4 + 1 # 1 to 13
            suit_idx = i%4
            c = Card(id, num, suit_idx)
            self.pack.append(c)


    def shuffle(self):
        shuffle = []
        a = []
        for i in range(52):
            a.append(i)
        a = np.random.permutation(a)
        for i in range(len(a)):
            c = self.pack[a[i]]
            shuffle.append(c)
        return shuffle
   
class Stock(object):
    def __init__(self, stock, count):
        self.count = count
        self.stock = stock
        for i in range(len(stock)):
            stock[i].hidden = True
        self.cursor = -1 

    def show_next(self):
        if (self.count == 0): return

        if (self.cursor == -1): # curr no card
            self.cursor += 1
            curr = self.stock[self.cursor]
            curr.hidden = False
        elif (self.cursor == self.count - 1): # curr last card
            curr = self.stock[self.cursor]
            curr.hidden = True
            self.cursor = -1
        else:
            curr = self.stock[self.cursor]
            curr.hidden = True
            self.cursor += 1
            next = self.stock[self.cursor]
            next.hidden = False

    def remove(self):
        if (self.count == 0):
            print("Error: remove from empty stock")
            return
        if (self.cursor == self.count - 1):
            
            self.stock.pop(self.cursor)
            self.count -= 1
            self.cursor = -1

        else:
            self.count -= 1
            self.stock.pop(self.cursor)
            assert(self.count == len(self.stock))
            self.show_next()


    def draw_stock(self):
        if (self.cursor != -1):
            curr = self.stock[self.cursor]
            curr.draw_card()
        else: 
            # draw an unknow card

            self.stock[0].draw_card()

class Tableau(object):
    def __init__(self, cards):
        # 7 cols, each col is a list of cards
        # left -> right in list == up -> bottom in terminal
        self.cards = cards
        self.column_count = 7
        self.c = [] # c for columns
        counter = 0
        for i in range(self.column_count):
            self.c.append(cards[counter:counter+i+1])
            counter += i + 1

        # initally, only the last card is shown
        for i in range(self.column_count):
            col = self.c[i]
            last_card = col[-1]
            last_card.hidden = False


    def draw(self): 
        empty_card = "      "
        space = "     "
        col_str = [" col0 "," col1 "," col2 "," col3 "," col4 "," col5 "," col6 "]
        s = "     "

        for i in range(7):
            s += col_str[i]+space
        print(s)

        for row in range(13): # 0, 1, ..., 6

            ceiling = "     "
            row1 = "row" + str(row) + " "

            for col in range(self.column_count): # i, i+1, ..., 6 
                if row >= len(self.c[col]):
                    ceiling += empty_card + space
                    row1 += empty_card + space
                else :
                    card = self.c[col][row]
                    ceiling += card.draw_ceiling() + space
                    row1 += card.draw_row1() + space

            print(ceiling)
            print(row1)
        return 

    def add(self, col, card):
        self.c[col].append(card)
        return

    def isEmpty(self):
        for i in range(self.column_count):
            if (len(self.c[i]) != 0): return False
        return True

    def noHidden(self):
        for i in range(self.column_count):
            for j in range(len(self.c[i])):
                card = self.c[i][j]
                if (card.hidden): return False
        return True
      
            

# class SingleFoundation(object): return
# cards, suit

class Foundations(object): 
    def __init__(self):
        self.cards = [[-1] for i in range(4)]
        self.suits = ["diamond", "club", "heart", "spade"]
        self.suits_symbols = ["♦", "♣", "♥", "♠"]

    def draw(self):
        top = "------"
        space = "     "
        ceiling = ""
        row1 = ""
        width = "|    |"
        row2 = ""
        for i in range(4):
            ceiling += top + space
            if (self.cards[i][0] == -1):
                row1 += "|****|" + space
                row2 += "|****|" + space
            else:
                row1 += self.cards[i][-1].draw_row1() + space
                row2 += "|    |" + space

        print(ceiling)
        print(row1)
        print(row2)
        print(row2)
        print(ceiling)

    def add(self, card):
        idx = card.suit_idx
        pile = self.cards[idx]
        if (pile[0] == -1):
            if (card.num == 1):
                self.cards[idx] = [card]
                return True
            else:
                print("Illegal Move. Try to move non-A card to empty foundations")
                return False
        else:
            top = pile[-1] 
            if (card.num - top.num == 1):
                self.cards[idx].append(card)
                return True
            else:
                print("Illegal Move. Try to move non consecutive card to foundations")
                return False


