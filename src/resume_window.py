import curses
from textwrap import wrap

class ResumeWindow:
    def __init__(self, lines, cols, height, width, resume_entry, index):
        self.index = index
        self.resume_entry = resume_entry
        self.window = curses.newwin(lines, cols, height, width)
        self.y, self.x = self.window.getbegyx()
        self.maxy, self.maxx = self.window.getmaxyx()

    def show(self):
        self.__print_border()
        self.__print_heading()
        self.__print_subheading()
        self.__print_tenure()
        self.__print_title()
        self.__print_summary()
        self.__print_skills()
        self.window.refresh()

    def __print_border(self):
        self.window.box(0, 0)
        self.window.addch(self.y, 0, curses.ACS_LTEE)
        self.window.addch(self.y, self.maxx - 1, curses.ACS_RTEE)
        self.window.hline(self.y, self.x - 1, curses.ACS_HLINE, self.maxx - 2)

    def __print_heading(self):
        self.window.addstr(self.y - 4, self.x, self.resume_entry.heading())
        self.window.addstr(self.y - 4, self.maxx - 9, 'Page {}'.format(str(self.index + 1)))

    def __print_subheading(self):
        padding = len(self.resume_entry.heading()) + 1
        self.window.addstr(self.y - 4, self.x + padding, self.resume_entry.subheading())

    def __print_tenure(self):
        tenure = "{} - {}".format(self.resume_entry.date_start(), self.resume_entry.date_end())
        self.window.addstr(self.y - 3, self.x, tenure)

    def __print_title(self):
        self.window.addstr(self.y - 2, self.x, self.resume_entry.title())

    def __print_summary(self):
        self.window.addstr(self.y + 1, self.x, "Summary:")

        for i, part in enumerate(wrap(self.resume_entry.summary(), self.maxx - 3)):
            self.window.addstr(self.y + 3 + i, self.x, part)

    def __print_skills(self):
        offset = self.maxy - 16
        self.window.addstr(self.maxy - 18, self.x, "Related Skills:")

        for i, skill in enumerate(self.resume_entry.skills()):
            self.window.addstr(offset, self.x, skill)
            offset += 1

