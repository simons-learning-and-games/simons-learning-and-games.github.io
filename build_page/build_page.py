import dominate
from dominate.tags import *
class img(html_tag):
    pass
    
# <div class="grid-container" style="grid-auto-flow: dense;">

#   <figure class="circle-image-box-with-caption">
#     <img class="wow rotateIn" src="./img/jake.jpeg" />
#     <figcaption>
#       <h5><a href="https://faculty.cc.gatech.edu/~jabernethy9/"> Jacob <br>Abernethy</a></h5>
#     </figcaption>
#   </figure>
#     <figure class="circle-image-box-with-caption">
#       <img class="wow rotateIn" src="./img/niao-he.jpg" />
#       <figcaption>
#         <h5><a href="https://odi.inf.ethz.ch/niaohe.html"> Niao<br>He</a></h5>
#       </figcaption>
#   </figure>

# </div>

speakers = [ {name:"Evangelos Papadopoulos", url:"foo.bar"}]
def confirmedSpeakers(speakers):

    with div(_class="grid-container", style="grid-auto-flow: dense;"):
        for speaker in speakers:
            with figure(_class="circle-image-box-with-caption"):
                with figcaption():
                    with h5():
                        a('<br>'.join(speaker.name.break()),  href=speaker.url)
