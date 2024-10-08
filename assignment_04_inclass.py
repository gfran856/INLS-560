#Assignent 4
#Constants required for automatic admission on a travel basketball league.
REQUIRED_MEDALS = 2
YEARS_COMPETING = 4


medals_won = int(input('How many medals have you won in the past? '))
years_practicing = int(input("How many years have you been practicing? "))

if medals_won >= REQUIRED_MEDALS and years_practicing >= YEARS_COMPETING:
    print("Congratulations! you are eligible for an AUTOMATIC admission to the team")
else:
    print(f'''
          Sorry, you do not meet the requirments for Automatic admission for the team.

          You need at least:
          - {REQUIRED_MEDALS} total medals won overtime
          AND
          - at least {YEARS_COMPETING} years competing 
          
          since you do not meet these requirments, you are still eligible to try-out for the team! See you there!
          ''')