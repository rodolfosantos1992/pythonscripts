#Script que verifica STATUS do servico SEFAZ SP

import requests_pkcs12


url="https://nfe.fazenda.sp.gov.br/ws/nfestatusservico4.asmx"


body = """<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:nfes="http://www.portalfiscal.inf.br/nfe/wsdl/NFeStatusServico4">
   <soap:Header/>
   <soap:Body>
      <nfes:nfeDadosMsg>
<consStatServ xmlns="http://www.portalfiscal.inf.br/nfe" versao="4.00"><tpAmb>1</tpAmb><cUF>35</cUF><xServ>STATUS</xServ></consStatServ></nfes:nfeDadosMsg>
   </soap:Body>
</soap:Envelope>"""

tamanhobody = len(body)

headers = {'content-type': 'text/xml; charset=utf-8','Content-Length' : str(tamanhobody)}


#caminho absoluto ou relativo para certificado modelo PFX e senha do certificado
certificado = 'C:\\caminho\\do\\certificado.pfx'
senha = b'senhaaqui'


response = requests_pkcs12.post(url,data=body,headers=headers, pkcs12_filename=certificado, pkcs12_password=senha, verify=False)
print(response.content)
print(response.status_code)

