from datetime import datetime

today=datetime(2019,9,4)


def check_birthdate(year, month, day):
        birthdate=datetime(int(year), int(month), int(day))
        if( today < birthdate):
                
                return False
        else:
                return True

def calculate_age(year, month, day):
        birthdate=datetime(int(year), int(month), int(day))
        difference = today - birthdate
        age=int(difference.days / 365)
        print("you are ",age, " years old" )

def main():
        
        
        year1=input("Enter year of birth: ")
        month1=input("Enter month of birth: ")
        day1=input("Enter day of birth: ")
        
        if(check_birthdate(year1, month1, day1)== True ):
                calculate_age(year1, month1, day1)
        else:
                print("Invalid birthdate")

        
if __name__ == '__main__':
	main()
