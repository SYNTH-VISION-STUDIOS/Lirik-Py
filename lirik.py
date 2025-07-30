import time
from threading import Thread, Lock
import sys

lock = Lock()

# Fungsi untuk memberi warna teks
def colored(text, color_code="36"):
    return f"\033[{color_code}m{text}\033[0m"

# Fungsi animasi ketik
def animate_text(text, delay=0.05, color="36"):
    with lock:
        sys.stdout.write("\n")  # baris kosong di awal
        for char in colored(text, color):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(delay)
        sys.stdout.write("\n")  # baris baru di akhir

# Fungsi untuk tiap lirik
def sing_lyric(lyric, delay, speed, color):
    time.sleep(delay)
    animate_text(lyric, speed, color)

# Fungsi utama
def sing_song():
    lyrics = [
        ("Photobook with my mistakes", 0.08, "35"),
        ("Promises that we never got to make", 0.08, "35"),
        ("All the things I wanna talk about", 0.08, "35"),
        ("Hard to say it to myself", 0.1, "36"),
        ("Wintertime, once again", 0.08, "34"),
        ("In the snow I can see just where I've been", 0.08, "34"),
        ("How far I've made it in the world so cold", 0.08, "32"),
        ("Where I have everything", 0.08, "32"),
        ("But he's not you", 0.2, "31"),
        ("He's not you", 0.15, "31"),
        ("He will never be you", 0.15, "31"),
    ]

    delays = [
        0.5, 3.0, 6.0, 9.0,
        13.0, 16.0, 19.0, 22.0,
        26.0, 29.0, 31.5,
        35.0, 38.0, 40.5
    ]

    threads = []
    for i in range(len(lyrics)):
        text, speed, color = lyrics[i]
        t = Thread(target=sing_lyric, args=(text, delays[i], speed, color))
        threads.append(t)
        t.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    sing_song()
