# Semestrální práce

## Dejvův jazyk (definován za pomocí ANTLR a jazyka Python)
__skupinové funkce__

__4 operace:__    
\+ ... suma  
\/ ... převrácená hodnota  
\* ... celkový součin  
\~ ... počet operandů  

__2 datové typy:__  
integer  
float  

__příklad validních výrazů a jejich výsledek:__  
+(1,2) ... 1 + 2 = 3  
+(1.1,0.9) ... 1.1 + 0.9 = 2.0  
\/(1,2) ... 1 / (1 * 2) = 0.5  
\*(1,2) ... 1 * 2 = 2  
\~(1,2) ... count([1,2]) = 2  
\+(+(1,2),*(3,4)) ... (1 + 2) + (3 * 4) = 15  

__příklady nevalidních výrazů (generují error):__  
+()  
*(1,(2))  
+(+(+(1,2)  
1,2,3  
(1,2,3)  
*(1,2~(3,4))  
/(0)

## struktura adresáře
* __/parser__ (složka se soubory lexer + parser, automaticky generovány z dj.g4)
* __dj.g4__ (definice jazyka)  
* __djCalculator.py__ (soubor obsahující definici třídy DjCalculator - kalkulačka pracující s výrazy dejvova jazyka)  
* __djCalculatorTests.py__ (soubor obsahující testy třídy DjCalculator)
* __input.txt__ (soubor obsahující vstupní výrazy pro výpočet)
* __main.py__ (soubor pracující s DjCalculator, který zpracovává výrazy ze souboru input.txt a výsledky zapisuje do souboru output.txt)  
* __myDjVisitor.py__ (soubor s třídou MyDjVisitor, který prochází vygenerovaný strom a zpracovává vstupní výraz)
* __myErrorListener.py__ (soubor s třídou MyErrorListener, který obsahuje logiku generování erroru v případě chybného výrazu)  
* __output.txt__ (soubor obsahující výsledky vstupních výrazů ze souboru input.txt)



