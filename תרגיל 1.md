
## שאלה 3

$$
\phi_{1}= (a \land \lnot c) \lor (f\to (h \lor \lnot a))
$$
$$
\phi_{2}= (a\land f) \lor \left(\lnot a \to (b\land g)\right)
$$
$$
\phi = \phi_{1} \leftrightarrow  \phi_{2}
$$
#### סעיף א
 נוסחא A שמסתפקת ביחד עם $\phi$ לפי אלגוריתם של צייטן.
נתחיל מחיפוש כל תתי-נוסחאות של $\phi$
$$
subform(\phi_{1})= \{\phi_{1}, (a\land \lnot c), a, \lnot c ,c, (f\to (h\lor \lnot a)), f, (h\lor \lnot a), h, \lnot a \}
$$
$$
subbofm(\phi_{2}) = \{ \phi_{2}, (a\land f), a, f, (\lnot a \to (b\land g)), \lnot a, (b\land g), b, g\}
$$
$$
\displaylines{subform(\phi) = \{\phi\} \cup subform(\phi_{1})\cup subform(\phi_{2})= \\ \\ = \{\phi, \phi_{1}, (a\land \lnot c), a, \lnot c ,c, (f\to (h\lor \lnot a)), f, (h\lor \lnot a), h, \lnot a ,\\ \phi_{2}, (a\land f), (\lnot a \to (b\land g)), (b\land g), b, g\}}
$$

עכשיו כל משתנים חדשים עבור תת-נוסחה $\psi$ נגדיר $P_{\psi}$.
נתחיל להרכיב את הנוסחא אלגוריתם של צייטן.
$\phi= \phi_{1}\leftrightarrow \phi_{2}$
Var: $P_{\phi}, P_{\phi_{1}},P_{\phi_{1}}$

$$\displaylines{CNF(\phi \leftrightarrow  P_{\phi}) =\\
(\lnot P_{\phi} \lor P_{\phi_{1}} \lor P_{\phi_{2}}) \land \\
 (\lnot P_{\phi} \lor P_{\phi_{1}} \lor \lnot P_{\phi_{2}}) \land \\
( P_{\phi} \lor \lnot P_{\phi_{1}} \lor \lnot P_{\phi_{2}}) \land \\
( P_{\phi} \lor P_{\phi_{1}} \lor P_{\phi_{2}})
}$$

$\phi_{1}= (a \land \lnot c) \lor (f\to (h \lor \lnot a))$
Var: $P_{\phi_{1}}, P_{(a \land \lnot c)}, P_{(f\to (h \lor \lnot a))}$
$$
\displaylines{CNF(\phi_{1} \leftrightarrow P_{\phi_{1}}) = \\
( \lnot P_{\phi_{1}}\lor P_{(a \land \lnot c)}\lor P_{(f\to (h \lor \lnot a))})\land \\
( \lnot P_{(a \land \lnot c)}\lor P_{(f\to (h \lor \lnot a))}) \land \\
( P_{(a \land \lnot c)}\lor \lnot P_{(f\to (h \lor \lnot a))})
}
$$


$a \land \lnot c$
Var: $P_{a \land \lnot c},P_{a}, P_{\lnot c}$
$$
\displaylines{CNF((a \land \lnot c ) \leftrightarrow P_{a \land \lnot c}) = \\
(P_{a \land \lnot c}\lor \lnot P_{a}\lor \lnot P_{\lnot c}) \land \\
(\lnot P_{a \land \lnot c}\lor P_{a}) \land \\
(\lnot P_{a \land \lnot c}\lor P_{\lnot c})
}
$$


$a$
$$CNF(a\leftrightarrow P_{a})=(\lnot P_{a}\lor a)\land (\lnot a \lor P_{a})$$

$\lnot c$
Var:$P_{\lnot c},P_c$
$$
CNF(\lnot c \leftrightarrow  P_{\lnot c}) = (P_{\lnot c}\lor P_{c})\land (\lnot P_{\lnot c}\lor \lnot P_{c})
$$

$c$
$$
CNF(c\leftrightarrow P_{c})=(\lnot P_{c}\lor c)\land (\lnot c \lor P_{c})
$$



$f\to (h \lor \lnot a)$
Var: $P_{f\to (h \lor \lnot a)},P_{f},P_{h \lor \lnot a}$
$$
\displaylines{
CNF((f\to (h \lor \lnot a)) \leftrightarrow  P_{f\to (h \lor \lnot a)}) = \\ 
(\lnot P_{f\to (h \lor \lnot a)}\lor \lnot P_{f}\lor P_{h \lor \lnot a})\land \\
(P_{f\to (h \lor \lnot a)}\lor P_{f})\land \\
(P_{f\to (h \lor \lnot a)}\lor \lnot P_{h \lor \lnot a})
}
$$

$f$
$$
CNF(f\leftrightarrow P_{f})=(\lnot P_{f}\lor f)\land (\lnot f \lor P_{f})
$$

$h \lor \lnot a$
Var: $P_{h \lor \lnot a},P_{h}, P_{\lnot a}$
$$
\displaylines{
CNF(h \lor \lnot a \leftrightarrow  P_{h \lor \lnot a})=\\
(\lnot P_{h \lor \lnot a}\lor P_{h}\lor  P_{\lnot a})\land \\
(P_{h \lor \lnot a} \lor \lnot P_{h})\land \\
(P_{h \lor \lnot a}\lor \lnot P_{\lnot a})
}
$$

$h$
$$
CNF(h\leftrightarrow P_{h})=(\lnot P_{h}\lor h)\land (\lnot h \lor P_{h})
$$




$\lnot a$
Var:$P_{\lnot a},P_{a}$
$$
CNF(\lnot a \leftrightarrow  P_{\lnot a}) = (P_{\lnot a}\lor P_{a})\land (\lnot P_{\lnot a}\lor \lnot P_{a})
$$

סיימנו עם $\phi_{1}$


$\phi_{2}= (a\land f) \lor \left(\lnot a \to (b\land g)\right)$
Var: $P_{\phi_{2}}, P_{(a\land f)},P_{\left(\lnot a \to (b\land g)\right)}$
$$
\displaylines{
CNF(\phi_{2}\leftrightarrow P_{\phi_{2}})= \\
(\lnot P_{\phi_{2}}\lor P_{(a\land f)}\lor P_{\left(\lnot a \to (b\land g)\right)})\land \\
(\lnot P_{(a\land f)}\lor P_{\left(\lnot a \to (b\land g)\right)})\land \\
(P_{(a\land f)}\lor \lnot P_{\left(\lnot a \to (b\land g)\right)})

}
$$

$a\land f$
Var: $P_{a\land f}, P_{a},P_{f}$
$$\displaylines{
CNF((a\land f) \leftrightarrow  P_{a\land f}) = \\
(P_{a\land f}\lor \lnot  P_{a}\lor \lnot P_{f})\land \\
(\lnot P_{a\land f} \lor P_{a})\land \\
(\lnot P_{a\land f}\lor P_{f})
}$$

$\lnot a \to (b\land g)$
Var: $P_{\lnot a \to (b\land g)},P_{\lnot a}, P_{b\land g}$
$$
\displaylines{
CNF((\lnot a \to (b\land g))\leftrightarrow P_{\lnot a \to (b\land g)}) = \\
(\lnot P_{\lnot a \to (b\land g)}\lor \lnot P_{\lnot a}\lor  P_{b\land g})\land \\
(P_{\lnot a \to (b\land g)}\lor P_{\lnot a})\land \\
(P_{\lnot a \to (b\land g)}\lor \lnot P_{b\land g})
}
$$

$(b\land g)$
Var: $P_{(b\land g)},P_{b},P_{g}$
$$\displaylines{
CNF((b\land g)\leftrightarrow P_{(b\land g)}) = \\
(P_{(b\land g)}\lor \lnot P_{b}\lor \lnot P_{g}) \land \\
(\lnot P_{(b\land g)}\lor P_{b}) \land \\
(\lnot P_{(b\land g)}\lor P_{g})
}$$


$b$
$$CNF(b\leftrightarrow P_{b})=(\lnot P_{b}\lor b)\land (\lnot b \lor P_{b})$$

$g$
$$CNF(g\leftrightarrow P_{g})=(\lnot P_{g}\lor g)\land (\lnot g \lor P_{g})$$

סיימנו.
עכשיו נחבר הכל לנוסחא אחת.

מכאן מה שנשאר זה רק לחבר הכל לפי הנוסחא של צייטן.

$$
P_{\phi} \land \bigwedge_{C\in subform(\phi)} CNF(C\leftrightarrow P_{C})
$$

מכאן 
$$
\displaylines{
P_{\phi}\land\\
(\lnot P_{\phi} \lor P_{\phi_{1}} \lor P_{\phi_{2}}) \land \\
 (\lnot P_{\phi} \lor P_{\phi_{1}} \lor \lnot P_{\phi_{2}}) \land \\
( P_{\phi} \lor \lnot P_{\phi_{1}} \lor \lnot P_{\phi_{2}}) \land \\
( P_{\phi} \lor P_{\phi_{1}} \lor P_{\phi_{2}})\land \\
( \lnot P_{\phi_{1}}\lor P_{(a \land \lnot c)}\lor P_{(f\to (h \lor \lnot a))})\land \\
( \lnot P_{(a \land \lnot c)}\lor P_{(f\to (h \lor \lnot a))}) \land \\
( P_{(a \land \lnot c)}\lor \lnot P_{(f\to (h \lor \lnot a))})\land\\
(P_{a \land \lnot c}\lor \lnot P_{a}\lor \lnot P_{\lnot c}) \land \\
(\lnot P_{a \land \lnot c}\lor P_{a}) \land \\
(\lnot P_{a \land \lnot c}\lor P_{\lnot c})\land \\
(\lnot P_{a}\lor a)\land (\lnot a \lor P_{a})\land\\
(P_{\lnot c}\lor P_{c})\land (\lnot P_{\lnot c}\lor \lnot P_{c})\land \\
(\lnot P_{c}\lor c)\land (\lnot c \lor P_{c})\land \\
(\lnot P_{f\to (h \lor \lnot a)}\lor \lnot P_{f}\lor P_{h \lor \lnot a})\land \\
(P_{f\to (h \lor \lnot a)}\lor P_{f})\land \\
(P_{f\to (h \lor \lnot a)}\lor \lnot P_{h \lor \lnot a})\land \\
(\lnot P_{f}\lor f)\land (\lnot f \lor P_{f})\land \\
(\lnot P_{h \lor \lnot a}\lor P_{h}\lor  P_{\lnot a})\land \\
(P_{h \lor \lnot a} \lor \lnot P_{h})\land \\
(P_{h \lor \lnot a}\lor \lnot P_{\lnot a})\land \\
(\lnot P_{h}\lor h)\land (\lnot h \lor P_{h})\land \\
(P_{\lnot a}\lor P_{a})\land (\lnot P_{\lnot a}\lor \lnot P_{a})\land \\
(\lnot P_{\phi_{2}}\lor P_{(a\land f)}\lor P_{\left(\lnot a \to (b\land g)\right)})\land \\
(\lnot P_{(a\land f)}\lor P_{\left(\lnot a \to (b\land g)\right)})\land \\
(P_{(a\land f)}\lor \lnot P_{\left(\lnot a \to (b\land g)\right)})\land \\
(P_{a\land f}\lor \lnot  P_{a}\lor \lnot P_{f})\land \\
(\lnot P_{a\land f} \lor P_{a})\land \\
(\lnot P_{a\land f}\lor P_{f})\land \\
(\lnot P_{\lnot a \to (b\land g)}\lor \lnot P_{\lnot a}\lor  P_{b\land g})\land \\
(P_{\lnot a \to (b\land g)}\lor P_{\lnot a})\land \\
(P_{\lnot a \to (b\land g)}\lor \lnot P_{b\land g})\land \\
(P_{(b\land g)}\lor \lnot P_{b}\lor \lnot P_{g}) \land \\
(\lnot P_{(b\land g)}\lor P_{b}) \land \\
(\lnot P_{(b\land g)}\lor P_{g})\land \\
(\lnot P_{b}\lor b)\land (\lnot b \lor P_{b})\land \\
(\lnot P_{g}\lor g)\land (\lnot g \lor P_{g})
}
$$



#### סעיף ב
אנחנו ניזכר בזה שאופרטורים בינארים מאותו סוג מקיימים קומוטטיביות ואסוציאטיביות. כלומר
$$\displaylines{
(A \land B ) = (B\land A)\\
(A \land B) \land C = (A\land B\land C) = A \land (B\land C)
}$$
ואותו דבר עבור אופרטור or לוגי. אנחנו נשתמש בזה בהמשך לצורך לפשט טיפה את הביטוי ולסדר אותו.

כללי שנתשמש בהם:

$$
\displaylines{
A\lor (B\land C) = (A\lor B)\land (A\lor C)\\
 (B\land C)\lor  A = (A\lor B)\land (A\lor C)
}
 \tag{1}
$$

$$
\displaylines{
A\land (B\lor C) = (A\land B)\lor (A\land C)\\
 (B\lor C)\land  A = (A\land B)\lor (A\land C)
}
 \tag{2}
$$
רק בשביל להקל עלינו בכתיבה אנחנו נשתמש לפעמים גירסה מורכבת של ביטויים מסוג (1) ו-(2). כלומר
$$
\displaylines{A \lor (B_{1}\land ...\land B_{n}) = (A\lor B_{1})\land...\land  (A\lor B_{n})\\
(B_{1}\land ...\land B_{n})\lor A   = (A\lor B_{1})\land...\land  (A\lor B_{n})}
$$
$$
\displaylines{A \land (B_{1}\lor ...\lor B_{n}) = (A\land B_{1})\lor...\lor  (A\land B_{n})\\
(B_{1}\lor ...\lor B_{n})\land A   = (A\land B_{1})\lor...\lor  (A\land B_{n})}
$$
ואנחנו עדיין בהערות נפנה לזה כביטוי (1) ו(2) לצורך הפשטות.
הנימוק לשימוש בזה ראינו בקורס בדידה 1 ע"י הוכחת באינדוקציה אבל נמציין את זה כאן בצורה מקוצרת. נראה עבור ביוי (1) ועבור ביטוי שני הוכחה דומה.
מקרה בסיס זה הביטוי (1) המקורי ונתון שזה מתקיים. נניח שזה מתקיים עבור 
$A \lor (B_{1}\land ...\land B_{n}) = (A\lor B_{1})\land...\land  (A\lor B_{n})$
ונראה שזה מתקיים עבור 
$$\displaylines{A \lor (B_{1}\land ...\land B_{n+1 }) = A \lor ((B_{1}\land ...B_{n})\land B_{n+1})=\\
= (A \lor (B_{1}\land ...\land B_{n}) \land (A \land B_{n+1}))=\\
= (A\lor B_{1})\land...\land  (A\lor B_{n})\land (A \lor B_{n+1})
}
$$
כאשר הביטוי המעבר ראשון נובע מאסוציאטיביות של אופרטורים בינארים באותו סוג , מעבר שני זה מקרה הבסיס ומעבר אחרון אנחת האינסדוקציה. מ.ש.ל. 
עבור כיוון שני הוכחה כמע זהה, כפי שנאמר עבור מקרה השני זה ממש דומה וצריך רק להחליף אופרטורים.



$$
A \to B \equiv \lnot A \lor B \tag{3}
$$


$$
\displaylines{\lnot(A\lor B) \equiv (\lnot A \land \lnot B)\\
\lnot (A\land B)\equiv (\lnot A \lor \lnot B)}\tag{4}
$$

$$
\lnot \lnot A \equiv A \tag {5}
$$

$$
A\leftrightarrow B \equiv (\lnot A \lor B) \land (\lnot B \lor A) \tag{6}
$$
כל מה שלעיל היה נתון כחלק מהתרגיל ונוסיף עוד מספר כללים שיאפשרו לנו לפשט את הביטוי.


נוכיח עוד כמה דברים קטנים רק בשביל להקל על כתיבת ביטוי.
**למה** (7)
$$\displaylines{a\land \lnot a =False \\
a\lor \lnot a=True
}\tag{7}$$
**הוכחה**:
שקילות ראשונה:
עבור $a=T$ נקבל $T\land F=F$ ואותה תוצאה תתקבל עבור $a=F$.
שקילות שניה:
עבור $a=T$ נקבל $T\lor F=T$ ואותה תוצאה תתקבל עבור $a=F$.


**למה** 8:
$$\displaylines{
F\lor a =a \\
T\land a = a
}
\tag{8}
$$
**הוכחה**:
שקילות ראשונה:
עבור a שווה T נקבל F או T שווה ל-T ועבור ערך a  שווה F נקבל $F\lor F=F$.
שקילות שניה:
עבור a שווה T נקבל $T\land T =T$  ועבור ערך a  שווה F נקבל $T \land F=F$.


**למה** 9
$$\displaylines{
a\lor a =a\\
a\land a= a
}
 \tag{9}
$$
**הוכחה**:
שקילות ראשונה:
אם a=T  אז $T\lor T=T$ אם a=F אז שוב $F\lor F=F$.
שקילות שניה:
אם אם a=T  אז $T\land T=T$ אם a=F אז שוב $F\land F=F$.



עד לכאן סיימנו עם הצרות שקילויות ותבונות שנשתמש בהן. אני רוצה שוב לדייק כל מה שהוספנו זו רק במטרה להקל על כתיבת הביטוי ולאפשר אפשרות לפשט אותו עד כמה שאפשר ובו זמנית ולהימנע משימוש בשקילויות מתקדמות יותר ולנסות להצימד לאלגוריתם נאיבי. אפשר להתייחס לזה כסוכר סינטקטי.

$$
\phi = \phi_{1}\leftrightarrow \phi_{2}=^{1}(\lnot \phi_{1}\lor \phi_{2})\land (\lnot \phi_{2}\lor \phi_{1})
$$
1. המעבר לפי (6)


נתבונן 
$$
\displaylines{\lnot \phi_{1}= \lnot \left( (a \land \lnot c) \lor (f\to (h \lor \lnot a))\right) =^1 \left( \lnot (a\land \lnot c) \land \lnot (\lnot f \lor (h \lor \lnot a)\right)=
^2\\
=(\lnot a \lor c) \land (f \land (\lnot h \land a)) = (\lnot a \lor c) \land f \land \lnot h \land a =^3 ((\lnot a \lor c) \land a ) \land f \land \lnot h=\\
= ((\lnot a \land a) \lor (a \land c)) \land f \land \lnot h=^4 \\
= (F\lor (a\land c))\land f \land \lnot h= (a\land c \land \lnot h\land f)\
}
$$


1. לפי כלל (4) וגם (3)
2. לפי כלל (4) וגם כלל (5).
3. לפי קומוטטיביות ואסוציאטיביות של אופרטורים בינארים מאותו סוג. 
4. לפי (7)
5. לפי (8.
6. 

$$
\displaylines{\phi_{2}=(a\land f) \lor \left(\lnot a \to (b\land g)\right)=^{1}\\
= (a \land f) \lor (a \lor (b\land g))=^{2} (a\land f)\lor ((a\lor b) \land (a\lor g)) =^3\\= \left( (a\land f)\lor (a\lor b)\right)\land \left((a\land f) \lor (a\lor g)\right) =^4\\
= \left( \left(a \lor (a\lor b)\right) \land \left(f \lor (a\lor b)\right)   \right)\land \left( \left(a \lor (a\lor g)\right) \land \left(f \lor (a\lor g)\right)   \right) =^4\\
=(a\lor a \lor b)\land (f\lor a \lor b) \land (a\lor a \lor g)\land (f\lor a \lor g)=^{6}\\
= (a \lor b) \land (f \lor a \lor b) \land (a\lor g) \land (f\lor a \lor g)
 }
$$
1. לפי (3), (5)
2. לפי (1)
3. לפי (1) אבל ברמת היטויים בסוגריים.
4. לפי (1), אותו רעיון.
5. אסוציאטיביות של אופרטורים מבינארים מאותו סוג.
6. לפי (9)
7. 
$$
\displaylines{
\lnot \phi_{1} \lor \phi_{2}= \\
(a\land c \land \lnot h\land f) \lor ((a \lor b) \land (f \lor a \lor b) \land (a\lor g) \land (f\lor a \lor g))=^{1}\\
= \left( X \lor (a\lor b) \right)\land (X \lor (f\lor a \lor b)) \land (X \lor (a\lor g))\land (X\lor (f \lor a\lor g))
}
$$
1. סימנו את הסיטוי $(a\land c \land \lnot h\land f)$ ב-$X$ להקל על הקריאה. ואנחנו משתמשים בצורה מורחבת של ביטוי (1) אשר הוכחנו לעיל.

נחלק למקרים ושוב לרשה לעצמנו לפשט ביטוי בפסוקית שיש כפילויות של ליטרלים ולהשאיר רק אחד מהם.
$$
\displaylines{(a\land c \land \lnot h\land f) \lor (a\lor b) =\\
= ( a \lor b) \land (c \lor a \lor b) \land (\lnot h\lor a \lor b) \land (f\lor a\lor b)
}
$$
$$
\displaylines{
(a\land c \land \lnot h\land f) \lor (f \lor a \lor b) = \\ 
= (a \lor a \lor f \lor b) \land (c \lor f \lor a \lor b) \land (\lnot h\lor f\lor a\lor b) \land (f\lor f\lor a \lor b) = \\
( a \lor f \lor b) \land (c \lor f \lor a \lor b) \land (\lnot h\lor f\lor a\lor b) \land ( f\lor a \lor b)
}
$$
$$
\displaylines{(a\land c \land \lnot h\land f) \lor (a\lor g) = \\=
(a\lor a\lor g) \land (c\lor a\lor g)\land (\lnot h \lor a\lor g) \land (f\lor a\lor g) = \\
( a\lor g) \land (c\lor a\lor g)\land (\lnot h \lor a\lor g) \land (f\lor a\lor g)
}
$$
$$\displaylines{(a\land c \land \lnot h\land f) \lor (f \lor a \lor g)=\\
= (a\lor f\lor a\lor g)\land (c\lor f\lor a \lor g) \land (\lnot h \lor f \lor a \lor g) \land (f \lor f \lor a \lor g) =\\
=( f\lor a\lor g)\land (c\lor f\lor a \lor g) \land (\lnot h \lor f \lor a \lor g) \land ( f \lor a \lor g)
}$$
בכל אחד מהפיתוחים אנחנו משתמבים שוב בהרחבה של ביטוי (1) או (2) אשר ציינו בהתחלה ואני מזכיר שזה רק במטרה להקל על פיתוח וקריאה, היינו יכולים גם לא להשתמש בזה ולבצע צעד צעד.

$$
\displaylines{
\lnot \phi_{1} \lor \phi_{2}= \\
( a \lor b) \land (c \lor a \lor b) \land (\lnot h\lor a \lor b) \land (f\lor a\lor b)\land \\
( a \lor f \lor b) \land (c \lor f \lor a \lor b) \land (\lnot h\lor f\lor a\lor b) \land ( f\lor a \lor b)\land \\
( a\lor g) \land (c\lor a\lor g)\land (\lnot h \lor a\lor g) \land (f\lor a\lor g)\land \\
( f\lor a\lor g)\land (c\lor f\lor a \lor g) \land (\lnot h \lor f \lor a \lor g) \land ( f \lor a \lor g) =^{1}\\\\
=( a \lor b) \land (c \lor a \lor b) \land (\lnot h\lor a \lor b) \land (f\lor a\lor b)\land \\
 (c \lor f \lor a \lor b) \land (\lnot h\lor f\lor a\lor b)\land \\
( a\lor g) \land (c\lor a\lor g)\land (\lnot h \lor a\lor g) \land (f\lor a\lor g)\land \\
( f\lor a\lor g)\land (c\lor f\lor a \lor g) \land (\lnot h \lor f \lor a \lor g) \land ( f \lor a \lor g)=^{2}\\\\
= ( a \lor b) \land (c \lor a \lor b) \land (\lnot h\lor a \lor b) \land (f\lor a\lor b)\land \\
 (c \lor f \lor a \lor b) \land (\lnot h\lor f\lor a\lor b)\land \\
( a\lor g) \land (c\lor a\lor g)\land (\lnot h \lor a\lor g) \land (f\lor a\lor g)\land \\
 (c\lor f\lor a \lor g) \land (\lnot h \lor f \lor a \lor g)
}
$$

1. לצמצם חזרות של ביטוי $f\lor a\lor b$
2. לצמצם חזרות של ביטוי $f\lor a\lor g$




עד לכאן סיימנו עם חלק הראשון של ביטוי סופי ויש לנו עוד חלק השני להשלים. נמשיך.

$$
\displaylines{\lnot \phi_{2}= \lnot ((a\land f) \lor \left(\lnot a \to (b\land g)\right))=^1 \lnot (a \land f )\land \lnot ( a \lor (b\land g))=^2\\
= (\lnot a \lor \lnot f) \land (\lnot a \land \lnot (b\land g))=^{2}(\lnot a\lor \lnot f)\land (\lnot a) \land (\lnot b \lor \lnot g)
}
$$
1. כלל (4) וגם (3)
2. כלל (4)


$$
\displaylines{\phi_{1}=  (a \land \lnot c) \lor (f\to (h \lor \lnot a))=^{1}\\
= (a\land \lnot c) \lor (\lnot f \lor (h\lor \lnot a)) =^{2} \\
= (a\land \lnot c) \lor (\lnot f \lor h \lor \lnot a) =^{3} \\
= ((a\land \lnot c) \lor \lnot a) \lor \lnot f \lor h)=^{4}\\
= ((a\lor \lnot a)) \land (\lnot c \lor \lnot a))\lor \lnot f\lor h=^{5}\\
= ((T)\land (\lnot c \lor\lnot a) ) \lor\lnot f\lor h=^{6}\\
=(\lnot c \lor \lnot a \lor \lnot f\lor h)
}
$$
1. לפי (3)
2. לפי אסוציאטיביות של אופרטור בינארי מאותו סוג.
3. לפי קומוטטיביות ואסוציאטיביות של אופרטור בינארי מאותו סוג.
4. לפי (1)
5. לפי (7)
6. לפי (8)

$$
\displaylines{\phi_{1}\lor \lnot\phi_{2} =\\ \\
(\lnot c \lor \lnot a \lor \lnot f\lor h) \lor ((\lnot a\lor \lnot f)\land (\lnot a) \land (\lnot b \lor \lnot g)) =^{1} \\
= ((\lnot c \lor \lnot a \lor \lnot f\lor h) \lor (\lnot a\lor \lnot f))\land \\
((\lnot c \lor \lnot a \lor \lnot f\lor h)\lor (\lnot a))\land \\
((\lnot c \lor \lnot a \lor \lnot f\lor h)\lor (\lnot b\lor \lnot g))=^{2}\\\\
=(\lnot c \lor \lnot a \lnot \lor \lnot f \lor h)\land (\lnot c \lor \lnot a\lor\lnot f\lor h \lor\lnot b\lor\lnot g)


}
$$

1.  שימוש בכלל (1) מורכב
2. כאן יש מספר דברים שדורשים נימוק. 
	1. ראשן, נשים לב שבפסוקית ראשונה מופיע $\lnot a\lor a$ וכפי שהראנו קודם הביטוי הזה הוא טאוטולוגיה ותמיד TRUE. כיוון שהוא חלק מביטוי הפסקוית וומספיק רק שביטוי אחת יסתפק בשביל לספק את הפסוקית שלמה אז כל הפסוקית היא הופכת להיות TRUE. ולפי למה (7) $T\land a=a$ ולכן אפשר למחוק אותה.
	2. שנית, בפסוקית שניה $\lnot a$ מופיע פעמיים ופי (9) אםשר להשאיר רק אחד מהן.
	3. בנוסף השתמשנו באסוציאטיביות וקומוטטיביות של אופרטור OR לעצמו.

סיימנו גם חלק השני ומכאן 
$$
\displaylines{
\phi = (\lnot \phi _{1} \lor \phi_{2})\land (\phi_{1}\lor \lnot \phi_{2})=\\
( a \lor b) \land (c \lor a \lor b) \land (\lnot h\lor a \lor b) \land (f\lor a\lor b)\land \\
 (c \lor f \lor a \lor b) \land (\lnot h\lor f\lor a\lor b)\land \\
( a\lor g) \land (c\lor a\lor g)\land (\lnot h \lor a\lor g) \land (f\lor a\lor g)\land \\
 (c\lor f\lor a \lor g) \land (\lnot h \lor f \lor a \lor g)\land \\
 (\lnot c \lor \lnot a \lnot \lor \lnot f \lor h)\land (\lnot c \lor \lnot a\lor\lnot f\lor h \lor\lnot b\lor\lnot g)
}
$$



