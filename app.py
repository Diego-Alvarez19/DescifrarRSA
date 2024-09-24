from flask import Flask, render_template, request
from rsa_utils import fermat_factor, method_pollard, calc_d, decrypt_message, small_prime_factorization

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
            method_name = "Fermat's Factorization"
            
            
        # Factorización por método de pollard
        elif method == "pollard":
            p, q = method_pollard(n)
            method_name = "Pollard's Rho Method"

            #return render_template('index.html', error="Se seleccionó un método de descifrado no válido.")
        elif method == "small_prime":
            factors = small_prime_factorization(n)
            if len(factors) != 2:
                raise ValueError("No se pudo factorizar n en exactamente dos factores primos.")
            p, q = factors
            method_name = "Small Prime Factorization"

        phi_n = (p - 1) * (q - 1)
        d = calc_d(e, phi_n)

        # Descifrar el mensaje
        message = decrypt_message(ciphertext, d, n)
        
        return render_template('index.html', decrypted_message=message, p=p, q=q, d=d, method_name=method_name)
    except Exception as e:
        return render_template('index.html', error=str(e))

if __name__ == '__main__':
    app.run(debug=True)
