class ResumeEntry:
    def __init__(self, json_data):
        self.json_data = json_data

    def heading(self):
        return self.json_data['heading']

    def subheading(self):
        return self.json_data['subheading']

    def title(self):
        return self.json_data['title']

    def date_start(self):
        return self.json_data['dateStart']

    def date_end(self):
        return self.json_data['dateEnd']

    def summary(self):
        return self.json_data['summary']

    def skills(self):
        return self.json_data['skills']

