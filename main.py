import subprocess

print("Select a package manager to run:")
print("pacman >>> 1")
print("yay >>> 2")

choice = input("Enter 1 or 2 >>> ")

if choice == "1":
    subprocess.run(["python", "pacman.py"])
elif choice == "2":
    subprocess.run(["python", "yay.py"])
else:
    print("Invalid choice!")
