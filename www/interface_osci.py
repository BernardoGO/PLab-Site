<%
from server.page import html, textStyle
from server.managers import sessionManager

html.initHTML(self)
html.beginHead(self)

%>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js"></script>
    <script src="scripts.js" language="JavaScript"></script>

<%

html.setMetaUTF8(self)
html.endHead(self)
html.beginContent(self)
%>

<!--
    actScale = getScale()
    nextScale = ""
    backScale = ""
    strSca = str(actScale).split("." )[0]
    if strSca == "5":
        backScale = "1.0e"+str(int(str(actScale).split("e" )[1])+1)
        nextScale = "2."+str(actScale).split("." )[1]
    elif strSca == "2":
        backScale = "5."+str(actScale).split("." )[1]
        nextScale = "1."+str(actScale).split("." )[1]
    elif strSca == "1":
        backScale = "2."+str(actScale).split("." )[1]
        nextScale = "5.0e"+str(int(str(actScale).split("e" )[1])-1)


def getScale():
    return osci.main("q_:timebase:main:scale?")
def setScale(scale):
    osci.main(":timebase:main:scale " + scale)
    return redirect()

-->
<button type="button" onclick="point_it('autoscale')">AutoScale</button>
<button type="button" onclick="point_it('run')">RUN</button>
<button type="button" onclick="point_it('stop')">STOP</button>
<button type="button" onclick="point_it('apply:pulse')">GEN PULSE</button>
<button type="button" onclick="point_it('apply:RAMP')">GEN RAMP</button>
<button type="button" onclick="point_it('apply:NOISE')">GEN NOISE</button>
<br>
<button type="button" onclick="point_it(':timebase:main:scale 5.0e-2')">5.0e-2</button>
<button type="button" onclick="point_it(':timebase:main:scale 5.0e-3')">5.0e-3</button>
<button type="button" onclick="point_it(':timebase:main:scale 5.0e-4')">5.0e-4</button>
<button type="button" onclick="point_it(':timebase:main:scale 5.0e-5')">5.0e-5</button>
<button type="button" onclick="point_it(':timebase:main:scale 5.0e-6')">5.0e-6</button>
<button type="button" onclick="point_it(':timebase:main:scale 5.0e-7')">5.0e-7</button>
<button type="button" onclick="point_it(':timebase:main:scale 5.0e-8')">5.0e-8</button>
<button type="button" onclick="point_it(':timebase:main:scale 5.0e-9')">5.0e-9</button>
<button type="button" onclick="point_it(':timebase:main:scale 5.0e-10')">5.0e-10</button>



<%
html.endContent(self)
html.endHtml(self)
%>

