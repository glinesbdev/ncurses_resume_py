import curses
from pathlib import Path
from string import ascii_letters
from json import load
from textwrap import wrap
from functools import reduce
from resume_entry import ResumeEntry
from resume_window import ResumeWindow

class App:
    def start(self):
        curses.wrapper(self.__main__)

    def __init__(self):
        self.commands = {}
        self.prelude = {}
        self.resume_entries = []
        self.windows = []
        self.window_index = 0
        self.__parse_json()

    def __parse_json(self):
        with open('{}/data/app_data.json'.format(Path(__file__).parent.resolve())) as f:
            data = load(f)['data']
            self.commands = data['commands']
            self.prelude = data['prelude']

            date_sort  = lambda d: int(d['dateStart'].strip(ascii_letters))

            for d in sorted(data['entries'], key = date_sort, reverse = True):
                self.resume_entries.append(ResumeEntry(d))

    def __main__(self, stdscr):
        for i, entry in enumerate(self.resume_entries):
            self.windows.append(ResumeWindow(curses.LINES - 8, curses.COLS - 4, 5, 2, entry, i))

        stdscr.clear()
        curses.curs_set(0)
        self.__print_heading(stdscr)
        self.__print_commands(stdscr)
        self.windows[0].show()

        while True:
            c = stdscr.getch()

            if c == curses.KEY_F1:
                break
            elif c == curses.KEY_UP:
                self.window_index -= 1
                self.windows[self.window_index % len(self.windows)].show()
            elif c == curses.KEY_DOWN:
                self.window_index += 1
                self.windows[self.window_index % len(self.windows)].show()

    def __print_heading(self, window):
        _, maxx = window.getmaxyx()
        tagline = wrap(self.prelude['tagline'], int(curses.COLS / 2))

        window.addstr(1, 3, self.prelude['name'])
        window.addstr(2, 3, self.prelude['email'])
        window.addstr(3, 3, self.prelude['phone'])

        for i, part in enumerate(tagline):
            window.addstr(i + 1, len(tagline[0]), part)

        window.refresh()

    def __print_commands(self, window):
        maxy, _ = window.getmaxyx()
        _, x = window.getbegyx()
        total_length = reduce(lambda a, b: len(str(a)) + len(str(b)), list(self.commands.values()))
        curx = total_length

        for command in self.commands.values():
            window.addstr(maxy - 2, curx , command)
            curx += len(command) + 2

        window.refresh()

