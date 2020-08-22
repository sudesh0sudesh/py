import xlrd


Workbook=xlrd.open_workbook("test.xlsx")
Worksheet_incident=Workbook.sheet_by_name("Incident")
Worksheet_analysis=Workbook.sheet_by_name("Analysis")
Worksheet_logs=Workbook.sheet_by_name("Logs")

print("[code]")
#Incident
print("<h4 'style=color:red;'>Incident details </h4></br>")
for i in range(0,Worksheet_incident.nrows-1):
    for y in range(0,Worksheet_incident.ncols):
        print("<strong>"+Worksheet_incident.cell_value(0,y)+": "+Worksheet_incident.cell_value(i+1,y)+"</strong></br>")
#Analysis
print("<h4 'style=color:red;'>Analysis</h4></br>")
for i in range(0,Worksheet_analysis.nrows):
    print(Worksheet_analysis.cell_value(i,0)+"</br>")

#LogLinks
print("<h4 'style=color:red;'>Logs</h4></br>")

for i in range(0,Worksheet_logs.nrows):
    print("<a href="+Worksheet_logs.cell_value(i,1)+" target=_blank>"+Worksheet_logs.cell_value(i,0)+"</a>")


print("[/code]")
