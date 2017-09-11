# CTI-110
# M2HW2_Tip Tax Total
# Airelle Hall
# 6 Sept 2017

# Tip, Tax and Total

foodcharge= float ( input ('Please enter the charge of food: ' ))

# Tip

tip = 0.18 * foodcharge 

# Tax

salestax= 0.07 * foodcharge

# Total

total=foodcharge +tip + salestax

print ('food charge: $' + format ( foodcharge, ',.2f' ))
'''
'tip: $' +\
        format (tip, ',.2f'), 'salestax: $' + format (salestax, ',.2f'), \
           'total: $' + format ( total, ',.2f' )'''
print ('tip: $' + format (tip, ',.2f'))

print ('salestax: $' + format (salestax, ',.2f'))

print ('total: $ ' + format (total, ',.2f'))



