# dejvuv-jazyk-prk

**vymyslet jazyk** -> skupinové funkce  
**2x typy** -> integer, float  
**2x operace** -> celkový součin, suma  
**2x něco navíc** -> počet, obrácená hodnota

**správné výrazy:**  
+(1,2,5,5.2,5.3)  
\*(1,2,3)  
/(1,2,5)  
\~(1,2,3,7)  
+(+(1,2,3),+(1,2,4),\*(1,2))  
+(1)  
+(1,2,3.5,*(2,4),1,2,3)
+(+(1,2),~(5,4))
+(+(1,2,3),1,2,3)

**nesprávné výrazy:**  
+()  
*(1,(2))  
+(+(+(1,2)  
1,2,3  
(1,2,3)  
*(1,2~(3,4))  
