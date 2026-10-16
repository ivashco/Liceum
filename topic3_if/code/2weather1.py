season = input().strip()
weather = input().strip()
if (season == "лето" and weather == "дождь") or (
    season == "зима" and weather == "снег"
):
    print("Нормально!")
elif (season == "лето" and weather == "снег") or (
    season == "зима" and weather == "дождь"
):
    print("Глобальное изменение климата!")
else:
    print("Не хватает данных.")
