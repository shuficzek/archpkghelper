import subprocess

package = input("What package to install/uninstall? >>> ")
action = input("What to do? 1=Install 2=Uninstall >>> ")

if action == "1":
    subprocess.run(f"sudo -S pacman -S --noconfirm {package}", shell=True)
elif action == "2":
    subprocess.run(f"sudo -S pacman -Rns --noconfirm {package}", shell=True)
else:
    print("Invalid input, bro. Pick 1 or 2.")