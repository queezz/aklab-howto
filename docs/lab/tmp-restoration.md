# 🚀 Mitsubishi Turbo Pump Restoration

## 🔎 Overview

An early-1990s Mitsubishi turbo molecular pump (TMP) and controller were restored and integrated into a small laboratory vacuum system.

The pump had been unused for many years and initially appeared non-functional.  
After mechanical integration and controller diagnostics the system successfully reached the high-vacuum regime.

The restoration also served as an opportunity to practice vacuum welding and confirm the functionality of aging electronics.

---

## 📜 History

The pump originally came to our laboratory as a gift from a retired professor to my advisor.

Around **2019–2020** we first attempted to use it.  
At that time the pump and controller were available, but the connecting cable was missing.

A custom cable was ordered from a manufacturer for roughly **30,000 JPY**.

Because no compatible flanges were available, a temporary test was performed by simply sealing the inlet with a large stainless disk and backing the pump with an oil rotary pump.  
The controller immediately produced an error and the pump never started.

After several attempts the project was abandoned.  
The pump had originally been intended for a **VUV spectrometer system**, which itself never materialized.

---

## 🔧 Flange Adapter Fabrication

At the end of last year I returned to the pump as a side project.

To integrate the pump properly into the vacuum hardware a **VF65 → KF40 stainless steel adapter nipple** was required.

During the previous months I had:

- purchased a [TIG welder](../hardware/equipment/tig-welder.md)
- built a small welding workstation
- practiced TIG welding for several weeks

An unused stainless flange from an earlier **movable Langmuir probe project** was available.  
Together with a KF40 welding nipple it was used to fabricate the adapter.

The flange was TIG welded and tested:

- rough pump test — no leaks detected  
- helium leak test using a QMS — no measurable leak

This confirmed that the adapter was vacuum-tight and suitable for the system.

---

## ⚡ Controller Diagnostics

After installing the new flange and attaching an ionization gauge, the turbo pump still refused to start.

The controller was opened for inspection.

Inside the controller a **NiCd backup battery** used for the hour counter had leaked and contaminated part of the PCB.

The board was cleaned using:

- distilled / purified water
- citric acid
- ethanol for final drying

After thorough drying the controller was reassembled.

Initially the pump still did not start.  
However, repeated start attempts eventually resulted in the pump spinning up.

The most likely explanation is **reforming of aged electrolytic capacitors** in the controller power supply.

---

## ▶️ First Startup

After several reset and start cycles the controller successfully accelerated the turbo pump.

Once the capacitors had warmed up and partially reformed, the controller behaved normally and the pump could be started and stopped reliably.

---

## 📉 Pump-down Results

| Day | Pressure |
|----|----|
| Tuesday | 5.8×10⁻⁵ Torr |
| Wednesday | 5.6×10⁻⁷ Torr |
| Thursday | 3.6×10⁻⁷ Torr |

The gradual improvement likely reflects continued conditioning of the vacuum system and stabilization of the controller electronics.

---

## 💡 Observations

Despite being more than thirty years old, the turbo pump and controller remain functional.

Vacuum equipment from this period was often designed conservatively using discrete through-hole components, making it relatively robust and serviceable even decades later.

The project also confirmed the quality of the welded vacuum adapter and demonstrated that the pump can still reach the high-vacuum regime.

---


## 🖼️ Image Gallery

![Busted Ni/Cd battery for the hours counter. Removed and cleand.](images/IMG_20260302_162258.jpg)
![IMG_20260302_172154](images/IMG_20260302_172154.jpg){data-title="Controller board"}
![IMG_20260302_172220](images/IMG_20260302_172220.jpg)
![IMG_20260302_172243](images/IMG_20260302_172243.jpg)
![IMG_20260302_180454](images/IMG_20260302_180454.jpg)
![IMG_20260303_182511](images/IMG_20260303_182511.jpg)
![IMG_20260303_182614](images/IMG_20260303_182614.jpg)
![IMG_20260304_111803](images/IMG_20260304_111803.jpg)
![IMG_20260304_111844](images/IMG_20260304_111844.jpg)
![IMG_20260304_153849](images/IMG_20260304_153849.jpg)
![IMG_20260304_153859](images/IMG_20260304_153859.jpg)
![IMG_20260305_140604](images/IMG_20260305_140604.jpg)
![IMG_20260305_140608](images/IMG_20260305_140608.jpg)
![IMG_20260305_140615](images/IMG_20260305_140615.jpg)
