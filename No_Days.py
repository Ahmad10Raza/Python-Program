from  datetime import date
f_date=date(2018,6,22)
l_date=date(2022,12,7)
# f_date=date(int(input("Enter present Date(Y/M/D): ")))
# l_date=date(int(input("Enter  past Date(Y/M/D): ")))
dayss=l_date-f_date
print(dayss.days)
