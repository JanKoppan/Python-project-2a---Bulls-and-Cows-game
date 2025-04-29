# Python-project-2a---Bulls-and-Cows-game
Hra "Bulls and Cows"

Tento projekt byl vytvořen jako cvičení v jazyce Python, zaměřené na procvičení práce s funkcemi, podmínkami, cykly, generováním náhodných čísel, uživatelským vstupem a časovými funkcemi. Jedná se o jednoduchou konzolovou verzi populární hry "Bulls and Cows", kde hráč hádá tajné čtyřciferné číslo, které bylo náhodně vygenerováno s unikátními číslicemi, které nezačínají nulou.

Po spuštění programu se zobrazí úvodní zpráva s pravidly hry. Hráč zadává své tipy na čtyřciferná čísla, které program vyhodnocuje na základě počtu bulls (správné číslo na správném místě) a cows (správné číslo na nesprávném místě). Program kontroluje platnost vstupu a informuje hráče, pokud je zadaný tip neplatný (např. obsahuje duplicity, začíná nulou nebo není čtyřciferný).

Po každém tipování se zobrazuje počet bulls a cows. Hráč pokračuje, dokud neuhádne tajné číslo. Jakmile hráč uhodne správné číslo, program vypíše počet pokusů a čas, který na to potřeboval. Hráč má možnost hrát znovu, a program zároveň uchovává statistiky o počtu odehraných her, průměrném počtu pokusů a průměrném čase.

Program obsahuje tyto klíčové části:

generování tajného čísla s unikátními číslicemi, které nezačíná nulou,

kontrola platnosti vstupu uživatele (ověření čtyřciferného čísla, bez duplicit a nuly na začátku),

vyhodnocení tipů uživatele na základě počtu bulls a cows,

zobrazení počtu pokusů a času po uhodnutí čísla,

uchovávání statistik o všech odehraných hrách, průměrném počtu pokusů a čase,

možnost opakování hry.

Hra je určena pro jednoho hráče, který hádá tajné číslo. Ovládání je plně realizováno pomocí konzole a vstupů z klávesnice.
