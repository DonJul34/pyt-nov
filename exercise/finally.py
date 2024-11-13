try:
    open_database_session()
    number = int(input("Entrez un nombre : "))
    result = 10 / number
    print(f"Résultat : {result}")
except ValueError:
    print("Veuillez entrer un nombre valide.")
except ZeroDivisionError:
    print("Impossible de diviser par zéro.")
except Exception as e:
    print(e)
finally:
    close_database_session()