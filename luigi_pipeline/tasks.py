import datetime

import luigi


class PrintDateTask(luigi.Task):
    date = luigi.DateParameter(default=datetime.date.today())

    def output(self):
        return luigi.LocalTarget(f"output/date_{self.date}.txt")

    def run(self):
        with self.output().open("w") as f:
            f.write(f"Today's date is {self.date}\n")
