from datetime import date
from Journal import Journal

def main():
  myJournal = Journal("journal.txt")

  while True:
    usr_in = input("What would you like to do?\n(R) Read journal entries\n(W) Add journal entry\n(Q) Quit\n")
    if usr_in.upper() == "R":
      myJournal.read_entries()
    elif usr_in.upper() == "W":
      journal_entry = input("Start your entry below:\n")
      myJournal.add_entry(journal_entry, date.today())
    elif usr_in.upper() == "Q":
      break

if __name__ == "__main__":
  main()