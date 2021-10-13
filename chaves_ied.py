from flask_restful import Resource, reqparse

chaves_ied = [  
    { 
    'chave_id': 'CH01',
	'IED': 1,
    'upstream': 'bus1_01',
    'downstream': 'path_A1',
	'FLAG_N': 'C',
    'FLAG_D': 'C',
	'CH_C': 'false',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S1',
	'rnp': 1
	},
    { 
    'chave_id': 'CH02',
	'IED': 2,
    'upstream': 'path_A1',
    'downstream': 'path_B1',
	'FLAG_N': 'C',
    'FLAG_D': 'C',
	'CH_C': 'false',
	'CH_rec': 'false',
    'Manobra':'01',
    'Sub': 'S1',
	'rnp': 2	
	},
    { 
    'chave_id': 'CH03_d',
	'IED': 3,
    'upstream': 'path_B1',
    'downstream': 'path_C1',
	'FLAG_N': 'O',
    'FLAG_D': 'O',
	'CH_C': 'True',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S1',
	'rnp': 3
	},				
	{ 
    'chave_id': 'CH06',
	'IED': 6,
    'upstream': 'bus2_01',
    'downstream': 'path_E1',
	'FLAG_N': 'C',
    'FLAG_D': 'C',
	'CH_C': 'false',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S1',
	'rnp': 1
	},
    { 
    'chave_id': 'CH07',
	'IED': 7,
    'upstream': 'path_E1',
    'downstream': 'path_F1',
	'FLAG_N': 'C',
    'FLAG_D': 'C',
	'CH_C': 'false',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S1',
	'rnp': 2
	},
    { 
    'chave_id': 'CH08_d',
	'IED': 8,
    'upstream': 'path_F1',
    'downstream': 'path_K1',
	'FLAG_N': 'O',
    'FLAG_D': 'O',
	'CH_C': 'True',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S1',
	'rnp': 3
	},
    { 
    'chave_id': 'CH09',
	'IED': 9,
    'upstream': 'bus3_01',
    'downstream': 'path_G1',
	'FLAG_N': 'C',
    'FLAG_D': 'C',
	'CH_C': 'false',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S1',
	'rnp': 1
	},
	{ 
    'chave_id': 'CH19_d',
	'IED': 19,
    'upstream': 'path_G1',
    'downstream': 'path_J1',
	'FLAG_N': 'O',
    'FLAG_D': 'O',
	'CH_C': 'false',
	'CH_rec': 'true',
    'Manobra':'01',
	'Sub': 'S1',
	'rnp': 2
	},
    { 
    'chave_id': 'CH10',
	'IED': 10,
    'upstream': 'path_G1',
    'downstream': 'path_H1',
	'FLAG_N': 'C',
    'FLAG_D': 'C',
	'CH_C': 'false',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S1',
	'rnp': 2
	},
    { 
    'chave_id': 'CH11_d',
	'IED': 11,
    'upstream': 'path_H1',
    'downstream': 'path_K1',
	'FLAG_N': 'O',
    'FLAG_D': 'O',
	'CH_C': 'True',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S1',
	'rnp': 3
	},	
	{ 
    'chave_id': 'CH13',
	'IED': 13,
    'upstream': 'bus4_01',
    'downstream': 'path_I1',
	'FLAG_N': 'C',
    'FLAG_D': 'C',
	'CH_C': 'false',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S1',
	'rnp': 1
	},
	{ 
    'chave_id': 'CH14',
	'IED': 19,
    'upstream': 'path_I1',
    'downstream': 'path_J1',
	'FLAG_N': 'C',
    'FLAG_D': 'C',
	'CH_C': 'false',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S1',
	'rnp': 2
	},
    { 
    'chave_id': 'CH19_i',
	'IED': 10,
    'upstream': 'path_J1',
    'downstream': 'path_G1',
	'FLAG_N': 'O',
    'FLAG_D': 'O',
	'CH_C': 'false',
	'CH_rec': 'true',
    'Manobra':'01',
	'Sub': 'S1',
	'rnp': 3
	},
    { 
    'chave_id': 'CH15',
	'IED': 15,
    'upstream': 'path_J1',
    'downstream': 'path_L1',
	'FLAG_N': 'C',
    'FLAG_D': 'C',
	'CH_C': 'false',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S1',
	'rnp': 3
	},
    { 
    'chave_id': 'CH16',
	'IED': 16,
    'upstream': 'path_L1',
    'downstream': 'path_M1',
	'FLAG_N': 'O',
    'FLAG_D': 'O',
	'CH_C': 'True',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S1',
	'rnp': 4
	},
	{ 
    'chave_id': 'CH05',
	'IED': 1,
    'upstream': 'bus1_02',
    'downstream': 'path_D1',
	'FLAG_N': 'C',
    'FLAG_D': 'C',
	'CH_C': 'false',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S2',
	'rnp': 1
	},
    { 
    'chave_id': 'CH04',
	'IED': 4,
    'upstream': 'path_D1',
    'downstream': 'path_C1',
	'FLAG_N': 'C',
    'FLAG_D': 'C',
	'CH_C': 'false',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S2',
	'rnp': 2
	},
    { 
    'chave_id': 'CH03_i',
	'IED': 3,
    'upstream': 'path_C1',
    'downstream': 'path_B1',
	'FLAG_N': 'O',
    'FLAG_D': 'O',
	'CH_C': 'True',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S2',
	'rnp': 3
	 },
	 { 
    'chave_id': 'CH12',
	'IED': 12,
    'upstream': 'bus2_02',
    'downstream': 'path_K1',
	'FLAG_N': 'C',
    'FLAG_D': 'C',
	'CH_C': 'false',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S2',
	'rnp': 1
	 },
     { 
    'chave_id': 'CH08_i',
	'IED': 8,
    'upstream': 'path_K1',
    'downstream': 'path_F1',
	'FLAG_N': 'A',
    'FLAG_D': 'A',
	'CH_C': 'True',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S2',
	'rnp': 1
	 },
     { 
    'chave_id': 'CH11_i',
	'IED': 11,
    'upstream': 'path_K1',
    'downstream': 'path_H1',
	'FLAG_N': 'A',
    'FLAG_D': 'A',
	'CH_C': 'True',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S2',
	'rnp': 2
	 },
	 { 
    'chave_id': 'CH18',
	'IED': 18,
    'upstream': 'bus1_03',
    'downstream': 'path_N1',
	'FLAG_N': 'C',
    'FLAG_D': 'C',
	'CH_C': 'false',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S3',
	'rnp': 1
	},
    { 
    'chave_id': 'CH17',
	'IED': 17,
    'upstream': 'path_N1',
    'downstream': 'path_M1',
	'FLAG_N': 'C',
    'FLAG_D': 'C',
	'CH_C': 'false',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S3',
	'rnp': 2
	 },
     { 
    'chave_id': 'CH16_i',
	'IED': 16,
    'upstream': 'path_M1',
    'downstream': 'path_L1',
	'FLAG_N': 'O',
    'FLAG_D': 'O',
	'CH_C': 'True',
	'CH_rec': 'false',
    'Manobra':'01',
	'Sub': 'S3',
	'rnp': 3
	}
    ]

class Chaves_ied(Resource):
    def get(self):
        return {'chaves_ied': chaves_ied} #dicionario que é convertido para JSON (a biblioteca flask_restful) faz automatico

class Chave_ied(Resource):
	argumentos = reqparse.RequestParser()
	argumentos.add_argument('IED')
	argumentos.add_argument('upstream')
	argumentos.add_argument('downstream')
	argumentos.add_argument('FLAG_N')
	argumentos.add_argument('FLAG_D')
	argumentos.add_argument('CH_C')
	argumentos.add_argument('Manobra')
	argumentos.add_argument('Sub')
	argumentos.add_argument('rnp')
	# Modelo que pega os argumentos que se deseja de uma subestação, melhor controle.
	
	def find_chave(chave_id):
		for chave_ied in chaves_ied:
			if chave_ied['chave_id'] == chave_id:
			    return chave_ied
		return None

	def get(self, chave_id):
		# Metodo transposto para o metodo find_chave
		#for chave_ied in chaves_ied:
		#	if chave_ied['chave_id'] == chave_id:
		#	    return chave_ied
		chave_ied = Chave_ied.find_chave(chave_id)
		if chave_ied:
			return chave_ied
		return {'message':'Chave IED not found'}, 404 #not found

	def post(self, chave_id):
	    
		dados = Chave_ied.argumentos.parse_args()
        
		        #nova_chave = { 
		#	'chave_id': chave_id,
		#    'IED': dados['IED'],
		#    'upstream': dados['upstream'],
		#    'downstream': dados['downstream'],
		#    'FLAG_N': dados['FLAG_N'],
		#    'FLAG_D': dados['FLAG_D'],
		#    'CH_C': dados['CH_C'],
		#    'Manobra': dados['Manobra'],
		#    'Sub': dados['Sub'],
		#    'rnp': dados['rnp']
		#}
		# Maneira que se repetiria, substituida pelo comando cahve-valor com **kargs (**dados)
		nova_chave = { 'chave_id': chave_id, **dados }
		chaves_ied.append(nova_chave)
	    
		return nova_chave, 200 # OK
		
	def put(self, chave_id):
		
		dados = Chave_ied.argumentos.parse_args()
		nova_chave = { 'chave_id': chave_id, **dados }

		chave_ied = Chave_ied.find_chave(chave_id)
		if chave_ied:
		   chave_ied.update(nova_chave)
		   return nova_chave, 200 #OK
		chaves_ied.append(nova_chave)
		return nova_chave, 201 # created criado


	def delete(self, chave_id):
		global chaves_ied
		chaves_ied = [chave for chave in chaves_ied if chave ['chave_id'] != chave_id ]
		return {'mesage': 'chave_id retirada'}

