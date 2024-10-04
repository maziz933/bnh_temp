import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

st.set_page_config(
    page_title="Emplacement Agences",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Créer des colonnes pour centrer l'image
col1, col2, col3 = st.columns([1, 2, 3])

# Afficher l'image dans la colonne centrale
with col2:
    image = st.image("https://bnh.dz/img/logo13.png", width=400)

st.title("Déploiement des agences de BNH ")

options = ['choisir une année','2024', '2025', '2026']
optionn= ['aucun choix','directeur oui','directeur non']
# Créer une colonne pour afficher la carte à gauche
col1, col2 = st.columns([3, 2])
WILAYAS=['choisir une wilaya','ADRAR ', 'ALGER ', 'BOUIRA','BLIDA','MEDIA']

# Afficher la carte dans la colonne de gauche
with col1:
    # Créer une carte Folium
    m = folium.Map(location=[35.7950980697429, 3.1787263226179263], zoom_start=6)

    choice = st.selectbox('Choisir une option:', options)

    if st.button('Refresh'):
        st.write(f"Recherche en cours pour : {choice}")

    # Charger les données en fonction de l'option sélectionnée
    if choice == '2024':
        df = pd.read_excel(r'carte.graphique.xlsx')
    elif choice == '2025':
        df = pd.read_excel(r'carte.graphique2.xlsx')
    else:
        df = pd.read_excel(r'carte.graphique3.xlsx')

    # Ajouter des marqueurs jaunes à la carte Folium
    for index, row in df.iterrows():
        folium.CircleMarker([row['latitude'], row['longitude ']],
                            radius=10,
                            color='yellow',
                            fill=True,
                            fill_color='red').add_to(m)
        folium.Marker([row['latitude'], row['longitude ']],
                      popup=f"<b>Emplacement:</b> {row['name']}, <br><b>Latitude:</b> {row['latitude']}, <br><b>Longitude:</b> {row['longitude ']}").add_to(m)

    # Afficher le tableau dans la colonne de droite
    with col2:
        choix = st.selectbox('Choisir une option:', optionn)

        if choix == 'directeur non':
            if choice in ['2024']:
                df1 = pd.read_excel(r'C:\Users\user\Documents\carte.graphique.xlsx')
                df1_filtered = df1[df1.iloc[:, 3] == 'non']

                # Ajouter des marqueurs rouges à la carte Folium pour les lignes filtrées
                for index, row in df1_filtered.iterrows():
                    folium.CircleMarker([row['latitude'], row['longitude ']],
                                       radius=10,
                                       color='red',
                                       fill=True,
                                       fill_color='red').add_to(m)
                    folium.Marker([row['latitude'], row['longitude ']],
                                  popup=f"<b>Emplacement:</b> {row['name']}, <br><b>Latitude:</b> {row['latitude']}, <br><b>Longitude:</b> {row['longitude ']}").add_to(m)

                st.write("Colonne 3 du fichier 1:")
                st.write(df1_filtered.iloc[:,[0,3]])

        if choix == 'directeur non':
            if choice in ['2025']:
                df2 = pd.read_excel(r'C:\Users\user\Documents\carte.graphique2.xlsx')
                df2_filtered = df2[df2.iloc[:, 3] == 'non']

                # Ajouter des marqueurs rouges à la carte Folium pour les lignes filtrées
                for index, row in df2_filtered.iterrows():
                    folium.CircleMarker([row['latitude'], row['longitude ']],
                                       radius=10,
                                       color='red',
                                       fill=True,
                                       fill_color='red').add_to(m)
                    folium.Marker([row['latitude'], row['longitude ']],
                                  popup=f"<b>Emplacement:</b> {row['name']}, <br><b>Latitude:</b> {row['latitude']}, <br><b>Longitude:</b> {row['longitude ']}").add_to(m)

                st.write("Colonne 3 du fichier 2:")
                st.write(df2_filtered.iloc[:,[0,3]])
        if choix == 'directeur oui':
            if choice in ['2024']:
                df1 = pd.read_excel(r'C:\Users\user\Documents\carte.graphique.xlsx')
            
                df1_filtered = df1[df1.iloc[:, 3] == 'oui']
                df1_filtered = df1_filtered.sort_values(by = df1_filtered.columns[0] )
                
                # Ajouter des marqueurs vert à la carte Folium pour les lignes filtrées
                for index, row in df1_filtered.iterrows():
                    folium.CircleMarker([row['latitude'], row['longitude ']],
                                       radius=10,
                                       color='green',
                                       fill=True,
                                       fill_color='green').add_to(m)
                    folium.Marker([row['latitude'], row['longitude ']],
                                  popup=f"<b>Emplacement:</b> {row['name']}, <br><b>Latitude:</b> {row['latitude']}, <br><b>Longitude:</b> {row['longitude ']}").add_to(m)

                st.write("Colonne 3 du fichier 1:")
                st.write(df1_filtered.iloc[  :, [0,3]])
                
        if choix == 'directeur oui':
            if choice in ['2025']:
            
                df2 = pd.read_excel(r'C:\Users\user\Documents\carte.graphique2.xlsx')
            
                df2_filtered = df2[df2.iloc[:, 3] == 'oui']
                df2_filtered = df2_filtered.sort_values(by=df2_filtered.columns[0])  # Trier par la première colonne
            
                # Ajouter des marqueurs verts à la carte Folium pour les lignes filtrées
                for index, row in df2_filtered.iterrows():
                     folium.CircleMarker([row['latitude'], row['longitude ']],
                                       radius=10,
                                       color='green',
                                       fill=True,
                                       fill_color='green').add_to(m)
                     folium.Marker([row['latitude'], row['longitude ']],
                                  popup=f"<b>Emplacement:</b> {row['name']}, <br><b>Latitude:</b> {row['latitude']}, <br><b>Longitude:</b> {row['longitude ']}").add_to(m)

                st.write(df2_filtered.iloc[:,[0,3]])
    folium_static(m, width=600, height=300)

with col1:

    choisir = st.selectbox('choisir une wilaya', WILAYAS, key='wilaya_choice')

    if st.button('Refresh', key='wilaya_refresh'):
        st.write(f"Recherche en cours pour : {WILAYAS}")
    # Charger les données en fonction de l'option sélectionnée
    if choisir  == 'ALGER ':
        df = pd.read_excel(r'C:\Users\user\Documents\recapitulation.alger.xlsx')
        st.write(df)
        # Calculer le montant total des 6 premières lignes de la colonne 2
        total1 = df.iloc[:6, 2].sum()
        # Afficher le total dans une boîte
        st.write(f"Le taux D'AMENAGEMENTS  total  est : {total1:.4f}")
        total2 = df.iloc[6:, 2].sum()
        # Afficher le total dans une boîte
        st.write(f"Le taux EQUIPEMENTS  total  est : {total2:.4f}")
        total = total1 + total2
        st.write(f"Le taux   total  est : {total:.4f}")
        total_ht=df.iloc[:,1].sum()
        st.write(f"le total des MONTANT HT est :{total_ht:.4f}")
    else:
        st.write("Veuillez sélectionner une WILAYA pour afficher les données.")  
    if choisir  == 'ADRAR ':
        df = pd.read_excel(r'C:\Users\user\Documents\recapitulation.alger.xlsx', sheet_name='ADRAR')
        st.write(df)
        # Calculer le montant total des 6 premières lignes de la colonne 2
        total1 = df.iloc[:6, 2].sum()
        # Afficher le total dans une boîte
        st.write(f"Le taux D'AMENAGEMENTS  total  est : {total1:.4f}")
        total2 = df.iloc[6:, 2].sum()
        # Afficher le total dans une boîte
        st.write(f"Le taux EQUIPEMENTS  total  est : {total2:.4f}")
        total = total1 + total2
        st.write(f"Le taux   total  est : {total:.4f}")
        total_ht=df.iloc[:,1].sum()
        st.write(f"le total des MONTANT HT est :{total_ht:.4f}")
    #else:
        #st.write("Veuillez sélectionner une WILAYA pour afficher les données.")  
    if choisir  == 'BOUIRA':
        df = pd.read_excel(r'C:\Users\user\Documents\recapitulation.alger.xlsx', sheet_name='BOUIRA')
        st.write(df)
        # Calculer le montant total des 6 premières lignes de la colonne 2
        total1 = df.iloc[:6, 2].sum()
        # Afficher le total dans une boîte
        st.write(f"Le taux D'AMENAGEMENTS  total  est : {total1:.4f}")
        total2 = df.iloc[6:, 2].sum()
        # Afficher le total dans une boîte
        st.write(f"Le taux EQUIPEMENTS  total  est : {total2:.4f}")
        total = total1 + total2
        st.write(f"Le taux   total  est : {total:.4f}")
        total_ht=df.iloc[:,1].sum()
        st.write(f"le total des MONTANT HT est :{total_ht:.4f}")
    #else:
      #  st.write("Veuillez sélectionner une WILAYA pour afficher les données.")