from flask import Flask, render_template, request
from rsa_utils import fermat_factor, mod_inverse, decrypt_message

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/decrypt', methods=['POST'])
def decrypt():
    try:
        n = int(request.form['n'])
        e = int(request.form['e'])
        ciphertext = request.form['ciphertext']
        method = request.form['method']

        # Factorización y cálculo de d
        if method == "fermat":
            p, q = fermat_factor(n)
            
            
        # ACA SE DEBE PONER LA OPCIÓN DEL METODO TAMBIEN
        elif method == "trial_division":
            p, q = trial_division_factor(n)
        else:
            return render_template('index.html', error="Invalid decryption method selected.")

        phi_n = (p - 1) * (q - 1)
        d = mod_inverse(e, phi_n)

        # Descifrar el mensaje
        message = decrypt_message(ciphertext, d, n)
        
        return render_template('index.html', decrypted_message=message, p=p, q=q, d=d)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
