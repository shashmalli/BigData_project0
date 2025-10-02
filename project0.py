from datetime import date
from Journal import Journal

def write_to_journal(journal):
  w_method = input("Import file (I) or Enter Manually (W)\n")
  if w_method.upper() == "W":
    journal_entry = input("Start your entry below:\n")
    journal.add_entry(journal_entry, date.today())
  elif w_method.upper() == "I":
    user_file = input("Enter the name of the file: ")
    journal.write_from_file(user_file)
  else:
    print("You must enter a letter for one of the options\n")
    return

def main():
  myJournal = Journal("journal.txt")

  while True:
    usr_in = input("What would you like to do?\n(R) Read journal entries\n(W) Add journal entry\n(Q) Quit\n")
    if usr_in.upper() == "R":
      myJournal.read_entries()
    elif usr_in.upper() == "W":
      write_to_journal(myJournal)
    elif usr_in.upper() == "Q":
      break
    else:
      print("You must enter a letter for one of the options")


if __name__ == "__main__":
  main()