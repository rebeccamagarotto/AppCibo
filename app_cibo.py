import streamlit as st

# Titolo dell'app
st.title("Cosa Mangiare Oggi?")

# Domande per l'albero decisionale
hunger = st.radio("Hai fame?", ["Sì", "No"])
healthy = st.radio("Vuoi qualcosa di sano?", ["Sì", "No"])
hot = st.radio("Vuoi qualcosa di caldo?", ["Sì", "No"])

# Logica dell'albero decisionale
def suggerisci_cibo(hunger, healthy, hot):
    if hunger == "No":
        return "Non mangiare nulla, è meglio fare una pausa!"
    
    if healthy == "Sì" and hot == "Sì":
        return "Potresti provare una zuppa di verdure calda!"
    
    if healthy == "Sì" and hot == "No":
        return "Un'insalata fresca sarebbe perfetta!"
    
    if healthy == "No" and hot == "Sì":
        return "Una pizza margherita calda potrebbe fare al caso tuo!"
    
    if healthy == "No" and hot == "No":
        return "Un panino veloce potrebbe essere l'ideale!"
    
    return "Non sono sicuro, prova a cambiare qualche preferenza!"

# Bottone per ricevere il consiglio
if st.button("Consigliami! 🔍"):
    suggerimento = suggerisci_cibo(hunger, healthy, hot)
    st.write(f"Consiglio: {suggerimento}")

# Opzione per visualizzare l'albero decisionale
show_tree = st.checkbox("Mostra l'albero decisionale")
if show_tree:
    st.image("tree_decisionale.png")  # Sostituisci con il percorso corretto dell'immagine dell'albero decisionale

