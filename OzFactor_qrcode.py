
import wifi_qrcode_generator as qr
import streamlit as st
import streamlit.components.v1 as components
from tempfile import TemporaryFile
from PIL import Image
from io import BytesIO

components.html(
"""
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
<script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
<div id="accordion">
   <div class="card">
      <div class="card-header" id="headingOne">
         <h5 class="mb-0">
            <button class="btn btn-link" data-toggle="collapse" data-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
               Collapsible Group Item #1
            </button>
         </h5>
      </div>
      <div id="collapseOne" class="collapse show" aria-labelledby="headingOne" data-parent="#accordion">
         <div class="card-body">
            Collapsible Group Item #1 content
         </div>
      </div>
   </div>
   <div class="card">
      <div class="card-header" id="headingTwo">
         <h5 class="mb-0">
            <button class="btn btn-link collapsed" data-toggle="collapse" data-target="#collapseTwo" aria-expanded="false" aria-controls="collapseTwo">
               Collapsible Group Item #2
            </button>
         </h5>
      </div>
      <div id="collapseTwo" class="collapse" aria-labelledby="headingTwo" data-parent="#accordion">
         <div class="card-body">
            Collapsible Group Item #2 content
         </div>
      </div>
   </div>
</div>
""",
height=600,
)
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
    st.header('WI-FI: {SSID}'.format(SSID=SSID))
    st.subheader('Para se conectar à rede, ligue a câmera do seu celular e aponte para a imagem abaixo:')
    qr_image = qr.wifi_qrcode(SSID, False, 'WPA', Senha)
    st.write('Aponte a câmera do celular no QR Code!')
    buffer = BytesIO()
    qr_image.save(buffer, format='pdf')
    st.image(qr_image, caption="WI-FI {SSID}. OzFactor by @OzBeto".format(SSID=SSID))
    st.download_button(label='Clique aqui para baixar', data=buffer.getvalue(), file_name="qr_code.pdf", mime="application/pdf")
  except RuntimeError as e:
    st.write(e)
