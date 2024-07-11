import rsa
from cryptography.fernet import Fernet

"""
Criptografia de chave simétrica:

Na criptografia de chave simétrica, os dados são codificados e decodificados com a mesma chave.
Esta é a maneira mais fácil de criptografar, mas também menos segura.
O receptor precisa da chave para descriptografar, portanto, uma maneira segura de transferir as chaves.
Qualquer pessoa com a chave pode ler os dados no meio.

"""

print("\n\nCRIPTOGRAFIA SIMÉTRICA\n")

mensagem = "MinhaSenha1234"

chave = Fernet.generate_key()


fernet = Fernet(chave)

msg_criptografada = fernet.encrypt(mensagem.encode())

print(f"MENSAGEM ORIGINAL: {mensagem}")
print(f"MENSAGEM ENCRIPTOGRAFADA: {msg_criptografada}")

msg_descriptografada = fernet.decrypt(msg_criptografada).decode()

print(f"MENSAGEM DESCRIPTOGRAFADA: {msg_descriptografada}")

########################################################################################


"""
Criptografia de chave assimétrica:

Na criptografia de chave assimétrica, usamos duas chaves, uma pública e outra privada.
A chave pública é usada para criptografar os dados e a chave privada é usada para descriptografar os dados.
Pelo nome, a chave pública pode ser pública (pode ser enviada para qualquer pessoa que precise enviar dados).
Ninguém tem sua chave privada, então ninguém do meio pode ler seus dados.

"""
print("\n\nCRIPTOGRAFIA ASSIMÉTRICA\n")

chave_publica, chave_privada = rsa.newkeys(512)
minha_mensagem = "E$saÉm!nhaS&nh4"

mensagem_encripitografada = rsa.encrypt(minha_mensagem.encode(), chave_publica)

print(f"MENSAGEM ORIGINAL: {minha_mensagem}")
print(f"MENSAGEM ENCRIPTOGRAFADA: {mensagem_encripitografada}")

mensagem_descriptografada = rsa.decrypt(mensagem_encripitografada, chave_privada).decode()

print(f"MENSAGEM DESCRIPTOGRAFADA: {mensagem_descriptografada}")
