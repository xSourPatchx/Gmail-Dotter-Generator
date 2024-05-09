#############################
## Generate a unique Gmail ##
#############################

import random

# function to create a list of username possibilites
def generate_usernames(username):
  if len(username[11:]) > 0:
    list = []
    for x in ('.', ''):
      for y in generate_usernames(username[1:]):
        list.append(username[0] + x + y)
    return list
  return [username]

# function to check if gmail is valid
def check_gmail(gmail):
  return '@' in gmail and 'gmail.com' in gmail.split('@')[1] and len(gmail.split('@')[0]) >= 2

# function to format text block for better readability

def format_text_block(text):
  formatted_text = ""
  lines = 1
  for word in text.split(" "):
    formatted_text += word + " "
    if (len(formatted_text) > lines * 65):
      formatted_text += '\n'
      lines += 1
  return formatted_text

# function to display help
def print_help():
  print(format_text_block("This program generates a unique Gmail for your logins. Assuming a password manager is being used to track your credentials, this Gmail trick helps you stay anonymous by rotating your login credentials. With Gmails in particular, the use of arbitrary dots in your Gmail (before the \"@\" symbol) will reach the same address no matter where you put the periods. Furthermore, adding a \"+\" symbol and any word or combination of characters after your username and before the \"@\" symbol, will reach the same address."))

def main():
  print('-' * 65)
  # prompted_gmail can be hard coded as your Gmail (ie. "example@gmail.com")
  prompted_gmail = str(input("Please enter Gmail, or type 'help', and press enter: "))
  print('-' * 65)
  gmail_possibilities = list()
  
  if (prompted_gmail == 'help'):
    print_help()
    return main()
  else:
    if (not check_gmail(prompted_gmail)):
      print("The gmail you provided is incorrectly formatted or not a Gmail, please check Gmail.")
      return main()
    else:
      
      # making a list using usernames to generate all possibilities of Gmail
      for gmail in generate_usernames(prompted_gmail):
        gmail_possibilities.append(gmail)

      # randomly select Gmail from list
      selected_gmail = random.choice(gmail_possibilities)

      # slicing Gmail before and after the '@' symbol
      slicer = selected_gmail.find('@')
      selected_gmail_username = selected_gmail[:slicer]
      selected_gmail_domain = selected_gmail[slicer:]

      website = input("Enter website name (hit enter to not include website in Gmail): ")
      print('-' * 65)
      # condition if website is blank
      if website == '':
        pass
      else:
        selected_gmail = selected_gmail_username + '+' + website + selected_gmail_domain
      print(selected_gmail)
      print('-' * 65)

if __name__ == "__main__":
  main()
