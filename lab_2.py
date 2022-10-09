class Animals():
    def __init__(self, view, kind, detachment):
        self.view = view
        self.kind = kind
        self.detachment = detachment
    def determ(self):
        print("Вид этого животного:", self.view, self.kind, self.detachment)
bear = Animals("Бурый медведь,","Медведи,","Хищные")
bear.determ()