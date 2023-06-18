import random
import curses

def main(stdscr):
    # 콘솔 환경 설정
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    # 콘솔 크기 가져오기
    sh, sw = stdscr.getmaxyx()

    # 뱀 초기 위치 설정
    snake_x = sw // 4
    snake_y = sh // 2

    # 뱀 몸통 설정
    snake_body = [
        [snake_y, snake_x],
        [snake_y, snake_x - 1],
        [snake_y, snake_x - 2]
    ]

    # 음식 위치 설정
    food = [sh // 2, sw // 2]
    stdscr.addch(food[0], food[1], curses.ACS_PI)

    # 초기 이동 방향 설정
    key = curses.KEY_RIGHT

    # 게임 루프
    while True:
        # 다음 키 입력 받기
        next_key = stdscr.getch()
        key = key if next_key == -1 else next_key

        # 새로운 머리 위치 계산
        new_head = [snake_body[0][0], snake_body[0][1]]

        if key == curses.KEY_DOWN:
            new_head[0] += 1
        if key == curses.KEY_UP:
            new_head[0] -= 1
        if key == curses.KEY_LEFT:
            new_head[1] -= 1
        if key == curses.KEY_RIGHT:
            new_head[1] += 1

        # 뱀이 벽에 부딪혔는지 확인
        if (
            new_head[0] in [0, sh] or
            new_head[1] in [0, sw] or
            new_head in snake_body[1:]
        ):
            stdscr.addstr(sh // 2, sw // 2, "게임 오버!")
            stdscr.refresh()
            stdscr.getch()
            break

        # 새로운 머리 추가
        snake_body.insert(0, new_head)

        # 음식 먹었는지 확인
        if snake_body[0] == food:
            # 음식 위치 재설정
            food = None
            while food is None:
                nf = [
                    random.randint(1, sh - 1),
                    random.randint(1, sw - 1)
                ]
                food = nf if nf not in snake_body else None
            stdscr.addch(food[0], food[1], curses.ACS_PI)
        else:
            # 꼬리 제거
            stdscr.addch(snake_body[-1][0], snake_body[-1][1], ' ')
            snake_body.pop()

        # 뱀 그리기
        stdscr.addch(snake_body[0][0], snake_body[0][1], curses.ACS_CKBOARD)

# 게임 실행
curses.wrapper(main)
