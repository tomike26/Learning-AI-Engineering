Monday = 2
Tuesday = 2.5
Wednesday = 2.5
Thursday = 2
Friday = 2
Saturday = 5
Sunday = 2

weekly_total = Monday + Tuesday + Wednesday + Thursday + Friday + Saturday + Sunday
print("Weekly Total:" , weekly_total)

daily_average = round(weekly_total / 7, 1)

print("Daily average:", daily_average)

yearly_total = weekly_total * 52

print("Total for 52 weeks:", yearly_total)


saturday_percentage = round((Saturday / weekly_total) * 100, 1)

print("Saturday percentage:", saturday_percentage, "%")

print()
(print("Python", "PyTorch", "LangGraph", sep=" | "))