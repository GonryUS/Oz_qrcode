
import wifi_qrcode_generator as qr
import streamlit as st
from tempfile import TemporaryFile
from PIL import Image
from io import BytesIO


with st.form(key='my_form'):

  st.title('OzFactor')
  st.header('Conecte seu Wi-FI apenas apontando o celular para o QR Code')
  st.subheader('Gere seu QR Code aqui!')

  SSID = st.text_input('Digite aqui o nome da rede Wi-FI')
  Senha = st.text_input('Digite aqui a senha da rede Wi-FI')
  aplicar = st.form_submit_button(label='Aplicar')

if aplicar:
  try:
    st.balloons()
    st.header('Bem vindo a rede {SSID}'.format(SSID=SSID))
    st.subheader('KEEP CALM')
    st.subheader('Aponte a câmera do celular no QR Code!')
    qr_image = qr.wifi_qrcode(SSID, False, 'WPA', Senha)
    buffer = BytesIO()
    qr_image.save(buffer, format='pdf')
    st.image(qr_image, caption="OzFactor by @OzBeto")
    st.download_button(label='Clique aqui para baixar', data=buffer.getvalue(), file_name="qr_code.pdf", mime="application/pdf")
  except RuntimeError as e:
    st.write(e)
