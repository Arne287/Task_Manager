Dit project is een command line applicatie geschreven in Python waarmee taken beheerd kunnen worden.
De applicatie gebruikt een SQLite database om data op te slaan en laat de gebruiker toe om:
- Taken toe te voegen
- Taken te bekijken
- Taken als voltooid te markeren
- Een rapport te exporteren naar CSV

Dit project werd ontwikkeld als onderdeel van een programmeeropdracht en demonstreert het gebruik van:
- Python
- SQLite
- Git & GitHub
- Virtual environments
- Command line interactie


Projectstructuur:
task_manager/
├── app/
│   ├── __init__.py
│   ├── database.py
│   ├── models.py
│   └── cli.py
├── config/
│   └── settings_example.py
├── data/
├── main.py
├── README.md
├── requirements.txt
├── .gitignore

Voer de volgende stappen uit om deze opdracht te testen:

git clone https://github.com/Arne287/Task_Manager/tree/main.git

cd Task_Manager

Virtuele omgeving aanmaken:

python -m venv venv

venv\Scripts\Activate


Settings bestand aanmaken:

config/settings.py

Database toevoegen:

Maak een folder aan dat data heet en plaats daarin tasks.db

DATABASE_PATH = "data/tasks.db"



Een taak toevoegen:

python main.py --add "Mijn eerste taak"

python main.py --list

Voorbeeld Output:

1 - Mijn eerste taak [❌]


Taak markeren als voltooid:

python main.py --done 1


CSV rapport exporteren:

python main.py --export


Dit genereert een bestand zoals:

tasks_report.csv


