import os

print("""[0] pip\n[1] pip2\nWhich one do you use?""")

c = input(">>>: ")
if c == "0":
    os.system("python -m pip install --upgrade pip")
    os.system("python -m pip install flake8 pytest")
    os.system("pip install requests")
    os.system("pip install colorama")
   

elif c == "1":
    os.system("python -m pip install --upgrade pip")
    os.system("python -m pip install flake8 pytest")
    os.system("pip2 install requests")
    os.system("pip2 install colorama")
   
  print("Done.")
