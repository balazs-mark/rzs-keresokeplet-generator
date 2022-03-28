# Keresőképlet Generátor RZS Szövegbányászhoz</h1>

## Telepítés:
1) [Python](https://www.python.org/downloads/) telepítése *(ha nem az összes felhasználónak, hanem csak magadnak telepíted akkor rendszergazdai jogosultság nélkül is telepíthető)*
2) Szükséges Python modulok telepítése *(police.hu-s hálózaton keresztül nem telepíthető, mert a tűzfal nem engedi át, de pl. telefonról rákötött internettel rendszergazdai jogosultság nélkül telepíthető)* a `pip install -r requirements.txt` paranccsal.


## Használat:

### Keresőkulcs generálás telefonszámhoz fájlból:
1) Ha a fő könyvtárban nem található egy `telefonszámok.txt` fájl akkor azt hozd létre.
2) A `telefonszámok.txt` fájlba másold be a telefonszámokat úgy, hogy mindegyik telefonszám új sorba kerüljön.
3) A parancssorban be kell lépni a könyvtárba és ott a `python keresokulcs_generalas_telefonszamhoz.py --fájl` parancsot lefuttatni
4) A keresőképleteket a `keresokulcsok` mappában találod, hívószámonként külön `.txt` fájlban.
> A RZS korlátai miatt (mivel egyben a teljes képletet nem tudja kezelni) a keresőkulcsot darabolni kellett. A keresőképletekkel külön-külön végezz keresést!

### Keresőkulcs generálás parancssorban megadott telefonszámhoz:
1) A parancssorban be kell lépni a könyvtárba és ott a `python keresokulcs_generalas_telefonszamhoz.py <telefonszám>` parancsot lefuttatni.  
*(pl.: `python keresokulcs_generalas_telefonszamhoz.py +36-20/111-22-33`)*
2) A keresőképleteket a `keresokulcsok` mappában találod, hívószámonként külön `.txt` fájlban.

> **A program ilyen módon történő használata esetén egyszerre csupán 1 db telefonszám megadására van lehetőség!**  

> A RZS korlátai miatt (mivel egyben a teljes képletet nem tudja kezelni) a keresőkulcsot darabolni kellett.  
> A keresőképletekkel külön-külön végezz keresést!

### Keresőkulcs generálás futtatás során megadott telefonszámhoz:
1) A parancssorban be kell lépni a könyvtárba és ott a `python keresokulcs_generalas_telefonszamhoz.py` parancsot lefuttatni.
2) A program a futtatást követően fogja kérni a telefonszámot. Azt be kell gépelni, majd az `Enter` leütésével elfogadtatni.
3) A keresőképleteket a `keresokulcsok` mappában találod, hívószámonként külön `.txt` fájlban.

> **A program ilyen módon történő használata esetén egyszerre csupán 1 db telefonszám megadására van lehetőség!**  

> A RZS korlátai miatt (mivel egyben a teljes képletet nem tudja kezelni) a keresőkulcsot darabolni kellett.  
> A keresőképletekkel külön-külön végezz keresést!