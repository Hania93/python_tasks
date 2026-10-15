# 8. Ile dni do wakacji — policz dni do 1 lipca 2027 ( date(2027, 7, 1) - date.today() , .days ) i zamień je
# na tygodnie i dni ( // , % ).

from datetime import date

total_days = date(2027,7,1) - date.today()
weeks = total_days.days // 7
days = total_days.days % 7

print(f"Do wakacji zostało {total_days.days} dni, czyli {weeks} tyg i {days} dni")
