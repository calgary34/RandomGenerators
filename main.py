from flask import Flask, render_template,request
import random
app=Flask(__name__)
@app.route('/random/float/')
def randomfloat():
    return render_template("rfloat.html")
@app.route('/random/float/<low>/<high>/')
def randomfloat_param(low,high):
    return render_template("rfloat.html",low=low,high=high,rand=random.uniform(int(low), int(high)))
@app.route('/random/letter/')
def randomletter():
    letters=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    return render_template("rletter.html",rand=random.choice(letters))
@app.route('/')
def randompage():
    return render_template("random.html")
@app.route('/random/int/<low>/<high>/')
def randint_param(low,high):
    return render_template("randint.html",low=low,high=high,rand=random.randint(int(low), int(high)))
@app.route('/random/int/')
def randint_no_param():
    return render_template("randint.html")
@app.route('/random/letter/greek/')
def randomgreek():
    letters=["α (alpha)","β (beta)","γ (gamma)","δ (delta)","ε (epsilon)","ζ (zeta)","η (eta)","θ (theta)","ι (iota)","κ (kappa)","λ (lambda)","μ (mu)","ν (nu)","ξ (xi)","ο (omicron)","π (pi)","ρ (rho)","σ (sigma)","τ (tau)","υ (upsilon)","φ (phi)","χ (chi)","ψ (psi)","ω (omega)"]
    return render_template("rgreek.html",rand=random.choice(letters))
@app.route('/random/letter/upper/')
def eng_upper():
    letters=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","X"]
    return render_template("rletterupper.html",rand=random.choice(letters))
@app.route('/random/letter/russian/')
def randomrussian():
    letters=["б", "в", "г", "д", "ж", "з", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ","а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я",'й']
    return render_template("rrussian.html",rand=random.choice(letters))
if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		host='0.0.0.0',  # Establishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
	)