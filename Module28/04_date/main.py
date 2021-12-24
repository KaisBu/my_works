class Date:

    def __init__(self, day=0, month=0, year=0) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __str__(self) -> str:
        return 'День: {day}\tМесяц: {month}\tГод: {year}'.format(
            day=self.day,
            month=self.month,
            year=self.year
        )

    @classmethod
    def from_string(cls, date: str) -> 'Date':

        if Date.is_date_valid(date):
            date_list = date.split('-')
            day, month, year = int(date_list[0]), int(date_list[1]), int(date_list[2])
            instance = cls(day, month, year)
        else:
            print('Date is invalid')
            instance = cls(0, 0, 0)
        return instance

    @classmethod
    def is_date_valid(cls, date: str) -> bool:

        if not date.isalpha():
            date_list = date.split('-')
            day, month, year = int(date_list[0]), int(date_list[1]), int(date_list[2])

            if 0 <= year <= 9999:
                if 0 < month <= 12 and month != 2:
                    if month % 2 == 0:
                        return Date.is_day_valid(day, 30)
                    else:
                        return Date.is_day_valid(day, 31)
                elif month == 2:
                    if year % 5 == 0:
                        return Date.is_day_valid(day, 29)
                    else:
                        return Date.is_day_valid(day, 28)
                else:
                    return False
            else:
                return False
        else:
            return False

    @classmethod
    def is_day_valid(cls, day: int, max_day: int) -> bool:
        if 0 < day <= max_day:
            return True
        else:
            return False


date1 = Date.from_string('10-12-2077')
print(date1)
date2 = Date.from_string('155-14-2077')
print(date2)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
print(Date.is_date_valid('29-2-2077'))

