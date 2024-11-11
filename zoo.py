class Zoo:
    def get_ticket_price(self, age):
        if 0 <= age <= 12: #age < 0
            return 50
        elif 13 <= age <= 20: #age < 20
            return 100
        elif 21 <= age <= 60: #age < 21
            return 150
        elif age >= 60:
            return 100
        elif age < 0 : #to handle input Under 0
            return "Invalid Input"