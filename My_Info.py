import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.write("# <span style='color:black'>I'm Anbu</span>", unsafe_allow_html=True)
    st.image("images/photo.png", use_column_width=True)

with col2:
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write(" ")
    st.write("## <span style='color:navy'>About me</span>", unsafe_allow_html=True)

    content = """I'm a Motivated and innovative software professional dedicated to staying
current with emerging technologies. Eager to deliver creative solutions and drive
organizational growth through continuous learning and contribution

 I have hands-on experience in Java, Python, SQL, PL/SQL, Spring Boot, and HTML. I am keen to further explore and
 deepen my knowledge in these technologies through continuous learning and practice.
            """

    st.write(content)
    st.write("## <span style='color:navy'>Foundational Skills and Practical Experience</span>", unsafe_allow_html=True)
    st.write("I have gained foundational experience in the mentioned skills by certifications and self learning,"
             " and I am eager to further develop and apply them in practical settings."
             " Below, I provide examples showcasing my early experiences and projects.")

# space
st.write("")
st.write("")
st.write("")
st.write("")

# add python projects
st.markdown("<h1><u><b style='color: maroon;'>Python projects</b><u></h1>", unsafe_allow_html=True)
col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:3].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], use_column_width=True)
        st.write(f"[Click here]({row['url']})")
with col4:
    for index, row in df[3:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"], use_column_width=True)
        st.write(f"[Click here]({row['url']})")

# space
st.write("")
st.write("")
st.write("")
st.write("")

# add java projects
st.write("<b><u><h1><b style='color: maroon;'>Java projects<u></b></h1></b>", unsafe_allow_html=True)
col5, empty_col2, col6 = st.columns([1.5, 0.5, 1.5])
with col5:
    st.header("Quiz App")
    st.write("""This app is a Java-based platform utilizing PostgreSQL for quiz creation, interaction, and user 
    management.""")
    st.image("images/quiz-image.png", use_column_width=True)
    st.markdown("[Click here](https://github.com/Anbarasan-M/calculator)")
with col6:
    st.write("")

    st.header("Calculator App")
    st.write("""This app is a Java-based platform utilizing PostgreSQL for calculations""")
    st.image("images/calc-image.jpg", use_column_width=True)
    st.markdown("[Click here](https://github.com/Anbarasan-M/quizz-app)")


# add certifications
st.write("<b><u><h1><b style='color: maroon;'>Certifications</b></h1></u></b>", unsafe_allow_html=True)
credentials = pandas.read_csv("credentials.csv", sep=";")
for index, row in credentials.iterrows():
    st.markdown(f"<h3>{index + 1}. {row['course']} - {row['organisation']}</h3>", unsafe_allow_html=True)
    st.write(f"[Check the credential here]({row['url']})")

# resume
st.write("<b><u><h1><b style='color: maroon;'>Resume</b></h1></u></b>", unsafe_allow_html=True)
# st.image("images/anbarasan_resume.jpg", use_column_width=True)
st.markdown("[Click here to download the resume](https://drive.google.com/file/d/1kuYCa-0AJQJ1gRj_4coPRz5k_Iq_im_z/view?usp=sharing)")

# Applying CSS for rounded corners
st.write(
    """
    <style>
    img {
        border-radius: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
