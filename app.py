import streamlit as st
from PIL import Image


img = Image.open("LDP-156.jpg")
img2 = Image.open("LDP-200.jpg")
img3 = Image.open("LDP-263.jpg")
img4 = Image.open("LDP-637.jpg")
img5 = Image.open("Martha.jpg")
img6 = Image.open("Adri.jpg")
img7 = Image.open("Mario.jpg")
img8 = Image.open("Franco.jpg")
img9 = Image.open("Negro.jpg")

def home():
    st.markdown(f"<h1 style='color: #b5752f;'>Llanto de perro</h1>", unsafe_allow_html=True)
    #st.title("Llanto de perro")
    st.image(img, use_column_width=True)
    st.markdown(
    """<div style='color: #b5752f; font-size: 24px; font-style: italic; text-align: left;'>La obra nos permite adentrarnos en La Perdida, un paraje olvidado en la inmensidad del campo, donde los personajes juegan entre lo real y lo imaginado, entre lo fraternal y lo absurdo, entre sus propios códigos y el afuera. La visita de una encuestadora proveniente de la ciudad será el desencadenante de una serie de acontecimientos entre humorísticos y oscuros que se irán desarrollando a medida que estos dos mundos tan disímiles intentan conectarse.</div>""",
    unsafe_allow_html=True,
                )

def proximas_funciones():
    st.markdown(f"<h1 style='color: #b5752f;'>Próximas funciones</h1>", unsafe_allow_html=True)
    #st.write("Domingo, 07 de mayo de 2023")
    #st.write("Domingo, 14 de mayo de 2023")
    #st.write("Domingo, 21 de mayo de 2023")
    #st.write("Domingo, 28 de mayo de 2023")
    #st.write("Domingo, 04 de junio de 2023")
    #st.write("Domingo, 11 de junio de 2023")
    #st.write("Domingo, 18 de junio de 2023")
    #st.write("Domingo, 25 de junio de 2023")
    #st.markdown(f"""<div style='color: #b5752f; font-size: 18px;'>{chr(128054)} Domingo, 07 de mayo de 2023</div>""", unsafe_allow_html=True)
    #st.markdown(f"""<div style='color: #b5752f; font-size: 18px;'>{chr(128054)} Domingo, 14 de mayo de 2023</div>""", unsafe_allow_html=True)
    #st.markdown(f"""<div style='color: #b5752f; font-size: 18px;'>{chr(128054)} Domingo, 21 de mayo de 2023</div>""", unsafe_allow_html=True)
    #st.markdown(f"""<div style='color: #b5752f; font-size: 18px;'>{chr(128054)} Domingo, 28 de mayo de 2023</div>""", unsafe_allow_html=True)
    #st.markdown(f"""<div style='color: #b5752f; font-size: 18px;'>{chr(128054)} Domingo, 04 de junio de 2023</div>""", unsafe_allow_html=True)
    #st.markdown(f"""<div style='color: #b5752f; font-size: 18px;'>{chr(128054)} Domingo, 11 de junio de 2023</div>""", unsafe_allow_html=True)
    #st.markdown(f"""<div style='color: #b5752f; font-size: 18px;'>{chr(128054)} Domingo, 18 de junio de 2023</div>""", unsafe_allow_html=True)
    #st.markdown(f"""<div style='color: #b5752f; font-size: 18px;'>{chr(128054)} Domingo, 25 de junio de 2023</div>""", unsafe_allow_html=True)
    st.markdown(":dog: [Domingo, 07 de mayo de 2023](https://calendar.google.com/calendar/u/0/r/month/2023/5/7)", unsafe_allow_html=True)
    st.markdown(":dog: [Domingo, 14 de mayo de 2023](https://calendar.google.com/calendar/u/0/r/month/2023/5/14)", unsafe_allow_html=True)
    st.markdown(":dog: [Domingo, 21 de mayo de 2023](https://calendar.google.com/calendar/u/0/r/month/2023/5/21)", unsafe_allow_html=True)
    st.markdown(":dog: [Domingo, 28 de mayo de 2023](https://calendar.google.com/calendar/u/0/r/month/2023/5/28)", unsafe_allow_html=True)
    st.markdown(":dog: [Domingo, 04 de junio de 2023](https://calendar.google.com/calendar/u/0/r/month/2023/6/7)", unsafe_allow_html=True)
    st.markdown(":dog: [Domingo, 11 de junio de 2023](https://calendar.google.com/calendar/u/0/r/month/2023/6/11)", unsafe_allow_html=True)
    st.markdown(":dog: [Domingo, 18 de junio de 2023](https://calendar.google.com/calendar/u/0/r/month/2023/6/18)", unsafe_allow_html=True)
    st.markdown(":dog: [Domingo, 25 de junio de 2023](https://calendar.google.com/calendar/u/0/r/month/2023/6/25)", unsafe_allow_html=True)
    st.image(img2, use_column_width=True)
    st.markdown(":calendar: [¡Agregá el evento a tu calendario para no olvidarte!](https://calendar.google.com/calendar/u/0/r/month/2023/6/25)", unsafe_allow_html=True)


def contacto():
    #st.title("Contacto")
    st.markdown(f"<h1 style='color: #b5752f;'>Contacto</h1>", unsafe_allow_html=True)
    st.markdown(":point_right: [Instagram](https://www.instagram.com/llantodeperro/)") 
    st.markdown(":point_right: [Reservas en Whatsapp](https://wa.me/543482624626)", unsafe_allow_html=True)
    st.image(img3, use_column_width=True)

def prensa():
    #st.title("Contacto")
    st.markdown(f"<h1 style='color: #b5752f;'>Prensa</h1>", unsafe_allow_html=True)
    st.markdown(":point_right: [Mirá nuestra nota en el Diario La Capital](https://www.lacapital.com.ar/escenario/llanto-perro-continua-los-sabados-junio-sala-tandava-n10017493.html)") 
    st.image(img4, use_column_width=True)

def elenco():
    st.markdown(f"<h1 style='color: #b5752f;'>Elenco</h1>", unsafe_allow_html=True)
    st.markdown(f"<h2 style='color: #b5752f;'>Pere</h2>", unsafe_allow_html=True) 
    st.image(img5, use_column_width=True)
    st.markdown("Interpretado por Martha Chiappetta")
    st.markdown(f"<h2 style='color: #b5752f;'>La Señorita</h2>", unsafe_allow_html=True) 
    st.image(img6, use_column_width=True)
    st.markdown("Interpretado por Adriana Racca")
    st.markdown(f"<h2 style='color: #b5752f;'>Zuare</h2>", unsafe_allow_html=True) 
    st.image(img7, use_column_width=True)
    st.markdown("Interpretado por Mario Armas")
    st.markdown(f"<h2 style='color: #b5752f;'>Gome</h2>", unsafe_allow_html=True) 
    st.image(img8, use_column_width=True)
    st.markdown("Interpretado por Franco Ramseyer")
    st.markdown(f"<h2 style='color: #b5752f;'>Director</h2>", unsafe_allow_html=True) 
    st.image(img9, use_column_width=True)
    st.markdown("Dirección por Martín Gigena")

# Crear la barra de navegación
st.set_page_config(page_title="Llanto de perro", page_icon=":dog:")
menu = ["Inicio", "Próximas funciones", "Contacto", "Prensa", "Elenco"]
choice = st.sidebar.selectbox("Selecciona una opción", menu)


# Mostrar la página correspondiente según la opción elegida
if choice == "Inicio":
    home()
elif choice == "Próximas funciones":
    proximas_funciones()
elif choice == "Contacto":
    contacto()
elif choice == "Prensa":
    prensa()
else:
    elenco()
