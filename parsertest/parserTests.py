testCases = [\
		('''var<<[["checkbox"]] ''', "assignmentLeft", 1),\
		('''[["checkbox"]]>>var ''', "assignmentRight", 1),\
		('''1==1''', "compCondition", 1),\
		('''!(1==1)''', "condition", 1),\
		('''true&&1==1''', "condition", 1),\
		('''(1==1)||!x''', "condition", 1),\
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
		('''"string+*  	^&()[]\{\}/.,!~~$%^@#$%^&*"''', "string", 1),\
		('''"{{1==1|"x"}}{{1==1|"f"}}"''', "extendedString", 1),\
		('''"x{{1==1|"f"}}"''', "extendedString", 1),\
		('''"x{{1==1|"f"}}{{1==1|"x"}}"''', "extendedString", 1),\
		('''"{{1==1|"f"}}g"''', "extendedString", 1),\
		('''"x{{1==1|"f"}}g"''', "extendedString", 1),\
		('''"x{{2!=4&& !x|"f" | "sf"}}g"''', "extendedString", 1),\
		('''"x{{2!=4&& !x|"{{1==1|"x"|"y"}}" | "sf"}}g"''', "extendedString", 1),\
		('''{{if 1==1}}\nx<<[["checkbox"]]\n{{elseif 1==1}}\n[["radiogroup"]]\n{{else}}\n[["select"]]>>y\n{{endif}}''', "widgetConditional", 1),\
		('''(1+1)''', "arythmExpr", 1),\
		('''1+1''', "arythmExpr", 1),\
		('''x-a.d''', "arythmExpr", 1),\
		('''(x-a.d)''', "arythmExpr", 1),\
		('''(1+1)/(x-a.d)''', "arythmExpr", 1),\
		('''-6+k.gh +-x''', "arythmExpr", 1),\
		('''name = -6+k.gh +-x''', "widgetArg", 1),\
		('''x*-9+(ad.k.p* 7 + 9) - 5''', "arythmExpr", 1),\
		('''x*-9+(ad.k.p* 7 + 9) - 5 == x''', "condition", 1),\
		('''"str{{x*-9+(ad.k.p* 7 + 9) - 5==x|"x"}}"''', "extendedString", 1),\
		('''"str{{1==x|"x"}}"''', "extendedString", 1),\
		('''var << "str{{1==x|"x"}}" ''', "assignmentLeft", 1),\
		('''var << "str{{x*-9+(ad.k.p* 7 + 9) - 5==x|"x"}}" ''', "assignmentLeft", 1),\
		('''{{iF x*-9+(ad.k.p* 7 + 9) - 5==x}}\nvar << 10\n{{ENDif }}''', "widgetConditional", 1),\
		('''var << 2+3 ''', "assignmentLeft", 1),\
		
		#SURVEY	
		('''var << [["checkbox"]]\n[["checkbox"]] >> var2 \n [["radio"]]''', "survey", 1),\
		('''var << [["checkbox"]]        {{ if !X || x.x == "str" && x }}\n[["checkbox"]]\n{{endif}}''', "survey", 1),\
		
		#WIDGET
		('''[["checkbox"]]''', "widget", 1),\
		('''[["radio"|"xxx"]]''', "widget", 1),\
		
		#WIDGET_CONDITIONAL
		('''{{ if !X || x.x == "str" && x }}\n[["checkbox"]]\n{{endif}}''', "widgetConditional", 1),\
		
		#ASSIGNMENT_LEFT
		('''ccACAf  <<       [["checkbox"]] ''', "assignmentLeft", 1),\
		
		#ASSIGNMENT_RIGHT
		('''[["checkbox"]]  >> vCSar ''', "assignmentRight", 1),\
		
		#WIDGET_ARG
		('''1''', "widgetArg", 1),\
		('''1+2''', "widgetArg", 1),\
		('''var = 5''', "widgetArg", 1),\
		('''var = iterator("ListIter")''', "widgetArg", 1),\
		('''var = (1,2,3)''', "widgetArg", 1),\
		('''var = [(1,23),(xx,"yz")]''', "widgetArg", 1),\
		('''([1,23],["c",x.y])''', "widgetArg", 1),\
		('''var = ([1,23],["c",x.y])''', "widgetArg", 1),\
		('''xxx = datasource("URLDatasource","www.jkm.pl")''', "widgetArg", 1),\
		('''datasource("URLData")''', "widgetArg", 1),\
		('''"string"''', "widgetArg", 1),\
		('''True''', "widgetArg", 1),\
		('''5*44 + (-3)''', "widgetArg", 1),\

		#LIST_WITH_TUPLES
		('''[(1,23),(xx,"yz"), (123,x.y,True,FaLSe), 11, ("asd{{1==2|"x"}}",5)]''', "listWithTuples", 1),\
		('''[1]''', "listWithTuples", 1),\

		#LIST_WITH_TUPLES_ELEMENT
		('''(1,23)''', "listWithTuplesElement", 1),\
		('''(123,x.y,True,FaLSe)''', "listWithTuplesElement", 1),\
		('''11''', "listWithTuplesElement", 1),\
		('''("asd{{1==2|"x"}}",5)''', "listWithTuplesElement", 1),\
		
		#LIST_WITHOUT_TUPLES
		('''[xx,"yz",123,x.y,True,FaLSe,"asd{{1==2|"x"}}"]''', "listWithoutTuples", 1),\
		
		#LIST_WITOUTH_TUPLES_ELEMENT
		('''23.9''', "listWithoutTuplesElement", 1),\
		('''True''', "listWithoutTuplesElement", 1),\
		('''11''', "listWithoutTuplesElement", 1),\
		('''"asd{{1==2|"x"}}"''', "listWithoutTuplesElement", 1),\
		
		#TUPLE_WITH_LIST
		('''([1,23],["c",x.y])''', "tupleWithLists", 1),\
		('''(11,2,[1])''', "tupleWithLists", 1),\
		('''(1)''', "tupleWithLists", 1),\
		('''([1,23],["c",x.y,"asd{{1==2|"x"}}"])''', "tupleWithLists", 1),\
		
		#TUPLE_WITH_LIST_ELEMENT
		('''["c",x.y]''', "tupleWithListsElement", 1),\
		('''True''', "tupleWithListsElement", 1),\
		('''"xx.crtfc.pp"''', "tupleWithListsElement", 1),\
		('''["c",x.y,"asd{{1==2|"x"}}"]''', "tupleWithListsElement", 1),\

		#TUPLE_WITHOUT_LIST
		('''(23,"c",x.y)''', "tupleWithoutLists", 1),\
		('''(1)''', "tupleWithoutLists", 1),\
		('''("asd{{1==2|"x"}}")''', "tupleWithoutLists", 1),\

		#TUPLE_WITHOUT_LIST_ELEMENT
		('''"c"''', "tupleWithoutListsElement", 1),\
		('''23''', "tupleWithoutListsElement", 1),\
		('''x.y''', "tupleWithoutListsElement", 1),\
		('''var = "trololo"''', "tupleWithoutListsElement", 1),\
		('''"asd{{1==2|"x"}}"''', "tupleWithoutListsElement", 1),\
		
		#ITERATOR
		('''iterator("ListIter")''', "iterator", 1),\
		('''iterator("ListIter", "xxx")''', "iterator", 1),\
		('''iterator("ListIter", "xxx", True, datasource("URLData"))''', "iterator", 1),\
		('''iterator("ListIter", v1 = "xxx", v2 = True,dat = datasource("URLData"))''', "iterator", 1),\
		('''iterator("ListIter", v1 = "xxx", v2 = True,dat = datasource("URLData"), "asd{{1==2|"x"}}")''', "iterator", 1),\
		('''iterator("adfsa",564.5,zmienna)''', "iterator", 1),\
		('''iterator("perm", name=value,num=-85.684)''', "iterator", 1),\
		('''iterator("nth", datasource("xx",name=value,-5.96),data=datasource("x"),datasource)''', "iterator", 1),\

		#ITERATOR_ARG
		('''"xxx"''', "iteratorArg", 1),\
		('''True''', "iteratorArg", 1),\
		('''datasource("URLData")''', "iteratorArg", 1),\
		('''x.y.z''', "iteratorArg", 1),\
		('''v1 = "xxx"''', "iteratorArg", 1),\
		('''va = 11''', "iteratorArg", 1),\
		('''xxx = datasource("URLData")''', "iteratorArg", 1),\

		#DATASOURCE
		('''datasource("URLDatasource","www.jkm.pl")''', "datasource", 1),\
		('''datasource("URLData",x, 1234, True, -1.12, x.uuu.z,"asd{{1==2|"x"}}")''', "datasource", 1),\
		('''datasource("URLData",xx = x,  v1 = 1234, v2 = True, v3=-1.12, v4=x.uuu.z,v5="asd{{1==2|"x"}}")''', "datasource", 1),\
		('''datasource("a",5.8,xxx)''', "datasource", 1),\
		('''datasource("url", name=value,num=-0.6955)''', "datasource", 1),\
		
		#DATASOURCE_ARG
		('''"www.jkm.pl"''', "datasourceArg", 1),\
		('''1234''', "datasourceArg", 1),\
		('''True''', "datasourceArg", 1),\
		('''-1.12''', "datasourceArg", 1),\
		('''x.uuu.z''', "datasourceArg", 1),\
		('''"asd{{1==2|"x"}}"''', "datasourceArg", 1),\
		('''var = "www.jkm.pl"''', "datasourceArg", 1),\
		('''var = 1234''', "datasourceArg", 1),\
		('''var =True''', "datasourceArg", 1),\
		('''var=-1.12''', "datasourceArg", 1),\
		('''var=x.uuu.z''', "datasourceArg", 1),\
		('''var = "asd{{1==2|"x"}}"''', "datasourceArg", 1),\
		('''var = x''', "datasourceArg", 1),\

		#ID
		('''asdfg''', "id", 1),\
		('''DSFGasdfg''', "id", 1),\
		('''asdwsdffDSRFHg''', "id", 1),\
		('''a123s134dfg''', "id", 1),\

		#SIMPLE_VALUE
		('''"www.jkm.pl"''', "simpleValue", 1),\
		('''1234''', "simpleValue", 1),\
		('''True''', "simpleValue", 1),\
		('''-1.12''', "simpleValue", 1),\
		('''x.uuu.z''', "simpleValue", 1),\
		('''"asd{{1==2|"x"}}"''', "simpleValue", 1),\
		
		#SIMPLE_EXPR_VALUE
		('''"www.jkm.pl"''', "simpleExprValue", 1),\
		('''1234''', "simpleExprValue", 1),\
		('''True''', "simpleExprValue", 1),\
		('''-1.12''', "simpleExprValue", 1),\
		('''x.uuu.z''', "simpleExprValue", 1),\
		('''"asd{{1==2|"x"}}"''', "simpleExprValue", 1),\
		('''(5)''', "simpleExprValue", 1),\
		('''(-7.13)''', "simpleExprValue", 1),\
		('''1+23*x''', "simpleExprValue", 1),\
		('''x+x.yr/v''', "simpleExprValue", 1),\
		('''5*z''', "simpleExprValue", 1),\
		('''(1+3/5)*(-1/x+4)*(x.xx+6)''', "simpleExprValue", 1),\

		#VAR_ID
		('''asdfg''', "varId", 1),\
		('''DSFGasdfg''', "varId", 1),\
		('''asdwsdffDSRFHg''', "varId", 1),\
		('''a123s134dfg''', "varId", 1),\

		#STRUCT_ELEM
		('''DSFGasdfg.adsfdasf''', "structElem", 1),\
		('''asdwsdffDSRFHg.dfsgwe.a12324''', "structElem", 1),\
		('''a123s134dfg.Aw345''', "structElem", 1),\

		#NUMBER
		('''16513''', "number", 1),\
		('''0''', "number", 1),\
		('''-68451''', "number", 1),\
		('''156.16''', "number", 1),\
		('''-561.6''', "number", 1),\
		('''0.66''', "number", 1),\
		('''-0.69''', "number", 1),\

		#BOOL
		('''true''', "bool", 1),\
		('''TRUE''', "bool", 1),\
		('''tRue''', "bool", 1),\
		('''trUe''', "bool", 1),\
		('''tRUE''', "bool", 1),\
		('''false''', "bool", 1),\
		('''FALSE''', "bool", 1),\
		('''fAlSE''', "bool", 1),\
		('''3''', "bool", 0),\

		#INNER_STRING
		('''string+*  	^&()[]\{\}\\"/.,!~~$%^@#$%^&*''', "innerString", 1),\
		('''string+*  	^&()[]\{\}/.,!~~$%^@#$%^&*''', "innerString", 1),\

		#STRING
		('''"string+*  	^&()[]\{\}\\"/.,!~~$%^@#$%^&*"''', "string", 1),\
		('''"string+*  	^&()[]\{\}/.,!~~$%^@#$%^&*"''', "string", 1),\

		#EXTENDED_STRING
		('''"string+*  	^&()[]\{\}\\"/.,!~~$%^@#$%{{2!=4&& !x|"f" | "sf"}}^&*"''', "extendedString", 1),\
		('''"string+*  	^&(){{2!=4&& !x|"{{1==1|"x"|"y"}}" | "sf"}}[]\{\}/.,!~~$%^@#$%^&*"''', "extendedString", 1),\
		('''"{{1==1|"x"}}{{1==1|"f"}}"''', "extendedString", 1),\
		('''"x{{1==1|"f"}}"''', "extendedString", 1),\
		('''"x{{1==1|"f"}}{{1==1|"x"}}"''', "extendedString", 1),\
		('''"{{1==1|"f"}}g"''', "extendedString", 1),\
		('''"x{{1==1|"f"}}{{1==1|"f"}}g"''', "extendedString", 1),\
		('''"x{{2!=4&& !x|"f" | "sf"}}g"''', "extendedString", 1),\
		('''"x{{2!=4&& !x|"{{1==1|"x"|"y"}}" | "sf"}}g"''', "extendedString", 1),\

		#STRING_CONDITIONAL
		('''{{2!=4&& !x|"f" | "sf"}}''', "stringConditional", 1),\
		('''{{1==1|"x"}}''', "stringConditional", 1),\
		
		#CONDITION
		('''x*-9+(ad.k.p* 7 + 9) - 5 == x''', "condition", 1),\
		('''x*-9+(ad.k.p* 7 + 9) - 5 == x && x > 1 || a < 3 || x.yy >= zmienna || x<="cos"''', "condition", 1),\
		('''5 == x or x.aa != val and xx == xy''', "condition", 1),\

		#CONDITION_CONTENT
		('''x*-9+(ad.k.p* 7 + 9) - 5 == x''', "conditionContent", 1),\
		('''x*-9+(ad.k.p* 7 + 9) - 5 == x && x > 1 || a < 3 || x.yy >= zmienna || x<="cos"''', "conditionContent", 1),\
		('''5 == x or x.aa != val and xx == False''', "conditionContent", 1),\

		#SUB_CONDITION
		('''(x*-9+(ad.k.p* 7 + 9) - 5 == x)''', "subCondition", 1),\
		('''(x*-9+(ad.k.p* 7 + 9) - 5 == x && x > 1 || a < 3 || x.yy >= zmienna || x<="cos")''', "subCondition", 1),\
		('''(!(5 == x))''', "subCondition", 1),\
		('''False''', "subCondition", 1),\
		('''!xx''', "subCondition", 1),\
		('''!x.y.z''', "subCondition", 1),\
		('''a > 5''', "subCondition", 1),\
		('''b < x.y''', "subCondition", 1),\

		#COMP_CONDITION
		('''!xx''', "subCondition", 1),\
		('''!x.y.z''', "subCondition", 1),\
		('''a > 5''', "subCondition", 1),\
		('''b < x.y''', "subCondition", 1),\

		#CONDITION_VALUE
		('''"www.jkm.pl"''', "conditionValue", 1),\
		('''1234''', "conditionValue", 1),\
		('''True''', "conditionValue", 1),\
		('''-1.12''', "conditionValue", 1),\
		('''x.uuu.z''', "conditionValue", 1),\
		('''(5)''', "conditionValue", 1),\
		('''(-7.13)''', "conditionValue", 1),\
		('''1+23*x''', "conditionValue", 1),\
		('''x+x.yr/v''', "conditionValue", 1),\
		('''5*z''', "conditionValue", 1),\
		('''(1+3/5)*(-1/x+4)*(x.xx+6)''', "conditionValue", 1),\

		#ARYTHM_EXPR
		('''(5)''', "arythmExpr", 1),\
		('''(-7.13)''', "arythmExpr", 1),\
		('''1+23*x''', "arythmExpr", 1),\
		('''x+x.yr/v''', "arythmExpr", 1),\
		('''5*z''', "arythmExpr", 1),\
		('''(1+3/5)*(-1/x+4)*(x.xx+6)''', "arythmExpr", 1),\

		#ARYTHM_EXPR_TOP_LEVEL_CONTENT
		('''(5)''', "arythmExprTopLevelContent", 1),\
		('''(-7.13)''', "arythmExprTopLevelContent", 1),\
		('''1+23*x''', "arythmExprTopLevelContent", 1),\
		('''x+x.yr/v''', "arythmExprTopLevelContent", 1),\
		('''5*z''', "arythmExprTopLevelContent", 1),\
		('''(1+3/5)*(-1/x+4)*(x.xx+6)''', "arythmExprTopLevelContent", 1),\

		#ARYTHM_EXPR_CONTENT
		('''1''', "arythmExprContent", 1),\
		('''1.1''', "arythmExprContent", 1),\
		('''-(5)''', "arythmExprContent", 1),\
		('''(-7.13)''', "arythmExprContent", 1),\
		('''-(1+23*x)/xx+(12)''', "arythmExprContent", 1),\
		('''-(x+x.yr/v)''', "arythmExprContent", 1),\
		('''-z*ge''', "arythmExprContent", 1),\
		('''-x.yy+ xx''', "arythmExprContent", 1),\

		#SUB_ARYTHM_EXPR
		('''1''', "subArythmExpr", 1),\
		('''1.1''', "subArythmExpr", 1),\
		('''-(5)''', "subArythmExpr", 1),\
		('''(-7.13)''', "subArythmExpr", 1),\
		('''-(1+23*x)''', "subArythmExpr", 1),\
		('''-(x+x.yr/v)''', "subArythmExpr", 1),\
		('''-z''', "subArythmExpr", 1),\
		('''-x.yy''', "subArythmExpr", 1),\

		#ARYTHM_OP
		('''-''', "arythmOp", 1),\
		('''+''', "arythmOp", 1),\
		('''*''', "arythmOp", 1),\
		('''/''', "arythmOp", 1),\

		#COMP_OP
		('''==''', "compOp", 1),\
		('''!=''', "compOp", 1),\
		('''>''', "compOp", 1),\
		('''>=''', "compOp", 1),\
		('''<=''', "compOp", 1),\
		('''<''', "compOp", 1),\

		#LOGIC_OP
		('''&&''', "logicOp", 1),\
		('''and''', "logicOp", 1),\
		('''||''', "logicOp", 1),\
		('''or''', "logicOp", 1),\

		#WS
		(''' ''', "ws", 1),\
		('''	''', "ws", 1),\
		('''\n''', "ws", 1),\
		('''\r''', "ws", 1),\
		('''\t''', "ws", 1),\


		]
