import random as rnd
from datetime import datetime


class Record:
    def __init__(self, record):
        name, score, date = record.split(', ')
        self.name = name
        self.score = int(score)
        self.date = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")


class Leaderboard:
    def __init__(self):
        self.top_10 = []
        self.all_records = []

    def get_top_10(self):
        for record in self.all_records:
            if len(self.top_10) == 0:
                self.top_10.append(record)
            else:
                for position in range(len(self.top_10)):
                    if record not in self.top_10:
                        if record.score < self.top_10[position].score:
                            self.top_10.insert(position, record)
                        elif record.score == self.top_10[position].score:
                            if record.date > self.top_10[position].date:
                                self.top_10.insert(position, record)
                            else:
                                self.top_10.insert((position + 1), record)
                        elif (len(self.top_10)+1) <= 10 and position == (len(self.top_10)-1):
                            self.top_10.append(record)
        if len(self.top_10) > 10:
            del self.top_10[10:]
        return


def show_leaderboard(all_stats):
    leaderboard = Leaderboard()
    for entry in all_stats:
        record = Record(entry)
        leaderboard.all_records.append(record)
    print("----------- Top 10 -----------")
    print("Rank |  Name - Score - Date  |")
    print("------------------------------")
    leaderboard.get_top_10()
    for position in range(len(leaderboard.top_10)):
        top_10_record = leaderboard.top_10[position]
        print(f"  {position + 1} |  {top_10_record.name} - {top_10_record.score} - {top_10_record.date}  |")
    return


names = ["Jack", "Jill", "Aiden", "Fred", "Bob", "Bill", "Susan", "Jimothy", "Bingus", "David"]
scores = [3, 1, 7, 4, 10, 3, 6, 2, 8, 8, 9]
dates = ["2025-03-01 13:15:55", "2023-02-11 15:11:35", "2011-07-09 10:12:34", "2015-06-04 10:28:14",
         "2017-07-09 10:12:34"]
raw_stats = []

for i in range(10):
    dates.append(
        f"{rnd.randrange(1990, 2025)}-{rnd.randrange(1, 13)}-{rnd.randrange(1, 29)} \
        {rnd.randrange(24)}:0{rnd.randrange(10)}:0{rnd.randrange(10)}")

for index in range(16):
    stat = f"{rnd.choice(names)}, {rnd.choice(scores)}, {rnd.choice(dates)}"
    raw_stats.append(stat)

show_leaderboard(raw_stats)
