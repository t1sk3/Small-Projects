
from stdatmos import isa
from matplotlib import pyplot as plt
from math import sqrt
import time
from tqdm import tqdm
lstt = []
lstp = []
lstrho = []
lsth = []
lsts = []
for h in tqdm(range(0,86001, 50)):
    t, p, rho = isa(h)
    #print(h)
    s = sqrt(1.4*287*t)
    lsth.append(h)
    lstt.append(t)
    lstp.append(p)
    lstrho.append(rho)
    lsts.append(s)

plt.figure(1)

plt.subplot(2,2,1)
plt.plot(lstt, lsth)
plt.title("Temperature in the atmosphere according to height")
plt.xlabel("Temperature [K]")
plt.ylabel("Height [m]")

plt.subplot(2,2,2)
plt.plot(lstp, lsth)
plt.title("Pressure in the atmosphere according to height")
plt.xlabel("Presssure [Pa]")
plt.ylabel("Height [m]")

plt.subplot(2,2,3)
plt.plot(lstrho, lsth)
plt.title("Airdensity in the atmosphere according to height")
plt.xlabel("Airdensity [kg/m^3]")
plt.ylabel("Height [m]")

plt.subplot(2,2,4)
plt.plot(lsts, lsth)
plt.title("Speed of sound in the atmosphere according to height")
plt.xlabel("Speed of sound [m/s]")
plt.ylabel("Height [m]")

plt.show()