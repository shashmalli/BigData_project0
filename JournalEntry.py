
class JournalEntry:
  def __init__(self, entry, date):
    self.entry = entry
    self.date = date

  def __str__(self):
    return f">{self.date}\n{self.entry}"