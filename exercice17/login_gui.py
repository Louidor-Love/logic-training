import tkinter as tk
from tkinter import messagebox

class LoginGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("OAuth Login")
        self.root.geometry("400x350")
        self.root.resizable(False, False)
        
        self.create_widgets()
        
    def create_widgets(self):
        # Título
        title = tk.Label(self.root, text="OAuth 2.0 Login", font=("Arial", 16, "bold"))
        title.pack(pady=20)
        
        # Frame para campos
        frame = tk.Frame(self.root)
        frame.pack(padx=20, pady=10)
        
        # Client ID
        tk.Label(frame, text="Client ID:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=5)
        self.client_id_entry = tk.Entry(frame, width=30, font=("Arial", 10))
        self.client_id_entry.insert(0, "client_123")
        self.client_id_entry.grid(row=0, column=1, pady=5)
        
        # Client Secret
        tk.Label(frame, text="Client Secret:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=5)
        self.client_secret_entry = tk.Entry(frame, width=30, font=("Arial", 10), show="*")
        self.client_secret_entry.insert(0, "secret_456")
        self.client_secret_entry.grid(row=1, column=1, pady=5)
        
        # Authorization Code
        tk.Label(frame, text="Auth Code:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=5)
        self.auth_code_entry = tk.Entry(frame, width=30, font=("Arial", 10))
        self.auth_code_entry.grid(row=2, column=1, pady=5)
        
        # Botones
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=20)
        
        tk.Button(button_frame, text="1. Authorize", command=self.on_authorize, 
                  width=12, font=("Arial", 9)).grid(row=0, column=0, padx=5)
        tk.Button(button_frame, text="2. Get Token", command=self.on_get_token, 
                  width=12, font=("Arial", 9)).grid(row=0, column=1, padx=5)
        tk.Button(button_frame, text="3. Protected", command=self.on_validate, 
                  width=12, font=("Arial", 9)).grid(row=0, column=2, padx=5)
        
        # Área de resultado
        tk.Label(self.root, text="Response:", font=("Arial", 10, "bold")).pack(anchor="w", padx=20)
        
        self.result_text = tk.Text(self.root, height=8, width=50, font=("Arial", 9))
        self.result_text.pack(padx=20, pady=5)
        self.result_text.config(state="disabled")
        
    def on_authorize(self):
        client_id = self.client_id_entry.get()
        if not client_id:
            self.show_result("Error: Client ID vacío")
            return
        
        auth_code = "auth_code_" + client_id[:5].upper()
        self.auth_code_entry.delete(0, tk.END)
        self.auth_code_entry.insert(0, auth_code)
        
        msg = f"✓ Authorize Success\nAuth Code: {auth_code}"
        self.show_result(msg)
        
    def on_get_token(self):
        client_id = self.client_id_entry.get()
        client_secret = self.client_secret_entry.get()
        auth_code = self.auth_code_entry.get()
        
        if not all([client_id, client_secret, auth_code]):
            self.show_result("Error: Completa todos los campos")
            return
        
        jwt = f"eyJhbGciOiJIUzI1NiJ9.{client_id[:5]}.signature"
        self.jwt_token = jwt
        
        msg = f"✓ Token Issued\n\nJWT:\n{jwt}\n\nExpires: 3600s"
        self.show_result(msg)
        
    def on_validate(self):
        if not hasattr(self, 'jwt_token'):
            self.show_result("Error: Obtén token primero")
            return
        
        msg = f"✓ Token Válido\n\nAcceso: GRANTED\nUser ID: user_123\nRoles: [admin, user]"
        self.show_result(msg)
        
    def show_result(self, message):
        self.result_text.config(state="normal")
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, message)
        self.result_text.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = LoginGUI(root)
    root.mainloop()
