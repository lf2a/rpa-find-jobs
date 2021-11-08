from botcity.core import DesktopBot

from search_jobs import FindJobs


class Bot(DesktopBot):
    def action(self, execution=None):
        FindJobs.run()


if __name__ == '__main__':
    Bot.main()
