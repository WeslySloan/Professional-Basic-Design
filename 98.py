def find_long_login_users():
    long_login_users = []
    while True:
        try:
            line = input()
        except EOFError:
            break

        try:
            user_id, login_time, logout_time = line.strip().split(', ')
        except ValueError:
            continue

        login_hour, login_minute = map(int, login_time.split(':'))
        logout_hour, logout_minute = map(int, logout_time.split(':'))

        elapsed_hour = logout_hour - login_hour
        elapsed_minute = logout_minute - login_minute
        if elapsed_minute < 0:
            elapsed_minute += 60
            elapsed_hour -= 1

        if elapsed_hour >= 1:  # 2시간 대신 1시간 이상으로 변경
            long_login_users.append((user_id, f"{elapsed_hour:02d}:{elapsed_minute:02d}"))

    return long_login_users


long_login_users = find_long_login_users()
for user_id, elapsed_time in long_login_users:
    print(f"{user_id} {elapsed_time}")
