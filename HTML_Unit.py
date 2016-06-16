#! /usr/bin/env python

def output_table_header(HTML_File,Table_Name,Table_Caption,Columns,Width=100):
   HTML_File.write('<a name="'+Table_Name+'">\n')
   if Width==None:
      HTML_File.write('<TABLE BORDER=1 class="tablesorter" id="'+Table_Name+'">\n')
   else:
      HTML_File.write('<TABLE BORDER=1 class="tablesorter" id="'+Table_Name+'" width=' + str(Width) +'%>\n')
   HTML_File.write('<caption><b>' + Table_Caption+'</b></caption>\n')
   HTML_File.write('<thead>\n')
   HTML_File.write('<tr>\n')
   for Column in Columns:
      HTML_File.write('<th>'+Column+'</th>\n')
   HTML_File.write('</tr>\n')
   HTML_File.write('</thead>\n')
   HTML_File.write('<tbody>')


def output_table_footer(HTML_File):
   HTML_File.write('</tbody>')
   HTML_File.write('</table>')


def output_table_row(HTML_File,Columns):
   HTML_File.write('<tr>\n')
   for Column in Columns:
#      HTML_File.write('<td>'+str(Column)+'</td>\n')
#      print type(Column)
      if type(Column) is bool:
         if Column:
            HTML_File.write('<td> True </td>\n')
         else:
            HTML_File.write('<td> False </td>\n')
      elif isinstance(Column, basestring):
#         print "IS String"
         if Column != "":
#            print "IS not blank String"
            HTML_File.write('<td>'+Column.encode('utf-8')+'</td>\n')
         else:
            HTML_File.write('<td>&nbsp;</td>\n')
      else:
         HTML_File.write('<td>'+str(Column)+'</td>\n')
   HTML_File.write('</tr>\n')


def output_html_header(HTML_File,Title):
   HTML_File.write('<!DOCTYPE HTML><meta charset="utf-8" /><html><head>\n')
   HTML_File.write(
"""
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>
<script src="/jquery.tablesorter.min.js"></script>
<link rel="stylesheet" type="text/css" href="/style.css">
<link rel="stylesheet" type="text/css" href="/css/tcui-styles.css">
""")

   HTML_File.write("<title>"+Title+"</title>\n")
   HTML_File.write("</head>\n")

def output_html_body(HTML_File):
   HTML_File.write(
"""
<body class="page">
<div class="container clearfix">
  <div style="padding: 10px 10px 10px 0 ;"> <a href="/">
        <img src="/images/trimble-logo.jpg" alt="Trimble Logo" id="logo"> </a>
      </div>
  <!-- end #logo-area -->
</div>
<div id="top-header-trim"></div>
<div id="content-area">
<div id="content">
<div id="main-content">
""")

def output_html_footer(HTML_File,Tables):

   if Tables != []:
      HTML_File.write(
"""
<script>
$(document).ready(function()
{
""")
      for Table in Tables:
         HTML_File.write('   $("#'+ Table+ '").tablesorter();\n')
      HTML_File.write("""}
);
</script>
""")

   HTML_File.write("</body></html>")
