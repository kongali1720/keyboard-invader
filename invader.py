
---

### 🧾 `invader.py` (main script)

```python
import curses
import random
import time

ALIEN_CHARS = list("ABCDEFGHJKLMNOPQRSTUVWXYZ1234567890")

def main(stdscr):
    curses.curs_set(0)
    stdscr.nodelay(True)
    height, width = stdscr.getmaxyx()
    score = 0
    alien = {
        "char": random.choice(ALIEN_CHARS),
        "x": random.randint(1, width - 2),
        "y": 1
    }

    while True:
        stdscr.clear()
        stdscr.addstr(0, 2, f"Score: {score}")
        stdscr.addstr(alien["y"], alien["x"], alien["char"])
        stdscr.refresh()

        key = stdscr.getch()
        if key != -1:
            if chr(key).upper() == alien["char"]:
                score += 1
                alien = {
                    "char": random.choice(ALIEN_CHARS),
                    "x": random.randint(1, width - 2),
                    "y": 1
                }

        alien["y"] += 1
        if alien["y"] >= height - 1:
            break

        time.sleep(0.1)

    stdscr.clear()
    stdscr.addstr(height // 2, width // 2 - 7, f"GAME OVER!")
    stdscr.addstr(height // 2 + 1, width // 2 - 9, f"Final Score: {score}")
    stdscr.refresh()
    time.sleep(3)

if __name__ == "__main__":
    curses.wrapper(main)
