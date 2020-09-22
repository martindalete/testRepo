import csv, datetime

RESoutput = 'Copy of Jodoin_RESPubs.csv'
REScsvFile = open('C:\\Users\\9ex\\Desktop\\python\\RIS\\' + RESoutput, 'r',
                  encoding = 'utf-8')
risfile = open('C:\\Users\\9ex\\Desktop\\python\\RIS\\' +
               str(datetime.date.today()) + '.ris', 'w', newline = '',
               encoding = 'utf-8')

RESDictReader = csv.DictReader(REScsvFile)

for line in RESDictReader:
    #print(line)
    if line['Communication Type'] == 'Journal':
        TY = 'JOUR' + '\n'
    elif line['Communication Type'] == 'Abstract':
        TY = 'UNPB' + '\n'
    elif line['Communication Type'] == 'ORNL Report':
        TY = 'RPRT' + '\n'
    elif line['Communication Type'] == 'Presentation':
        TY = 'UNPB' + '\n'
    elif line['Communication Type'] == 'Conference Paper':
        TY = 'CPAPER' + '\n'
    elif line['Communication Type'] == 'LDRD Report':
        TY = 'RPRT' + '\n'
    elif line['Communication Type'] == 'Other STI':
        TY = 'UNPB' + '\n'
    elif line['Communication Type'] == 'Book':
        TY = 'BOOK' + '\n'
    elif line['Communication Type'] == 'Book Chapter':
        TY = 'CHAP' + '\n'
    elif line['Communication Type'] == 'Thesis / Dissertation':
        TY = 'UNPB' + '\n'
    TI = line['Title'] + '\n'
    C1 = 'Report No.: ' + line['Report Number'] + '\n'
    try:
        ID = 'RES Pub ID: ' + line['\ufeffPub Id'] + '\n'
    except KeyError:
        ID = '\n'
    Authors = []
    Authors = line['Authors'].split(', ')
    AUlength = len(Authors)
    AU = 'AU  - '
    AUlist = []
    for i in range(AUlength):
        name_surname = Authors[i].split(" ")
        to_output = name_surname[-1] + ", " + name_surname[0]   
        AUi = AU + to_output
        AUlist.append(AUi)
        spam = ('\n').join(AUlist)

    T2 = line['Journal Name'] + '\n'
    AB = line['Abstract'] + '\n'
    VL = line['Volume'] + '\n'
    IS = line['Issue'] + '\n'
    SP = line['Page Start'] + '\n'
    EP = line['Page End'] + '\n'
    PY = line['Publication Year'] + '\n'
    DO = line['DOI'] + '\n'
    ER = '' + '\n\n'
    
    risfile.write('TY  - ' + TY +
                  'TI  - ' + TI +
                  str(spam) + '\n' +
                  'T2  - ' + T2 +
                  'AB  - ' + AB +
                  'VL  - ' + VL +
                  'IS  - ' + IS +
                  'SP  - ' + SP +
                  'EP  - ' + EP +
                  'PY  - ' + PY +
                  'DO  - ' + DO +
                  'C1  - ' + C1 +
                  'ID  - ' + ID + 
                  'ER  - ' + ER)

REScsvFile.close()
risfile.close()
