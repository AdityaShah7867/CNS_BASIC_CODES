import hmac
import hashlib
import tkinter as tk
from tkinter import ttk

def generate_hmac():
    secret_key = secret_key_entry.get()
    plaintext = plaintext_entry.get()

    secret_key_bytes = secret_key.encode('utf-8')
    hmac_sha256 = hmac.new(secret_key_bytes, plaintext.encode('utf-8'), hashlib.sha256)
    generated_hmac = hmac_sha256.digest()
    hex_hmac = generated_hmac.hex()

    result_label.config(text="Generated HMAC (in hexadecimal): " + hex_hmac)

window = tk.Tk()
window.title("HMAC Generator")

secret_key_label = ttk.Label(window , text="Secret Key:" )
secret_key_label.pack()
secret_key_entry = ttk.Entry(window)
secret_key_entry.pack()

plaintext_label = ttk.Label(window, text="Plaintext Message:")
plaintext_label.pack()
plaintext_entry = ttk.Entry(window)
plaintext_entry.pack()

generate_button = ttk.Button(window, text="Generate HMAC", command=generate_hmac)
generate_button.pack()

result_label = ttk.Label(window, text="")
result_label.pack()

window.mainloop()
