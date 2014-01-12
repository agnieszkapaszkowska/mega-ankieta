testCases = [\
		('''var<<[["checkbox"]]''', "assignmentLeft", 1),\
		('''[["checkbox"]]>>var ''', "assignmentRight", 1),\
		('''1==1&&true&&(true&&!(false)||1==1)''', "condition", 1),\
		('''{{ If ((6 == 8 && 1 > 0 && "xxx" == str || ( ! true && a.b.c.d != "abc" ) )) }} \nxx << 5\n{{  eNdIf }}''', "widgetConditional", 1),\
		('''x.x.fda==5&&!(aa!="str")||(!(var)&&(5>=a.f)||!x)''', "condition", 1),\
		('''{{ if !X || x.x == "str" && x }}\n[["checkbox"]]\n{{endif}}''', "widgetConditional", 1),\
		('''datasource("a",5.8,xxx)''', "datasource", 1),\
		('''datasource("url", name=value,num=-0.6955)''', "datasource", 1),\
		('''iterator("adfsa",564.5,zmienna)''', "iterator", 1),\
		('''iterator("perm", name=value,num=-85.684)''', "iterator", 1),\
		('''iterator("nth", datasource("xx",name=value,-5.96),data=datasource("x"),datasource)''', "iterator", 1),\
		('''16513''', "number", 1),\
		('''0''', "number", 1),\
		('''-68451''', "number", 1),\
		('''156.16''', "number", 1),\
		('''-561.6''', "number", 1),\
		('''0.66''', "number", 1),\
		('''-0.69''', "number", 1),\
		('''"string"''', "string", 1),\
		('''"string+*  	^&()[]{}/.,!~~$%^@#$%^&*"''', "string", 1),\
		('''"x{{1==1|"f"}}g"''', "extendedString", 1),\
		('''"x{{2!=4&& !x|"f" | "sf"}}g"''', "extendedString", 1),\
		('''"x{{2!=4&& !x|"{{1==1|"x"|"y"}}" | "sf"}}g"''', "extendedString", 1),\
		('''{{if 1==1}}\nx<<[["checkbox"]]\n{{elseif 1==1}}\n[["radiogroup"]]\n{{else}}\n[["select"]]>>y\n{{endif}}''', "widgetConditional", 1),\
		]
