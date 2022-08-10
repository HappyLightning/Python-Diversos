import pyautogui as auto
import time

# Abre o software e em seguida espera.
auto.press('win')
auto.write('OpenVPN', interval=0.05)
auto.press('enter')
time.sleep(4)
# Liga a VPN
auto.click(x= 529, y= 187)
# Da input da sua senha
file = open(r'C:\Users\Felipe\Documents\Senha_VPN.txt', 'r')
l = file.readlines(); senha = l.pop(1)
auto.write(senha, interval =0.05)
file.close()
# Esperar
time.sleep(1)
auto.click(x= 634, y=430)
# Minimiza o software
time.sleep(2.5)
auto.click(x= 847, y=31)