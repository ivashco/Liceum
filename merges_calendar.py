from pathlib import Path
from icalendar import Calendar, Event
from datetime import datetime, time
import pytz


def normalize_dtstart(dt):
    """
    Приводит DTSTART к UTC для сравнения.
    Если время «наивное» (без tzinfo), считаем, что оно уже в едином формате,
    но всё равно нормализуем в UTC, чтобы сравнение было однозначным.
    """
    if dt.tzinfo is None:
        # Если нет часового пояса — считаем, что все файлы в одном формате,
        # и для сравнения просто добавляем условный UTC (чтобы не зависеть от локальной зоны).
        dt = pytz.utc.localize(dt)
    return dt.astimezone(pytz.utc)


def merge_calendars_from_folder(folder_path, output_file):
    folder = Path(folder_path)
    ics_files = list(folder.glob("*.ics"))

    if not ics_files:
        print(f"В папке {folder} не найдено .ics файлов.")
        return

    seen_starts = set()
    merged_cal = Calendar()
    merged_cal.add("prodid", "-//Alice AI Calendar Merger//RU")
    merged_cal.add("version", "2.0")
    merged_cal.add("calscale", "GREGORIAN")

    for path in ics_files:
        with path.open("rb") as f:
            cal = Calendar.from_ical(f.read())

        for component in cal.walk():
            if component.name != "VEVENT":
                continue

            dtstart = component.get("dtstart")
            if not dtstart:
                continue  # событие без DTSTART пропускаем

            dt_obj = dtstart.dt

            if isinstance(dt_obj, datetime):
                key = normalize_dtstart(dt_obj)
            else:
                # all-day событие: считаем как полночь UTC этого дня
                key = pytz.utc.localize(datetime.combine(dt_obj, time.min))

            key_str = key.isoformat()

            if key_str in seen_starts:
                continue  # дубликат по DTSTART
            seen_starts.add(key_str)

            new_event = Event()
            for name, value in component.items():
                if name == "UID":
                    continue  # не копируем UID, чтобы избежать конфликтов
                new_event.add(name, value)

            merged_cal.add_component(new_event)

    with open(output_file, "wb") as f:
        f.write(merged_cal.to_ical())

    print(f"Готово! Объединённый календарь сохранён в {output_file}")
    print(f"Обработано файлов: {len(ics_files)}")
    print(f"Уникальных событий (по DTSTART): {len(seen_starts)}")


if __name__ == "__main__":
    # Укажите путь к папке с .ics файлами
    input_folder = r"C:\Users\Ivashco\Downloads\calendar"  # Windows
    output_path = "merged_calendar.ics"

    merge_calendars_from_folder(input_folder, output_path)
