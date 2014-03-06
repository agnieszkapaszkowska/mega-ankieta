testCases = [
		'''[["radio"|var1|var2]]''',
		'''[["radio"|var1.x|var2.y]]''',
		'''[["text"|"x{{2!=4&& !x|"{{1==1|"x"|"y"}}" | "sf"}}g"]]''',
		'''[["radio"|"x"|iterator("test", "x")]]''',
		'''[["radio"|"x"|iterator("test", datasource("test", "x"))]]'''
		]
