# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 22:17:26 2026

@author: USER
"""

import streamlit as st
from datetime import datetime, timedelta

# --- AYARLAR ---
SON_REGL = "14/03/2026" # Burayı güncelleyebilirsin
DONGU = 20
# ---------------

st.set_page_config(page_title="Senin İçin", page_icon="🤍")
st.title("Merhabalar kainatın en güzel kadını 🤍")
st.subheader("Güzeller güzelim için yardımcı robot 🤍🥺")

baslangic_dt = datetime.strptime(SON_REGL, "%d/%m/%Y")
gelecek_tarih = baslangic_dt + timedelta(days=DONGU)
bugun = datetime.now()
kalan_gun = (gelecek_tarih - bugun).days

st.divider()

if kalan_gun > 0:
    st.metric(label="Bir sonraki tahmini tarihe", value=f"{kalan_gun} gün kaldı")
    st.info(f"Beklenen tarih: {gelecek_tarih.strftime('%d.%m.%Y')}")
elif kalan_gun == 0:
    st.warning("⚠️ Bugün başlaması bekleniyor!")
else:
    st.error(f"Beklenen tarih {abs(kalan_gun)} gün geçmiş.")

st.divider()
st.caption("Her zaman yanındayım. ❤️")