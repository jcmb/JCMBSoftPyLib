#! /usr/bin/env python3
"""Helper for creating HTML report files.

Takes an open text file, HTML_File, as a parameter.

Call output_html_header, then output_html_body.
For each table: output_table_header, output_table_row(...), output_table_footer.
Finish with output_html_footer with the list of table names to enable sorting
(tables omitted from that list are not made sortable).
"""

from html import escape
import json


def _attr(value):
   return escape(str(value), quote=True)


def _text(value):
   return escape(str(value), quote=False)


def output_table_header(HTML_File, Table_Name, Table_Caption, Columns, Width=100):
   table_id = _attr(Table_Name)
   if Width is None:
      HTML_File.write(
         '<table border="1" class="tablesorter" id="' + table_id + '">\n'
      )
   else:
      HTML_File.write(
         '<table border="1" class="tablesorter" id="'
         + table_id
         + '" width="'
         + _attr(Width)
         + '%">\n'
      )
   HTML_File.write('<caption><b>' + _text(Table_Caption) + '</b></caption>\n')
   HTML_File.write('<thead>\n')
   HTML_File.write('<tr>\n')
   for Column in Columns:
      HTML_File.write('<th>' + _text(Column) + '</th>\n')
   HTML_File.write('</tr>\n')
   HTML_File.write('</thead>\n')
   HTML_File.write('<tbody>')


def output_table_footer(HTML_File):
   HTML_File.write('</tbody>')
   HTML_File.write('</table>')


def output_table_row(HTML_File, Columns):
   HTML_File.write('<tr>\n')
   for Column in Columns:
      if isinstance(Column, bool):
         HTML_File.write('<td> True </td>\n' if Column else '<td> False </td>\n')
      elif isinstance(Column, str):
         if Column != '':
            HTML_File.write('<td>' + _text(Column) + '</td>\n')
         else:
            HTML_File.write('<td>&nbsp;</td>\n')
      else:
         HTML_File.write('<td>' + _text(Column) + '</td>\n')
   HTML_File.write('</tr>\n')


def output_html_header(HTML_File, Title, Refresh=None):
   """Title is the page title. Refresh is optional auto-refresh interval in seconds."""
   HTML_File.write('<!DOCTYPE HTML><meta charset="utf-8" /><html><head>\n')
   HTML_File.write(
"""
<script src="//ajax.googleapis.com/ajax/libs/jquery/3.7.0/jquery.min.js"></script>
<script src="/jquery.tablesorter.min.js"></script>
<script src="/jquery.tablesorter.widgets.min.js"></script>
<script src="/parser-date-iso8601.js"></script>


<link rel="stylesheet" type="text/css" href="/style.css">
<link rel="stylesheet" type="text/css" href="/css/theme.blue.css">
<link rel="stylesheet" type="text/css" href="/css/tcui-styles.css">
""")

   HTML_File.write('<title>' + _text(Title) + '</title>\n')
   if Refresh:
      HTML_File.write(
         '<meta http-equiv="refresh" content="' + _attr(Refresh) + '">'
      )

   HTML_File.write('</head>\n')


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
<div id="content-area">
<div id="content">
<div id="main-content">
""")


def output_html_footer(HTML_File, Tables):
   if Tables:
      HTML_File.write(
"""
<script>
$(document).ready(function()
{
""")
      for Table in Tables:
         HTML_File.write(
            '   $(document.getElementById('
            + json.dumps(str(Table))
            + ')).tablesorter({"theme": "blue"});\n'
         )
      HTML_File.write("""}
);
</script>
""")

   HTML_File.write('</div></div></div></body></html>')
