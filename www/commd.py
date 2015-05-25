<%
from server.page import html, textStyle
from server.managers import sessionManager

html.initHTML(self)
html.beginHead(self)
html.setMetaUTF8(self)
%>

<script type="text/javascript">
 
function Redirect()
{
 window.back();
}
document.write("You will be redirected to a new page in 5 seconds");
//setTimeout('Redirect()', 5000);
window.history.back();
</script>
 
<%
html.endHead(self)
html.beginContent(self)




def write(cmd):
    try:
        import visa;
        rm = visa.ResourceManager("@py")
        inst = rm.open_resource("TCPIP::192.168.1.103")
        inst.write(cmd)
    except:
        print(u"Não encontrado")


login = __GET__['cmd'][0]
write(login)

html.endContent(self)
html.endHtml(self)
%>
