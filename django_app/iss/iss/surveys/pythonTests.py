testCases = [
		#WIDGETS
		'''[["radio"|var1|var2]]''',
		'''[["radio"|var1.x|var2.y]]''',
		'''[["text"|"x{{2!=4&& !x|"{{1==1|"x"|"y"}}" | "sf"}}g"]]''',
		'''[["radio"|"x"|iterator("test", "x")]]''',
		'''[["radio"|"x"|iterator("test", datasource("test", "x"))]]''',

		#ASSIGN_LEFT
		'''x << [["text"|"trololo"]] ''',
		'''x << [["radio"|var1|var2]] ''',
		'''x << [1,2,3] ''',
		'''x << (1,2,3) ''',
		'''x << y ''',
		'''x << [["radio"|"x"|iterator("test", "x")]] ''',
		'''x << [["radio"|"x"|iterator("test", datasource("test", "x"))]] ''',
		'''x << iterator("test", "x") ''',
		'''x << datasource("test", "x") ''',
		'''x << TRUE ''',
		'''x << 1+1 ''',
		'''x << "str" ''',
		'''x << "str{{1==1|"1"|"nie"}}" ''',
		'''x << y.y.z ''',
		'''x << 1.12 ''',
		'''x << (1+1)/43 + x.c*(-4) ''',

		#ASSIGN_RIGHT
		'''[["text"|"trololo"]] >> x ''',
		'''[["radio"|var1|var2]] >> x ''',
		'''[["radio"|var1.c|var2.d]] >> x ''',
		'''[["radio"|"x"|iterator("test", "x")]] >> x ''',
		'''[["radio"|"x"|iterator("test", datasource("test", "x"))]] >> x ''',

		#SURVEY
		'''[["radio"|var1|var2]]\n[["radio"|var1.x|var2.y]][["text"|"x{{2!=4&& !x|"{{1==1|"x"|"y"}}" | "sf"}}g"]]''',
		'''x << [["text"|"trololo"]]\nx << [["radio"|var1|var2]] ''',
		'''[["text"|"trololo"]] >> x\n[["radio"|var1|var2]] >> x ''',
		'''[["radio"|var1|var2]]\nx << [["text"|"trololo"]]\n[["text"|"trololo"]] >> x ''',
		'''[["radio"|var1|var2]] x << [["text"|"trololo"]]\t[["text"|"trololo"]] >> x ''',
		'''x << [["text"|"trololo"]]\n[["radio"|var1|var2]]\n[["text"|"trololo"]] >> x ''',
		'''[["text"|"trololo"]] >> x x << [["text"|"trololo"]]\n[["radio"|var1|var2]]''',
		'''x << [["radio"|"x"|iterator("test", "x")]] x << [["radio"|"x"|iterator("test", datasource("test", "x"))]] ''',
		'''[["radio"|"x"|iterator("test", "x")]][["radio"|"x"|iterator("test", datasource("test", "x"))]]''',
		'''[["radio"|"x"|iterator("test", "x")]] >> x [["radio"|"x"|iterator("test", datasource("test", "x"))]] >> x ''',
		


		''' '''
		]
