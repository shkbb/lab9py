def calculate_cosmic_distance(speed_of_light_fraction, time_years):
    return speed_of_light_fraction * time_years


def calculate_simplified_gravity(mass1, mass2, cosmic_factor=1.0):
    return mass1 * mass2 * cosmic_factor


def calculate_time_dilation_approximation(speed_of_light_fraction, time_seconds):
    # Просте (не фізично точне) наближення
    if speed_of_light_fraction >= 1:
        raise ValueError("speed_of_light_fraction must be less than 1 for time dilation")
    return time_seconds / (1 - speed_of_light_fraction)


def main():
    while True:
        print("\nВиберіть розрахунок 'таємниці Всесвіту':")
        print("1 - Космічна відстань")
        print("2 - Спрощена гравітація")
        print("3 - Наближення сповільнення часу")
        print("0 - Вихід")

        choice = input("Ваш вибір: ")

        if choice == '0':
            print("До зустрічі у Всесвіті!")
            break

        try:
            if choice == '1':
                v = float(input("Введіть частку швидкості світла (0-1): "))
                t = float(input("Введіть час у роках: "))
                result = calculate_cosmic_distance(v, t)
                print(f"Приблизна космічна відстань становить: {result} світлових років.")

            elif choice == '2':
                m1 = float(input("Введіть масу першого об'єкта: "))
                m2 = float(input("Введіть масу другого об'єкта: "))
                cf = input("Введіть космічний фактор (натисніть Enter для 1.0): ")
                cosmic_factor = float(cf) if cf.strip() != '' else 1.0
                result = calculate_simplified_gravity(m1, m2, cosmic_factor)
                print(f"Спрощений показник гравітаційної взаємодії: {result}.")

            elif choice == '3':
                v = float(input("Введіть частку швидкості світла (0-<1): "))
                ts = float(input("Введіть час у секундах: "))
                result = calculate_time_dilation_approximation(v, ts)
                print(f"Приблизне сповільнення часу: {result} секунд (за вашим спрощенням).")

            else:
                print("Невірний вибір. Спробуйте ще раз.")
                continue

        except ValueError as e:
            print(f"Помилка введення: {e}. Будь ласка, введіть коректні числові значення або 0 для виходу.")
            continue

        # Після успішного розрахунку
        again = input("Бажаєте виконати ще один розрахунок? (y/n): ")
        if again.lower() not in ('y', 'yes', 'т', 'так'):
            print("Дякую за використання космічного калькулятора!")
            break

if __name__ == "__main__":
    main()
