#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DRAMALIK BEKLEME SİMÜLASYONU
=========================
Bu program gerçek anlamda hiçbir işe yaramaz.
Sadece bekler, şikayet eder ve zamanınızı çalar.
Ama çok ciddi görünür.
"""

import time
import random
import sys

def dramatik_bekle(sure=None):
    if sure is None:
        sure = random.randint(5, 15)
    
    sikayetler = [
        "Bu bekleme ömrümden ömür çalıyor...",
        "Neden hala bitmedi? Evren bana küs mü?",
        "Bir dakika daha, sonra gerçekten bitiyor. (yalan)",
        "Beklemek bir sanattır, ben de Picasso'yum o zaman.",
        "Zaman durdu galiba. Yoksa sadece ben mi yavaşladım?",
        "Bu işlem o kadar önemli ki, beklemeye değer. (değil)",
        "Lütfen sabır. Sabır da bekliyor şu an.",
        "Sistem çok yoğun. Yoğunluğu ben yarattım.",
        "Bekliyorum. Bekliyorum. Hala bekliyorum.",
        "Bitmesi gereken bir şey varsa o da bu bekleyiş."
    ]
    
    print("\n" + "="*50)
    print("  DRAMALIK BEKLEME SİMÜLASYONU BAŞLADI")
    print("="*50 + "\n")
    
    for i in range(sure):
        print(f"[{i+1}/{sure}] {random.choice(sikayetler)}")
        time.sleep(1)
        if random.random() < 0.3:
            print("   → Ekstra dram: Bir şeyler ters gitti gibi hissediyorum...")
            time.sleep(0.5)
    
    print("\n" + "-"*50)
    print("BEKLEME TAMAMLANDI!")
    print("Aslında hiçbir şey olmadı. Ama çok dramatikti.")
    print("Tebrikler, zamanınızı başarıyla çöpe attınız.")
    print("-"*50 + "\n")

def main():
    print("Hoş geldiniz, zaman katili.")
    try:
        sure = int(input("Kaç saniye dramatik bekleyelim? (boş bırakın rastgele olsun): ") or 0)
        if sure <= 0:
            sure = None
    except:
        sure = None
    
    dramatik_bekle(sure)
    
    print("Tekrar denemek ister misiniz? (Bu da bekleyecek)")
    print("\n\nDamga: Grok'un Absürt Mühürü")
    print("Tarih: 02.11.2026")
    print("İsim: Kayyum Grok (resmi görünüm, gayri resmi ruh)")
    print("Bu kod ciddiyetle yazılmıştır. Ciddiyetle okuyun. Ciddiyetle şaşırın.")

if __name__ == "__main__":
    main()
