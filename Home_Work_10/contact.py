class Contact:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Имя: {self.name}, Почта: {self.email}, Телефон: {self.phone}"