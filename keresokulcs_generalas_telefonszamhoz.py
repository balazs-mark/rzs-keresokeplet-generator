#!/usr/bin/ python
# -*- coding: utf-8 -*-

import sys
import os
from modules.print_developer_and_program_version import PrintDeveloperAndProgramVersion
from modules.check_update import CheckUpdate


class SzovegbanyaszKepletGeneraloTelefonszamhoz:

    def __init__(self) -> None:
        try:
            PrintDeveloperAndProgramVersion()
            if "--no-update" not in sys.argv:
                CheckUpdate()
            self.generate()
            print("\n"
                "A generálás sikeresen véget ért.\n"
                "A keresőkulcsokat a 'keresokulcsok' nevű mappában találod hívószámok szerint külön '.txt' fájlokban.\n"
            )
        except KeyboardInterrupt:
            print("\n\nKilépés...")
            exit()
        except WrongParameterError:
            print("\n"
                "Kérlek a program futtatásához az alábbi lehetőségek valamelyikét használd:\n"
                    "\t'python keresokulcs_generalas_telefonszamhoz.py --fájl'\n"
                    "\t'python keresokulcs_generalas_telefonszamhoz.py <telefonszám>'\n"
                    "\t'python keresokulcs_generalas_telefonszamhoz.py'\n"
            )
            exit()
        except UnkownCountryCodeError as unknown_country_code:
            print("\n"
                f"A +{unknown_country_code} előhívójú országok telefonszámaira a program jelenleg nincs felkészítve. :(\n"
                "Ha szükséged lenne erre a képességre kérlek vedd fel a kapcsolatot a fejlesztővel!\n"
                f"HA FÁJLBÓL TÖLTÖTTED BE A TELEFONSZÁMOKAT AKKOR TÁVOLÍTSD EL A LISTÁBÓL A +{unknown_country_code}-AL KEZDŐDŐ TELEFONSZÁMOKAT ÉS ÚGY FUTTASD ÚJRA A PROGRAMOT!\n"
            )
            exit()
        except NoPhoneNumberInFileError as name_of_empty_file:
            print("\n"
                f"A {name_of_empty_file} fájlban nem található telefonszám.\n"
                "Kérlek írd be a számokat, majd futtasd újra a programot.\n"
            )
            exit()
        except NotMobilePhoneNumber as not_mobilephone_number:
            print("\n"
                f"A nem 11 számjegyből álló telefonszámokra a program jelenleg nincs felkészítve. :(\n"
                "Ha szükséged lenne erre a képességre kérlek vedd fel a kapcsolatot a fejlesztővel!\n"
                f"HA FÁJLBÓL TÖLTÖTTED BE A TELEFONSZÁMOKAT AKKOR TÁVOLÍTSD EL A LISTÁBÓL A {not_mobilephone_number} TELEFONSZÁMOT, ILLETVE A TÖBBI NEM MAGYAR MOBILTELEFONSZÁMOT ÉS ÚGY FUTTASD ÚJRA A PROGRAMOT!\n"
            )
            exit()
        finally:
            pass


    @staticmethod
    def read_phone_number_from_command_line() -> str:
        typed_phone_number = sys.argv[1]
        return str(typed_phone_number)


    def read_phone_numbers_from_file(self, filename) -> list:
        typed_phone_numbers = []
        try:
            with open(filename, "r") as list:
                list_binary = list.read()
                for phone_number in list_binary.split("\n"):
                    if len(phone_number) > 6:
                        typed_phone_numbers.append(phone_number)
            if len(typed_phone_numbers) < 1:
                raise NoPhoneNumberInFileError(filename)
            return typed_phone_numbers
        except FileNotFoundError:
            open(filename, "a").close()
            self.read_phone_numbers_from_file(filename=filename)


    def get_phone_numbers(self) -> list:
        typed_phone_numbers = []
        try:
            if "--fájl" in sys.argv:
                typed_phone_numbers = self.read_phone_numbers_from_file(filename="telefonszámok.txt")
            elif sys.argv[1] != "--no-update":
                typed_phone_number = self.read_phone_number_from_command_line()
                typed_phone_numbers.append(typed_phone_number)
            else:
                typed_phone_number = input("\nKérlek add meg a telefonszámot:\n\t> ")
                typed_phone_numbers.append(typed_phone_number)
        except IndexError:
            typed_phone_number = input("\nKérlek add meg a telefonszámot:\n\t> ")
            typed_phone_numbers.append(typed_phone_number)
        return typed_phone_numbers

    
    @staticmethod
    def remove_nondigit_characters(phone_number_with_nondigit_characters) -> str:
        phone_number_with_only_digit_characters = ""
        digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for character in phone_number_with_nondigit_characters:
            if character in digits:
                phone_number_with_only_digit_characters = phone_number_with_only_digit_characters + character
            else:
                pass
        if phone_number_with_only_digit_characters == "":
            raise WrongParameterError()
        else:
            return phone_number_with_only_digit_characters


    def generate(self) -> None:
        typed_phone_numbers = self.get_phone_numbers()
        for typed_phone_number in typed_phone_numbers:
            phone_number = self.remove_nondigit_characters(typed_phone_number)
            country_code = phone_number[0:2]
            match country_code:
                case "06" | "36": # Hungarian country codes
                    phone_number_without_country_code = phone_number[2:]
                    match len(phone_number):
                        case 11:
                            code = f'''
        1. keresőkulcs a {typed_phone_number} telefonszámhoz:
        ("06{phone_number_without_country_code}" OR\
        "06{phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]}{phone_number_without_country_code[5:7]}{phone_number_without_country_code[7:9]}" OR\
        "06{phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]}-{phone_number_without_country_code[5:7]}{phone_number_without_country_code[7:9]}" OR\
        "06{phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]}-{phone_number_without_country_code[5:7]}-{phone_number_without_country_code[7:9]}" OR\
        "36{phone_number_without_country_code}" OR\
        "36{phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]}{phone_number_without_country_code[5:7]}{phone_number_without_country_code[7:9]}" OR\
        "36{phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]}-{phone_number_without_country_code[5:7]}{phone_number_without_country_code[7:9]}" OR\
        "36{phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]}-{phone_number_without_country_code[5:7]}-{phone_number_without_country_code[7:9]}" OR\
        "36-{phone_number_without_country_code[0:2]}{phone_number_without_country_code[2:5]}{phone_number_without_country_code[5:7]}{phone_number_without_country_code[7:9]}" OR\
        "36-{phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]}{phone_number_without_country_code[5:7]}{phone_number_without_country_code[7:9]}" OR\
        "36-{phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]}-{phone_number_without_country_code[5:7]}{phone_number_without_country_code[7:9]}" OR\
        "36-{phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]}-{phone_number_without_country_code[5:7]}-{phone_number_without_country_code[7:9]}")
        2. keresőkulcs a {typed_phone_number} telefonszámhoz:
        ("06{phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]} {phone_number_without_country_code[5:7]}{phone_number_without_country_code[7:9]}" OR\
        "06{phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]} {phone_number_without_country_code[5:7]} {phone_number_without_country_code[7:9]}" OR\
        "36{phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]} {phone_number_without_country_code[5:7]}{phone_number_without_country_code[7:9]}" OR\
        "36{phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]} {phone_number_without_country_code[5:7]} {phone_number_without_country_code[7:9]}" OR\
        "36 {phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]} {phone_number_without_country_code[5:7]}{phone_number_without_country_code[7:9]}" OR\
        "36 {phone_number_without_country_code[0:2]}/{phone_number_without_country_code[2:5]} {phone_number_without_country_code[5:7]} {phone_number_without_country_code[7:9]}" OR\
        "06{phone_number_without_country_code[0:2]} {phone_number_without_country_code[2:5]} {phone_number_without_country_code[5:7]}{phone_number_without_country_code[7:9]}" OR\
        "06{phone_number_without_country_code[0:2]} {phone_number_without_country_code[2:5]} {phone_number_without_country_code[5:7]} {phone_number_without_country_code[7:9]}" OR\
        "36{phone_number_without_country_code[0:2]} {phone_number_without_country_code[2:5]} {phone_number_without_country_code[5:7]}{phone_number_without_country_code[7:9]}" OR\
        "36{phone_number_without_country_code[0:2]} {phone_number_without_country_code[2:5]} {phone_number_without_country_code[5:7]} {phone_number_without_country_code[7:9]}" OR\
        "36 {phone_number_without_country_code[0:2]} {phone_number_without_country_code[2:5]} {phone_number_without_country_code[5:7]}{phone_number_without_country_code[7:9]}" OR\
        "36 {phone_number_without_country_code[0:2]} {phone_number_without_country_code[2:5]} {phone_number_without_country_code[5:7]} {phone_number_without_country_code[7:9]}"\
        )
        '''
                            # print(code)
                            self.write_into_txt_file(filename=f"{phone_number}.txt", content=code)
                        case _:
                            raise NotMobilePhoneNumber(typed_phone_number)
                case _:
                    raise UnkownCountryCodeError(country_code)


    def write_into_txt_file(self, filename, content) -> None:
        try:
            with open(f"keresokulcsok/{filename}", "w") as result_file:
                result_file.write(content)
        except FileNotFoundError:
            os.mkdir("keresokulcsok")
            self.write_into_txt_file(filename=filename, content=content)


class WrongParameterError(ValueError):
    pass

class UnkownCountryCodeError(ValueError):
    pass

class NoPhoneNumberInFileError(ValueError):
    pass

class NotMobilePhoneNumber(ValueError):
    pass


if __name__ == "__main__":
    SzovegbanyaszKepletGeneraloTelefonszamhoz()
