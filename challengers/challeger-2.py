aws_iam_response = {
    "account_alias": "my-company-prod",
    "users": [
        {"user_id": "admin_01", "status": "active", "settings": {"mfa_active": True, "cli_access": True}},
        {"user_id": "dev_02", "status": "inactive", "settings": {"mfa_active": False}},
        {"user_id": "dev_03", "status": "active"} 
    ]
}

#reescrever o código, se necessário, para facilitar entrar dentro do dicionário.
#criar uma variável que já nos coloca dentro de onde queremos ter esse acesso ao dicionário
#criar o loop baseado no que queremos, se atentando com o try e except

mfa_users = aws_iam_response["users"]

for mfa_user in mfa_users:
    if mfa_user["status"] == "activate":
        try: 
            mfa_status = mfa_user["active"] ["mfa_active"]
        except KeyError:
            mfa_status = False
        print(f"User {mfa_user['user_id']} has MFA: {mfa_status}")

