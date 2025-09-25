from JournalEntry import JournalEntry

class Journal:
  def __init__(self, filename="journal.txt"):
    self.filename = filename

  def add_entry(self, text, date):
    entry = JournalEntry(text, date)
    with open(self.filename, "a") as f:
      f.write(f"\n>{entry.date}\n{entry.entry}\n")

  def read_entries(self):
    with open(self.filename, "r") as f:
      print("\tJournal\n")
      print(f.read())
