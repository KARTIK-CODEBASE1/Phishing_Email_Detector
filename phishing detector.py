# phishing_detector.py

keywords = ["urgent", "verify", "login", "password", "bank", "click here" , "click this link" , "download this .exe file" , "download this file"]
email_text = input("Paste email text here:\n").lower()

found = [word for word in keywords if word in email_text]

if found:
    print("⚠️ Warning: Possible phishing keywords found:", ", ".join(found))
else:
    print("✅ No suspicious keywords detected.")
