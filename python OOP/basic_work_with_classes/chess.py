# king - король, queen - ферзь, rook - ладья, bishop - слон, knight - конь, pawn - пешка

class Figure:
    def __init__(self, color: bool, place: tuple) -> None:  # initialization
        self.color = color
        self.place = place  # place[0] - column, place[1] - row

    def change_color(self) -> None:
        if self.color:  # self.color == True
            self.color = False
        else:
            self.color = True

    def change_place(self, new_place: tuple) -> None:
        self.place = new_place


# ROOK
class rook(Figure):
    def __str__(self) -> str:
        return f'Type: Rook, place: {self.place}, color: {"white" if self.color else "black"}.'

    def checkrook(self, check_place: tuple) -> bool:
        if self.place[0] == check_place[0] or self.place[1] == check_place[1]:
            return True
        return False
