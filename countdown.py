import urwid
import time
import sys


class CountDown:

    def __init__(self, seconds):
        self.seconds = seconds
        self.palette = [('start', 'yellow', ''),
                        ('finish', 'dark red', '')
                        ]
        self.alarm = None

    def main(self):
        self.setup_view()
        self.main_loop = urwid.MainLoop(self.view,
                                        palette=self.palette,
                                        unhandled_input=self.keypress)
        self.alarm = self.main_loop.set_alarm_in(1, self.start)
        self.main_loop.run()

    def keypress(self, key):
        if key in ('q', 'Q'):
            raise urwid.ExitMainLoop()

    def setup_view(self):
        color = 'start' if self.seconds > 5 else 'finish'
        self.count_text = urwid.BigText(
            time.strftime('%H:%M:%S', time.gmtime(self.seconds)),
            urwid.font.HalfBlock6x5Font())
        self.view = urwid.Padding(self.count_text, 'center', width='clip')
        self.view = urwid.AttrMap(self.view, color)
        self.view = urwid.Filler(self.view, 'middle')

    def start(self, loop=None, data=None):
        self.seconds = self.seconds - 1
        if self.seconds < 0:
            return
        self.setup_view()
        loop.widget = self.view
        self.alarm = loop.set_alarm_in(1, self.start)

if __name__ == '__main__':
    try:
        init = sys.argv[1]
        sourcetime = map(lambda x: int(x), init.split(':'))
        total_seconds = sourcetime[0] * 3600 + \
            sourcetime[1] * 60 + sourcetime[2]
        c = CountDown(total_seconds)
        c.main()
    except Exception, KeyboardInterrupt:
        pass
