
import requests
import time
import os
import sys

# RGB renkli yazı için ANSI escape kodu
def rgb_text(text, r, g, b):
    return f"\033[38;2;{r};{g};{b}m{text}\033[0m"

# Gökkuşağı efekti
def rainbow_text(text):
    result = ""
    colors = [
        (255, 0, 0),    # Kırmızı
        (255, 127, 0),  # Turuncu
        (255, 255, 0),  # Sarı
        (0, 255, 0),    # Yeşil
        (0, 0, 255),    # Mavi
        (75, 0, 130),   # Lacivert
        (148, 0, 211)   # Mor
    ]
    for i, char in enumerate(text):
        r, g, b = colors[i % len(colors)]
        result += rgb_text(char, r, g, b)
    return result

def clear(): os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    logo = r""" 
███████╗███████╗███████╗██╗     ███████╗
██╔════╝██╔════╝██╔════╝██║     ██╔════╝
███████╗█████╗  █████╗  ██║     █████╗  
╚════██║██╔══╝  ██╔══╝  ██║     ██╔══╝  
███████║███████╗██║     ███████╗███████╗
╚══════╝╚══════╝╚═╝     ╚══════╝╚══════╝
  ezel fake mail | Hacked by restwix ezel
"""
    print(rainbow_text(logo))

def generate_emails(prefix, count):
    domain = "1secmail.com"
    start = len([e for e in emails if e.startswith(prefix)])
    return [f"{prefix}{start + i + 1}@{domain}" for i in range(count)]

def check_inbox(email):
    login, domain = email.split('@')
    url = f"https://www.1secmail.com/api/v1/?action=getMessages&login={login}&domain={domain}"
    try:
        response = requests.get(url)
        messages = response.json()
        if not messages:
            print(rainbow_text(f"[{email}] Gelen kutusu boş."))
        else:
            print(rainbow_text(f"[{email}] Gelen kutusu:"))
            for msg in messages:
                print(rainbow_text(f" - ID: {msg['id']}, Kimden: {msg['from']}, Konu: {msg['subject']}"))
    except Exception as e:
        print(rainbow_text(f"[!] Hata: {e}"))

def rainbow_input(prompt):
    return input(rainbow_text(prompt))

def main():
    global emails
    prefix = "ezel"
    emails = []

    while True:
        clear()
        banner()
        print(rainbow_text("[1] Mail adreslerini göster"))
        print(rainbow_text("[2] Yeni mail oluştur"))
        print(rainbow_text("[3] Çıkış"))
        secim = rainbow_input("Seçiminiz: ")

        if secim == "1":
            if not emails:
                print(rainbow_text("Henüz mail yok. Önce oluşturmalısın."))
            else:
                for email in emails:
                    print(rainbow_text(f"\n[+] {email}"))
                    check_inbox(email)
            input(rainbow_text("\nDevam etmek için Enter'a bas..."))
        elif secim == "2":
            try:
                adet = int(rainbow_input("Kaç yeni mail oluşturulsun?: "))
                yeni_mailler = generate_emails(prefix, adet)
                emails.extend(yeni_mailler)
                print(rainbow_text(f"{adet} yeni mail oluşturuldu."))
            except:
                print(rainbow_text("Lütfen geçerli bir sayı gir."))
            input(rainbow_text("Devam etmek için Enter'a bas..."))
        elif secim == "3":
            print(rainbow_text("Çıkılıyor..."))
            break
        else:
            print(rainbow_text("Geçersiz seçim!"))
            time.sleep(1)

if __name__ == "__main__":
    main()
