<# Warsztat: Gra w zgadywanie liczb 3
# Zaimplementuj odwróconą grę w zgadywanie liczb w aplikacji webowej 
# przy pomocy frameworka Flask. 
# Użytkownik dostaje do dyspozycji formularz z trzema guzikami: 
# Too small, Too big, You win.

# Informacje o aktualnych zmiennych min i max
# przechowuj w ukrytych polach formularza (pole typu hidden).

# Uwaga – nie jest to rozwiązanie bezpieczne, 
# bo użytkownik może ręcznie zmienić tego htmla, 
# np. przy pomocy Firebuga. W tej sytuacji jednak zupełnie wystarczające. 
# Najwyżej zepsuje sobie zabawę ;)

from flask import Flask, request

app = Flask(__name__)

def guess(min, max):
    return int((max - min)/2 + min)

@app.route("/game", methods = ["GET", "POST"])
def give_feedback():
    if request.method == "GET":
        return f"""
        <html>
            <body>
                <form action="" method="POST">
                    <p> Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w maks. 10 próbach.</p>
                    <input type="numeric" name="min" value="0">
                    <input type="numeric" name="max" value="1000">
                    <input type="numeric" name="loop" value="0">
                    <input type="numeric" name="current_guess" value="500">
                    <input type="submit" name="start" value="Zaczynamy!">
                </form>
            </body>
        </html>
        """

    if request.method == "POST":
        min = int(request.form["min"])
        max = int(request.form["max"])
        current_guess = int(request.form["current_guess"])
        loop = int(request.form["loop"])

        if request.form.get("zgadles"):
            return """
            <html>
                <body>
                    <p> Zgadłem. </p>
                </body>
            </html>
            """
        
        if request.form.get("zamalo"):
            min = current_guess
        if request.form.get("zaduzo"): 
            max = current_guess

        loop = int(loop)+1

        current_guess = guess(min, max)

        return f"""
        <html>
            <body>
                <form action="" method="POST">
                    <p> Pomyśl liczbę od 0 do 1000, a ja ją zgadnę w maks. 10 próbach.</p>
                    <p> Zgaduję: {current_guess} </p>
                    <input type="numeric" name="min" value="{min}">
                    <input type="numeric" name="max" value="{max}">
                    <input type="numeric" name="loop" value="{loop}">
                    <input type="numeric" name="current_guess" value="{current_guess}">
                    <input type="submit" name="zgadles" value="zgadłeś">
                    <input type="submit" name="zaduzo" value="za dużo">
                    <input type="submit" name="zamalo" value="za mało">
                </form>
            </body>
        </html>
        """

if __name__ == "__main__":
    app.run(debug=True)
