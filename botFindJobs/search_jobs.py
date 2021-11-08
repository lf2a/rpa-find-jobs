from botcity.core import DesktopBot

from botFindJobs.image_not_found_exception import ImageNotFoundException


class FindJobs(DesktopBot):

    def action(self, execution=None):
        self.add_image("keywords", self.get_resource_abspath("keywords.png"))
        self.add_image("sort_jobs", self.get_resource_abspath("sort_jobs.png"))
        self.add_image("viewing", self.get_resource_abspath("viewing.png"))
        self.add_image("print", self.get_resource_abspath("print.png"))
        self.add_image("download", self.get_resource_abspath("download.png"))

    def access(self):
        self.browse("https://www.usajobs.gov/")
        self.wait(10000)

    def search(self, keywords: str, location: str):
        key_input = self.find(label="keywords")

        if key_input is None:
            raise ImageNotFoundException("Not found: keywords.png")

        self.click_relative(x=14, y=41)

        self.control_a(1000)
        self.kb_type(keywords, 100)

        self.tab(1000)

        self.control_a(1000)
        self.kb_type(location, 100)

        self.enter(10000)

        print(f"Search: ${keywords} in ${location}")
        print(f"searching ${keywords} job in ${location}")

        sort = self.find(label="sort_jobs")

        if sort is None:
            raise ImageNotFoundException("Not found: sort_jobs.png")

        self.click_relative(x=120, y=0)

        self.type_down(1000)
        self.type_down(1000)

        self.enter(10000)

    def collect_info(self):
        view = self.find(label="viewing")

        if view is None:
            raise ImageNotFoundException("Not found: viewing.png")

        self.triple_click()

        self.control_c(1000)

        content = str(self.get_clipboard()).split(" ")
        num_of_jobs = content[len(content) - 2]
        print("Jobs found: " + num_of_jobs)

        self.tab(1000)
        self.tab(1000)
        self.tab(1000)

        self.get_job_info(int(num_of_jobs))

    def get_job_info(self, jobs: int):
        for i in range(jobs):

            self.type_keys(['ctrl', 'enter'])
            self.wait(1000)

            self.type_keys(['ctrl', 'tab'])
            self.wait(1000)

            prnt = self.find(label="print")

            if prnt is None:
                raise ImageNotFoundException("Not found: print.png")

            self.click()
            self.wait(3000)

            down = self.find(label="download")

            if down is None:
                raise ImageNotFoundException("Not found: download.png")

            self.click_relative(x=64, y=-3)
            self.wait(3000)

            print("Page saved.")

            self.control_w(1000)
            self.control_w(1000)
            self.tab(1000)

            if i == 1:
                self.tab(1000)

        self.control_w(1000)

    @classmethod
    def run(cls):
        f = FindJobs()
        f.access()
        f.search("Software Developer", "Boston, Massachusetts")
        f.collect_info()
