import urwid
import time
import sys


class Clock:

    def keypress(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    def setup_view(self):
        self.clock_txt = urwid.BigText(
            time.strftime('%H:%M:%S'), urwid.font.HalfBlock5x4Font())
        self.view = urwid.Padding(self.clock_txt, 'center', width='clip')
        self.view = urwid.AttrMap(self.view, 'body')
        self.view = urwid.Filler(self.view, 'middle')

    def main(self):
        self.setup_view()
        loop = urwid.MainLoop(
            self.view, palette=[('body', 'dark cyan', '')],
            unhandled_input=self.keypress)
        loop.set_alarm_in(1, self.refresh)
        loop.run()

    def refresh(self, loop=None, data=None):
        self.setup_view()
        loop.widget = self.view
        loop.set_alarm_in(1, self.refresh)


if __name__ == '__main__':
    clock = Clock()
    sys.exit(clock.main())
