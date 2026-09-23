import datetime
import random
import streamlit as st

# Naslov aplikacije
st.markdown(
    "<h1 style='text-align: center; color: #1f77b4;'>Pametna Analiza Utakmica</h1>",
    unsafe_allow_html=True,
)
st.write(
    "Dohvat parova s raznovrsnim i uravnoteženim preporukama (1, 2, 1X, X2)."
)

# Odabir datuma utakmica
odabrani_datum = st.date_input(
    "Izaberi datum utakmica", datetime.date.today()
)

# Gumb za pokretanje analize
if st.button("Pokreni analizu parova"):
  with st.spinner(f"Dohvaćam parove za datum: {odabrani_datum}..."):
    # Simulacija učitavanja / spajanja bez grešaka
    import time

    time.sleep(1.5)

  st.success("Analiza uspješno završena!")

  # Primjer generiranih parova i preporuka
  st.subheader(f"Preporučeni parovi za {odabrani_datum}")

  primjeri_parova = [
      {"utakmica": "Real Madrid - Barcelona", "tip": "1X", "koeficijent": "1.45"},
      {
          "utakmica": "Manchester City - Liverpool",
          "tip": "3+ gola",
          "koeficijent": "1.70",
      },
      {"utakmica": "Inter - Juventus", "tip": "1", "koeficijent": "2.10"},
      {"utakmica": "Bayern Munchen - Dortmund", "tip": "GG", "koeficijent": "1.55"},
      {"utakmica": "Milan - Napoli", "tip": "X2", "koeficijent": "1.60"},
  ]

  for p in primjeri_parova:
    st.info(
        f"**{p['utakmica']}** — Preporuka: **{p['tip']}** (Kvota: približno"
        f" {p['koeficijent']})"
    )
