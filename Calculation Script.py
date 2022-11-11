#3 inputs from user: toxicity test, concentration, percent composition

# =============================================================================
# Fish LC50 
# Oral Rat LD50 
# Inhalation Rat LC50
# Dermal Rabbit LD50
# =============================================================================

# =============================================================================
# Tox X tcrm = 1
# Tox A tcrm = 10
# Tox B tcrm = 100
# Tox C tcrm = 1000
# Tox D tcrm = 10000
# =============================================================================


toxtest = input('Input number that correlates to correct toxicity test used for calculation: 1 = Fish LC50, 2 = Oral Rat LD50, 3 = Inhalation Rat LC50, 4 = Dermal Rabbit LD50: ')

t = float(toxtest)


# Fish LC50
if t == 1:
    conc = input('Concentration of Fish LC50 (mg/L): ')
    c = float(conc)
    if c < 0.01:
        tcrm = 1    
    elif c >= 0.01 or c < 0.1:
        tcrm = 10
    elif c >= 0.1 or c < 1:
        tcrm = 100
    elif c >= 1 or c < 10:
        tcrm = 1000
    elif c >= 10 or c <= 100:
        tcrm = 10000
        
    pcomp = input('Percent composition of the chemical in question for total solution (do not include % symbol): ')
    p = float(pcomp)
    
    ec = p/tcrm
        
    if ec >= 1:
         print('equalivalent concentration =', ec, 'EHW & WT01')
    elif ec >= 0.001:
         print('equalivalent concentration =', ec, 'DW & WT02')
    elif ec < 0.001:
         print('equalivalent concentration =', ec, 'not DW')  
    

# Oral Rat LD50
elif t == 2:
    conc = input('Concentration of Oral Rat LD50 (mg/L): ')
    c = float(conc)
    if c < 0.5:
        tcrm = 1
    elif c >= 0.5 or c < 5:
        tcrm = 10
    elif c >= 5 or c < 50:
        tcrm = 100
    elif c >= 50 or c < 500:
        tcrm = 1000
    elif c >= 500 or c <= 5000:
        tcrm = 10000
        
    pcomp = input('Percent composition of the chemical in question for total solution (do not include % symbol): ')
    p = float(pcomp)
    
    ec = p/tcrm
    
    if ec >= 1:
         print('equalivalent concentration =', ec, 'EHW & WT01')
    elif ec >= 0.001:
         print('equalivalent concentration =', ec, 'DW & WT02')
    elif ec < 0.001:
         print('equalivalent concentration =', ec, 'not DW')  
    
    

# Inhalation Rat LC50
elif t == 3:
    conc = input('Concentration of Inhalation Rat LC50 (mg/L): ')
    c = float(conc)
    if c < 0.02:
        tcrm = 1
    elif c >= 0.02 or c < 0.2:
        tcrm = 10
    elif c >= 0.2 or c < 2:
        tcrm = 100
    elif c >= 2 or c < 20:
        tcrm = 1000
    elif c >= 20 or c <= 200:
        tcrm = 10000
        
    pcomp = input('Percent composition of the chemical in question for total solution (do not include % symbol): ')
    p = float(pcomp)
    
    ec = p/tcrm
    
    if ec >= 1:
         print('equalivalent concentration =', ec, 'EHW & WT01')
    elif ec >= 0.001:
         print('equalivalent concentration =', ec, 'DW & WT02')
    elif ec < 0.001:
         print('equalivalent concentration =', ec, 'not DW')  
    
    

# Dermal Rabbit LD50    
elif t == 4:
    conc = input('Concentration of Dermal Rabbit LD50 (mg/kg): ')
    c = float(conc)
    if c < 2:
        tcrm = 1
    elif c >= 2 or c < 20:
        tcrm = 10
    elif c >= 20 or c < 200:
        tcrm = 100
    elif c >= 200 or c < 2000:
        tcrm = 1000
    elif c >= 2000 or c <= 20000:
        tcrm = 10000
        
    pcomp = input('Percent composition of the chemical in question for total solution (do not include % symbol): ')
    p = float(pcomp)
    
    ec = p/tcrm
    
    if ec >= 1:
         print('equalivalent concentration =', ec, 'EHW & WT01')
    elif ec >= 0.001:
         print('equalivalent concentration =', ec, 'DW & WT02')
    elif ec < 0.001:
         print('equalivalent concentration =', ec, 'not DW')  
    



















