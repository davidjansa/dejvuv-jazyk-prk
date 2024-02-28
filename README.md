# dejvuv-jazyk-prk

**vymyslet jazyk** -> skupinové funkce  
**2x typy** -> integer, float  
**2x operace** -> celkový součin, suma  
**2x něco navíc** -> počet, obrácená hodnota  

**příklady:**  
+(1,2,5,5.2,5.3) -> 23.5  
\*(1,2,3) -> 6  
/(1,2,5) -> 1/10 -> 0.1  
~(1,2,3,7) -> 4  
+(+(1,2,3),*(1,2,4)) -> +(6,8) -> 14  

<code>
integer ::= [1-9][0-9]* | "0"  
float ::= integer "." "0" | integer "." [0-9]*[1-9]  
operation ::= "+" | "*" | "~" | "/"  
value ::= integer | float  
values ::= value ("," value)*  
operands ::= "(" values ")"  
expression ::= operation operands | operation (expression)*
</code>


_nebo druhý návrh - udělat operace s vektory -> skalární součin... (datové typy int a vector)..._
