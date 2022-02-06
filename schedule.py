from datetime import date, timedelta
import datetime
import sys




today = date.today()


date_str = "08/02/22"
# date_str = input("Starting date in %d/%m/%y format:")
startdate = datetime.datetime.strptime(date_str, "%d/%m/%y")
date_str = "31/05/22"
# date_str = input("Finishing date in %d/%m/%y format:")

enddate = datetime.datetime.strptime(date_str, "%d/%m/%y")












placeholder =\
'''
\t\t\t<li>Session 1: <a href="https://www2.eecs.berkeley.edu/Faculty/Homepages/shenker.html">\n
\t\t\t\tScott Shenker</a> (UC Berkeley) - Why the Internet Architecture is almost perfect, but our core beliefs about it are entirely wrong</li><br>\n
\n
\t\t\t\t<button class="collapsible collapsible-abstract"></button>\n
\t\t\t\t<div class="content">\n
\t\t\t\t\t<p>\n
\t\t\t\t\tA very popular trick for solving certain types of optimization problems is this: write your objective as the solution of a two-player zero-sum game, endow both players with an appropriate learning algorithm, watch how the opponents compete, and extract an (approximate) solution from the actions/decisions taken by the players throughout the process. This approach is very generic and provides a natural template to produce new and interesting algorithms. I will describe this framework and show how it applies in several scenarios, and describe recent work drawing connections to classical algorithms including Frank-Wolfe, Nesterov Accelerated Gradient Descent, and many others.\n
\t\t\t\t\t</p>\n
\t\t\t\t</div>\n
\t\t\t\t\t\n
\t\t\t\t<button class="collapsible collapsible-bio"></button>\n
\t\t\t\t<div class="content">\n
\t\t\t\t\t<p>\n
\t\t\t\t\tJacob Abernethy is an Associate Professor in the College of Computing at Georgia Tech. In October 2011 he finished a PhD in the Division of Computer Science at the University of California at Berkeley, spent two years as a Simons postdoctoral fellow at UPenn, and held a faculty job at the University of Michigan for four years before joining Georgia Tech. Abernethy's primary interest is in Machine Learning, with a particular focus in sequential decision making, online learning, online algorithms and adversarial learning models\n
\t\t\t\t\t</p>\n
\t\t\t\t</div>\n
\t\t\t<li>Session 2: <a href="https://people.eecs.berkeley.edu/~jordan/">\n
\t\t\t\tMichael I. Jordan</a> (UC Berkeley) - Dr. AI: or How I Learned to Stop Worrying and Love Economics</p></li><br>
\n
\t\t\t\t<button class="collapsible collapsible-abstract"></button>\n
\t\t\t\t<div class="content">\n
\t\t\t\t\t<p>\n
\t\t\t\t\tA very popular trick for solving certain types of optimization problems is this: write your objective as the solution of a two-player zero-sum game, endow both players with an appropriate learning algorithm, watch how the opponents compete, and extract an (approximate) solution from the actions/decisions taken by the players throughout the process. This approach is very generic and provides a natural template to produce new and interesting algorithms. I will describe this framework and show how it applies in several scenarios, and describe recent work drawing connections to classical algorithms including Frank-Wolfe, Nesterov Accelerated Gradient Descent, and many others.\n
\t\t\t\t\t</p>\n
\t\t\t\t</div>\n
\t\t\t\t\t\n
\t\t\t\t<button class="collapsible collapsible-bio"></button>\n
\t\t\t\t<div class="content">\n
\t\t\t\t\t<p>\n
\t\t\t\t\tJacob Abernethy is an Associate Professor in the College of Computing at Georgia Tech. In October 2011 he finished a PhD in the Division of Computer Science at the University of California at Berkeley, spent two years as a Simons postdoctoral fellow at UPenn, and held a faculty job at the University of Michigan for four years before joining Georgia Tech. Abernethy's primary interest is in Machine Learning, with a particular focus in sequential decision making, online learning, online algorithms and adversarial learning models\n
\t\t\t\t\t</p>\n
\t\t\t\t</div><br>\n
\t\t\t<li>Session 3: <a href="https://www.cs.washington.edu/people/faculty/karlin">\n
\t\t\t\tAnna Karlin</a> (University of Washington) - An improved approximation for TSP in the half-integral case (and why Christos is my hero)</li><br>\n
\n
\t\t\t\t<button class="collapsible collapsible-abstract"></button>\n
\t\t\t\t<div class="content">\n
\t\t\t\t\t<p>\n
\t\t\t\t\tA very popular trick for solving certain types of optimization problems is this: write your objective as the solution of a two-player zero-sum game, endow both players with an appropriate learning algorithm, watch how the opponents compete, and extract an (approximate) solution from the actions/decisions taken by the players throughout the process. This approach is very generic and provides a natural template to produce new and interesting algorithms. I will describe this framework and show how it applies in several scenarios, and describe recent work drawing connections to classical algorithms including Frank-Wolfe, Nesterov Accelerated Gradient Descent, and many others.\n
\t\t\t\t\t</p>\n
\t\t\t\t</div>\n
\t\t\t\t\t\n
\t\t\t\t<button class="collapsible collapsible-bio"></button>\n
\t\t\t\t<div class="content">\n
\t\t\t\t\t<p>\n
\t\t\t\t\tJacob Abernethy is an Associate Professor in the College of Computing at Georgia Tech. In October 2011 he finished a PhD in the Division of Computer Science at the University of California at Berkeley, spent two years as a Simons postdoctoral fellow at UPenn, and held a faculty job at the University of Michigan for four years before joining Georgia Tech. Abernethy's primary interest is in Machine Learning, with a particular focus in sequential decision making, online learning, online algorithms and adversarial learning models\n
\t\t\t\t\t</p>\n
\t\t\t\t</div><br>\n
\t\t\t\t</ul>\n
\t\t</li>\n
'''

head=\
r'''
<head>
    <!-- add mathjax for tex support -->
<base target="_top">
<script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
<script>
  MathJax = {
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']]
    },
    svg: {
      fontCache: 'global'
    }
  };
  </script>
<script id="MathJax-script" async
        src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
</script>
<style>
.collapsible{
  display: flex;
  justify-content: center;
  cursor: pointer;
  /* padding: 18px;
  width: 75%; */
  border: none;
  width: 75%;
  margin: 0 auto;
  margin-left: auto;
  margin-right: auto;
  text-align: justify;
  text-justify: inter-word;
}
.collapsible-bio::before{
  font-weight: bold;
  content: "Short Bio";
}

.active, .collapsible-bio:hover {
  /* background-color: #555; */
}

.collapsible-bio:after {
  content: '\002B';
  /* color: white; */
  font-weight: bold;
  float: right;
  /* margin-left: 5px; */
}
/*  */
.collapsible-abstract::before{
  font-weight: bold;
  content: "Abstract";
}

.active, .collapsible-abstract:hover {
  /* background-color: #555; */
}

.collapsible-abstract:after {
  content: '\002B';
  /* color: white; */
  font-weight: bold;
  float: right;
  margin-left: 5px;
}
/*  */
.active:after {
  content: "\2212";
}

.content {
  /* padding: 0 18px; */
  max-height: 0;
  overflow: hidden;
  transition: max-height 0.2s ease-out;
  /* background-color: #f1f1f1; */
  border: none;
  width: 75%;
  margin: 0 auto;
  margin-left: auto;
  margin-right: auto;
  text-align: justify;
  text-justify: inter-word;
}
</style>
</head>

<body>
'''

fd = open("schedule.html", "w")
fd.write(head)
fd.write('<ul class="timeline list">\n')


date = startdate
idx = 0
while date <= enddate:
    string_date = date.strftime("%A %d %B, %Y")

    day = f'\t\t\t<li><span class="itemlabel"><span class="hbox llap">Day {idx+1}</span></span>\n\t\t\t<p><span class="bf"><span> {string_date}</p> Sessions:\n\t\t\t<ul style="list-style-type:disc;">\n\n'

    fd.write(day)
    fd.write(placeholder)

    date += timedelta(days=7)
    idx += 1

fd.write('\t</li>\n</ul>')

closing =\
r"""
<script>
var coll = document.getElementsByClassName("collapsible");
var i;

for (i = 0; i < coll.length; i++) {
  coll[i].addEventListener("click", function() {
    this.classList.toggle("active");
    var content = this.nextElementSibling;
    if (content.style.maxHeight){
      content.style.maxHeight = null;
    } else {
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
}
</script>
</body>
"""
fd.write(closing)
fd.close()