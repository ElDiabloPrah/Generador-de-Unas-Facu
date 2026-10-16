import streamlit as st

st.set_page_config(page_title="Diseñador de Uñas Pro", page_icon="💅", layout="centered")

st.title("💅 Diseñador de Uñas Pro")
st.write("Elige tus opciones en español. La app armará la instrucción perfecta en inglés para que las IAs de imágenes creen exactamente lo que imaginas.")

# Diccionarios de traducción
formas = {
    "Almendradas": "almond", 
    "Puntiagudas (Stiletto)": "stiletto", 
    "Ataúd (Coffin/Balerina)": "coffin", 
    "Cuadradas": "square", 
    "Ovaladas": "oval",
    "Naturales": "natural"
}

longitudes = {
    "Cortas": "short",
    "Medias": "medium length",
    "Largas": "long",
    "Extra largas (XL)": "extra long (XL)"
}

opacidades = {
    "Opaca (Sólida)": "solid opaque",
    "Translúcida (Efecto Jelly)": "translucent jelly",
    "Encapsulado (Transparente)": "clear transparent"
}

tonos_piel = {
    "Piel clara": "fair skin tone",
    "Piel media / trigueña": "medium olive skin tone",
    "Piel oscura": "dark brown skin tone",
    "Piel muy oscura": "deep dark skin tone"
}

colores = {
    "Nude / Piel": "nude",
    "Rosa pastel": "pastel pink",
    "Rojo cereza": "cherry red",
    "Negro": "black",
    "Blanco lechoso (Milky white)": "milky white",
    "Blanco puro": "pure white",
    "Verde neón": "neon green",
    "Azul cielo": "sky blue",
    "Lila / Lavanda": "lavender",
    "Marrón chocolate": "chocolate brown",
    "Plateado cromado": "chrome silver",
    "Dorado": "gold"
}

estilos = {
    "Color sólido": "solid color",
    "Francesa clásica": "classic French tip",
    "Francesa invertida": "reverse French",
    "Degradado / Ombré": "ombré gradient",
    "Mármol": "marble effect",
    "Aura (Centro difuminado)": "aura gradient"
}

acabados = {
    "Brillante (Glossy)": "glossy finish",
    "Mate": "matte finish",
    "Metálico": "metallic finish",
    "Holográfico / Tornasolado": "holographic finish",
    "Ojo de gato (Cat eye velvet)": "velvet cat eye polish"
}

apliques_3d = {
    "Ninguno": "no 3D elements",
    "Gotas de resina transparente": "3D clear resin drops",
    "Perlas": "pearl accents",
    "Diamantes de imitación (Strass)": "rhinestones",
    "Moños 3D": "3D bows",
    "Flores en relieve 3D": "3D sculpted acrylic flowers",
    "Aros metálicos / Piercings": "metal chains and nail piercings"
}

arte_mano = {
    "Ninguno": "no freehand art",
    "Líneas geométricas finas": "fine geometric lines",
    "Flores detalladas": "intricate floral patterns",
    "Llamas (Flames)": "painted flames",
    "Estrellas y destellos": "stars and sparkles",
    "Diseño abstracto": "abstract swirls"
}

fondos = {
    "Mármol blanco": "white marble",
    "Tela de seda suave": "soft silk fabric",
    "Fondo rosa pastel mate": "matte pastel pink",
    "Mesa limpia de salón de manicura": "clean salon table"
}

st.subheader("1. Estructura de la Uña")
col1, col2, col3 = st.columns(3)
with col1:
    forma_sel = st.selectbox("Forma", list(formas.keys()))
with col2:
    longitud_sel = st.selectbox("Longitud", list(longitudes.keys()))
with col3:
    opacidad_sel = st.selectbox("Opacidad base", list(opacidades.keys()))

st.subheader("2. Diseño y Colores")
col4, col5 = st.columns(2)
with col4:
    estilo_sel = st.selectbox("Estilo de diseño", list(estilos.keys()))
    color_base_sel = st.selectbox("Color Base", list(colores.keys()))
with col5:
    acabado_sel = st.selectbox("Acabado (Esmalte)", list(acabados.keys()))
    color_sec_sel = st.selectbox("Color Secundario", ["Ninguno"] + list(colores.keys()))

st.subheader("3. Arte, Texturas y Detalles")
col6, col7 = st.columns(2)
with col6:
    arte_sel = st.selectbox("Arte a mano alzada", list(arte_mano.keys()))
with col7:
    aplique_sel = st.selectbox("Apliques 3D o Joyería", list(apliques_3d.keys()))

st.subheader("4. Entorno de la Foto")
col8, col9 = st.columns(2)
with col8:
    tono_piel_sel = st.selectbox("Tono de piel de las manos", list(tonos_piel.keys()))
with col9:
    fondo_sel = st.selectbox("Fondo de la fotografía", list(fondos.keys()))

st.markdown("---")

# Botón generador
if st.button("✨ Generar Diseño", type="primary", use_container_width=True):
    # Traducir todo
    f_forma = formas[forma_sel]
    f_longitud = longitudes[longitud_sel]
    f_opacidad = opacidades[opacidad_sel]
    f_estilo = estilos[estilo_sel]
    f_cbase = colores[color_base_sel]
    f_acabado = acabados[acabado_sel]
    f_arte = arte_mano[arte_sel]
    f_aplique = apliques_3d[aplique_sel]
    f_tono = tonos_piel[tono_piel_sel]
    f_fondo = fondos[fondo_sel]
    
    # Combinar colores
    if color_sec_sel != "Ninguno":
        f_csec = colores[color_sec_sel]
        color_phrase = f"{f_cbase} and {f_csec} {f_estilo}"
    else:
        color_phrase = f"{f_cbase} {f_estilo}"
        
    # Sumar detalles
    details = []
    if f_arte != "no freehand art": details.append(f_arte)
    if f_aplique != "no 3D elements": details.append(f_aplique)
    
    if details:
        details_phrase = "decorated with " + " and ".join(details)
    else:
        details_phrase = "with a clean professional look"

    # Ensamblar el prompt final
    prompt = f"A photorealistic top-down view of two female hands with {f_tono} stretched outwards and laid flat on a {f_fondo} surface, showcasing detailed nail art. The nails are {f_longitud} length, {f_forma} shaped with a {f_opacidad} base. The design features a {f_acabado} {color_phrase}, {details_phrase}. Professional studio lighting, macro photography, crisp focus on the nails, highly detailed, 8k resolution, beauty editorial style."
    
    st.success("¡Aquí tienes tu prompt listo para copiar! (Toca el ícono en la esquina derecha del cuadro para copiar)")
    st.code(prompt, language="text")