# Flashing the firmware

Since we're using SAMD21 microcontroller you'll be needing "**BOSSA**"  
resource: [Link](https://www.shumatech.com/web/products/bossa)  

> [!NOTE]
> bossac is easier


1. Connect your MCU to PC
2. press "reset" twice to enter bootloader mode
3. Navigate to your binary folder  
run:
```
./bossac.exe -i -d --port=COM8 -U true -i -e -w -v ./EcoDecible.bin -R
```
(Change --port to your device's port)  

4. Your device should be ready after flashing
