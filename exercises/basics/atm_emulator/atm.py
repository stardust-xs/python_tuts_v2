# Flow author's name: S. Maladkar
# Flow author's github: https://github.com/srushti-maladkar
#
# Flow of the code:
# -----------------
#
# Welcome message
# Enter the card
# Language selection - English, Hindi, Marathi
# Enter Pin
# Verify Pin
# Show Menu - Withdraw, Change Pin, Check balance
#   Withdraw - Saving, Current
#     Saving - Enter Amount
#       Processing Prompt and collect cash message
# Print Receipt option - Y/N
# Remove Card prompt
# Exit transaction

import time
import random
from users import users  # pyright: reportMissingImports=false


def display(options):
  for idx, option in enumerate(options, start=1):
    print(f"{idx}. {option}")


def load_msg(processing, msg, interval=1.0):
  print(f"\n{processing}")
  time.sleep(interval)
  print(msg)


def _input(msg):
  return int(input(msg))


_RECIEPT = ("|------------------------|\n"
            "|                        |\n"
            "|                        |\n"
            "| RECEIPT OF TRANSACTION |\n"
            "|                        |\n"
            "|                        |\n"
            "|========================|\n"
            "|------------------------|")

print("\nWELCOME TO THE GOTHAM CITY STATE BANK ATM NETWORK\n\n")
ins = input("Please press 'I' to insert your card for service >>> ")

if ins == "I" or ins == "i":
  print()
  languages = ["English", "Hindi"]
  display(languages)

  lang_inp = input("Please select your preferred language >>> ")
  if lang_inp == "2":
    print("Sorry for the inconvenience, we couldn't set Hindi as your "
          "preferred language. English would be set by default.")

  attempt = 1
  print("\nProcessing...")

  while attempt <= 3:
    time.sleep(1.5)
    user_pin = _input("Please enter your 4 digit ATM Pin >>> ")

    if user_pin in users:
      first_name = users[user_pin]["first_name"]
      last_name = users[user_pin]["last_name"]
      account_no = users[user_pin]["account_no"]
      balance = users[user_pin]["balance"]
      currency = users[user_pin]["currency"]

      load_msg("Processing...",
               f"\nHello {first_name} {last_name[0]}.\n"
               "What would you like to do?\n", 1.2)

      options = ["Withdraw", "Change Pin", "Check Balance"]
      display(options)

      opt_inp = _input("Please select from the above options >>> ")

      while True:
        if opt_inp in [1, 2, 3]:
          if opt_inp == 4:
            load_msg("Please wait...",
                     "We are fetching your account details...")
            time.sleep(2.0)
            print(f"Your account balance is {currency}{balance}.")
          elif opt_inp == 1:
            print("\nPlease wait...")
            time.sleep(1.0)

            wdw_options = ["Savings Account", "Current Account"]
            display(wdw_options)

            wdw_opt = _input("\nChoose account >>> ")
            if wdw_opt == 2:
              load_msg("Processing...",
                       ("You are not allowed to dispense from "
                        "your Current Account."), 1.2)
              break
            elif wdw_opt == 1:
              wdw_inp = _input("Please enter the amount >>> $")

              if wdw_inp > balance:
                print("Cannot withdraw amount greater than "
                      "account balance!")
              elif wdw_inp > 30000:
                otp = random.randint(111111, 999999)
                print(f"\nHINT: {otp}\n")
                otp_inp = _input("An OTP is sent to your "
                                 "phone XXX-XXX-1234. "
                                 "Please enter the OTP to "
                                 "proceed with your "
                                 "transaction >>> ")
                if otp == otp_inp:
                  balance -= wdw_inp
                  load_msg("Processing...\n",
                           "Please collect your cash...",
                           2.0)
                  print("Your account balance is "
                        f"{currency}{balance}")
                  receipt = input("Press 'Y' for printing "
                                  "transaction receipt >>> ")
                  if receipt == 'Y':
                    load_msg("Printing...\n", _RECIEPT)
                  users[user_pin]["balance"] = balance
                else:
                  print("Invalid OTP!")
              else:
                balance -= wdw_inp
                load_msg("Processing...\n",
                         "Please collect your cash...", 2.0)
                print("Your account balance is "
                      f"{currency}{balance}")
                receipt = input("Press 'Y' for printing "
                                "transaction receipt >>> ")
                if receipt == "Y":
                  load_msg("Printing...\n", _RECIEPT)
                users[user_pin]["balance"] = balance
            else:
              print("Invalid input!")
              break
          else:
            print("\nProcessing...")
            time.sleep(1.0)
            curr_pin = int(input("\nPlease enter your 4 digit ATM "
                                 "Pin >>> "))
            if curr_pin in users:
              new_pin = _input("Please enter your new 4 "
                               "digit ATM Pin >>> ")
              if len(str(new_pin)) == 4:
                temp = users[curr_pin]
                del users[curr_pin]
                users[new_pin] = temp
                load_msg("Updating...",
                         "ATM Pin successfully updated!", 2.0)
              else:
                print("Invalid pin!")
              break
            else:
              print("Entered ATM pin doesn't match our records!")
          break
        else:
          print("Please select a valid option!")
      time.sleep(1.0)
      load_msg("Please remove your card!",
               ("Thanks for visiting GOTHAM CITY STATE BANK ATM "
                "NETWORK... Have a good day!"), 3.0)
      break
    else:
      attempt += 1
      print(f"Invalid ATM Pin. You have {4 - attempt} attempt(s) "
            "remaining.")
else:
  print("Card not inserted!\nThanks for visiting... Have a good day!")
