import os
import time

# Membersihkan layar
os.system('clear')

# Animasi teks
print("\033[1;33mMemulai proses...\033[0m")
time.sleep(1)
print("\033[1;32mMenyiapkan tampilan...\033[0m")
time.sleep(1)

# Banner
print("\033[1;36m====================================")
print("      ZUDENZA TEAM - TERMUX")
print("====================================")
print("\033[0m")

# Informasi Media Sosial
print("\033[1;34mFollow kami di media sosial:\033[0m")
print("Youtube: \033[1;32m@zudenza\033[0m")
print("Github: \033[1;32m@zudenza\033[0m")
print("Gmail: \033[1;32mzudenza@hotmail.com\033[0m")
print("")

# Mengganti Prompt (Simulasi mengubah prompt bash)
bashrc_path = os.path.expanduser('~/.bashrc')
with open(bashrc_path, 'a') as bashrc:
    bashrc.write(r'PS1="\033[1;35m\u@\h \033[1;34m\w \$ \033[0m"\n')

# Menambahkan Alias
with open(bashrc_path, 'a') as bashrc:
    bashrc.write("alias cls='clear'\n")
    bashrc.write("alias ll='ls -la'\n")
    bashrc.write("alias update='pkg update && pkg upgrade'\n")
    bashrc.write("alias h='htop'\n")

# Animasi loading
print("\033[1;33mWelcome to Termux in theme ZUDENZA TEAM - loading.....\033[0m")
time.sleep(1)

# Pesan Selesai
print("\033[1;32mSUCCESS\033[0m")