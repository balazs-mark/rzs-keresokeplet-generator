#!/usr/bin/ python
# -*- coding: utf-8 -*-

from config import Config


class PrintDeveloperAndProgramVersion:

    def __init__(self) -> None:

        print("\n"
            "_________________________________________________________________________________________________________________\n"
            "|                                                                                                                |\n"
            f"|     Képlet Generátor az RZS Szöveges Keresőjéhez ({Config.version_in_use})                                                      |\n"
            f"|     Legfrisebb verzió letöltése: https://github.com/balazs-mark/{Config.name_of_project_on_github}/releases/latest     |\n"
            "|________________________________________________________________________________________________________________|\n"
            "|                                                                                                                |\n"
            "|     Hiba vagy további képesség kérése esetén kérlek vedd fel a kapcsolatot a fejlesztővel:                     |\n"
            "|                                                                                                                |\n"
            "|         Márk Balázs r. hdgy.                                                                                   |\n"
            "|         BRFK BÜFO KBEO                                                                                         |\n"
            "|         06-20/563-10-12                                                                                        |\n"
            "|         markb@budapest.police.hu                                                                               |\n"
            "|________________________________________________________________________________________________________________|\n"
            )