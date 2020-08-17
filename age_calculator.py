from datetime import datetime

today=datetime.now()



def check_birthdate(year, month, day):
        birthdate=datetime(year, month, day)
        if( today <= birthdate):
                return False
        else:
                return True

def calculate_age(year, month, day):
        birthdate=datetime(year, month, day)
        difference = today - birthdate
        age=int(difference.days / 365)
        print("you are %d years old" % (age))

def main():
        
        
        year1=eval(input("Enter year of birth: "))
        month1=eval(input("Enter month of birth: "))
        day1=eval(input("Enter day of birth: "))
        
        if check_birthdate(year1, month1, day1):
                calculate_age(year1, month1, day1)
        else:
                print("Invalid birthdate")

        
if __name__ == '__main__':
	main()
