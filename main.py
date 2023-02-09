#boas vindas
print('Bem vindo(a) ao Simulador de SISU (por enquanto só da UFG - Campus Samambaia).')
print('\nSua média final será calculada de acordo com os pesos atualizados de 2023 oficiais disponibilizados pela UFG. \nVocê pode acessar o PDF com os pesos aqui: https://showrtner.com/lninIyh')
print('\nIMPORTANTE: Separe as casas decimais das notas que você inserir a seguir por um ponto, e não por vírgula.')
input('\nAperte ENTER para prosseguir. ')

#inputs de nota
nota_linguagens = float(input('\nInsira sua nota na área de Linguagens: '))
nota_matematica = float(input('Insira sua nota na área de Matemática: '))
nota_natureza = float(input('Insira sua nota na área de Ciências da Natureza: '))
nota_humanas = float(input('Insira sua nota na área de Ciências Humanas: '))
nota_redacao = float(input('Insira sua nota na Redação: '))

#input do curso
cursoinserido = input('\nInsira o curso de desejo: ').lower()

#cursos listados por grupo
grupo1 = ['engenharia ambiental','engenharia civil','engenharia da computação',
'engenharia da computacao','engenharia da computaçao','engenharia de minas','engenharia de producao',
'engenharia de produção','engenharia de produçao','engenharia de transportes','engenharia eletrica',
'engenharia elétrica','engenharia fisica','engenharia física','engenharia mecanica','engenharia mecânica',
'engenharia quimica','engenharia química','estatistica','estatística','física','fisica','fisica medica',
'física médica','fisica médica','física medica','geologia','química','quimica']

grupo2 = ['matematica', 'matemática', 'matematica industrial', 'matemática industrial']

grupo3 = ['ciencia da computacao', 'ciência da computacao', 'ciência da computação',
 'ciencia da computaçao', 'ciência da computação', 'engenharia de software',
 'sistema de informacao', 'sistemas de informação', 'sistemas de informaçao']

grupo4 = ['biomedicina', 'biotecnologia', 'ciencias ambientais', 'ciências ambientais', 'ciencias biologicas',
'ciências biologicas', 'ciencias biológicas', 'ciências biológicas', 'ecologia e analise ambiental',
'ecologia e análise ambiental', 'enfermagem', 'farmacia', 'farmácia','fisioterapia', 'medicina', 'nutrição', 'nutricao', 'nutriçao', 'odontologia']

grupo5 = ['agronomia', 'engenharia de alimentos', 'engenharia florestal', 'medicina veterinaria', 'veterinaria', 'medicina veterinária', 'zootecnia']

grupo6 = ['filosofia', 'geografia', 'historia', 'história', 'pedagogia', 'psicologia', 'relacoes internacionais', 'relaçoes internacionais', 'relações internacionais']

grupo7 = ['administracao', 'administraçao', 'administração', 'arquitetura', 'arquitetura e urbanismo', 'biblioteconomia', 'ciencias contabeis', 'ciências contábeis',
'ciencias contábeis', 'ciências contabeis', 'ciencias economicas', 'ciências economicas', 'ciencias econômicas', 'ciências econômicas',
'ciencias sociais', 'ciências sociais', 'ciências sociais politicas publicas', 'ciências sociais políticas publicas', 'ciências sociais políticas públicas',
'ciencias sociais políticas publicas', 'ciencias sociais politicas publicas', 'comunicação social', 'comunicacao social', 'comunicaçao social', 'publicidade e propaganda',
'publicidade', 'direito', 'gestao da informacao', 'gestao da informação', 'gestão da informacao', 'gestão da informação', 'jornalismo', 'museologia', 'relacoes publicas', 'relações publicas',
'relaçoes publicas', 'relacoes públicas', 'relações públicas', 'relações publicas', 'serviço social', 'servico social',]

grupo8 = ['artes cenicas', 'artes cênicas', 'artes visuais', 'dança', 'design de ambientes', 'design de moda', 'design gráfico', 'design grafico', 'direção de arte', 'direcao de arte',
 'direçao de arte', 'letras espanhol', 'letras estudos literarios','letras frances', 'letras francês', 'letras ingles',
'letras inglês', 'letras libras', 'letras lingua portuguesa', 'letras portugues','letras linguistica', 'letras linguística'
'letras português', 'letras português/inglês', 'letras portugues/ingles',
'letras traducao e interpretacao de libras', 'letras tradução e interpretação de libras', 'letras libras/português', 'música', 'musica', 'musicoterapia']

#PESOS GRUPO 1
pesoling1=2.0
pesohum1=1.0
pesonatu1=2.5
pesomat1=3.0
pesored1=1.5

#PESOS GRUPO 2
pesoling2=2.0
pesohum2=1.0
pesonatu2=1.5
pesomat2=4.0
pesored2=1.5

#PESOS GRUPO 3
pesoling3=2.0
pesohum3=1.0
pesonatu3=1.0
pesomat3=4.0
pesored3=2.0

#PESOS GRUPO 4
pesoling4=2.0
pesohum4=1.5
pesonatu4=3.0
pesomat4=1.5
pesored4=2.0

#PESOS GRUPO 5
pesoling5=2.0
pesohum5=1.0
pesonatu5=3.0
pesomat5=2.0
pesored5=2.0

#PESOS GRUPO 6
pesoling6=2.5
pesohum6=3.0
pesonatu6=1.0
pesomat6=1.0
pesored6=2.5

#PESOS GRUPO 7
pesoling7=2.5
pesohum7=2.0
pesonatu7=1.0
pesomat7=2.0
pesored7=2.5

#PESOS GRUPO 8
pesoling8=3.0
pesohum8=2.5
pesonatu8=1.0
pesomat8=1.0
pesored8=2.5

#criando excecao pra ed fisica (bacharel/licenciatura)
educacoesfisicas = ['educacao fisica', 'educacao fisica', 'educação física', 'educaçao fisica','educação fisica']

letrass = []
 
if cursoinserido in educacoesfisicas:

 input2 = input('Licenciatura ou bacharelado?\n[L] Licenciatura\n[B] Bacharelado\n') 

 if input == 'L':  #NOTA PRA LICENCIATURA

    notacompesoling6=(pesoling6*nota_linguagens)
    notacompesohum6=(pesohum6*nota_humanas)
    notacompesonatu6=(pesonatu6*nota_natureza)
    notacompesomat6=(pesomat6*nota_matematica)
    notacompesored6=(pesored6*nota_redacao)

    print('Segundo a divisão oficial da UFG, seu curso está contido no GRUPO 2.')
    print('\nNOTAS COM PESO DO GRUPO 2')
    print('\nLinguagens: {}'.format(round(notacompesoling6, 2)))
    print('Matemática: {}'.format(round(notacompesomat6, 2)))
    print('C. Natureza: {}'.format(round(notacompesonatu6, 2)))
    print('C. Humanas: {}'.format(round(notacompesohum6, 2)))
    print('Redação: {}'.format(round(notacompesored6, 2)))
    
    mediafinal = ((notacompesoling6+notacompesohum6+notacompesonatu6+notacompesomat6+notacompesored6)/10)
    print('\nA sua média final é de {}'.format(round(mediafinal, 2)))

 elif input == 'B':  #NOTA PRA BACHARELADO
    notacompesoling4=(pesoling4*nota_linguagens)
    notacompesohum4=(pesohum4*nota_humanas)
    notacompesonatu4=(pesonatu4*nota_natureza)
    notacompesomat4=(pesomat4*nota_matematica)
    notacompesored4=(pesored4*nota_redacao)

    print('Segundo a divisão oficial da UFG, seu curso está contido no GRUPO 4.')
    print('\nNOTAS COM PESO DO GRUPO 4')
    print('\nLinguagens: {}'.format(round(notacompesoling4, 2)))
    print('Matemática: {}'.format(round(notacompesomat4, 2)))
    print('C. Natureza: {}'.format(round(notacompesonatu4, 2)))
    print('C. Humanas: {}'.format(round(notacompesohum4, 2)))
    print('Redação: {}'.format(round(notacompesored4, 2)))
    
    mediafinal = ((notacompesoling4+notacompesohum4+notacompesonatu4+notacompesomat4+notacompesored4)/10)
    print('\nA sua média final é de {}'.format(round(mediafinal, 2)))
  
 else:
    print('Você não inseriu uma resposta válida.')

elif cursoinserido in grupo1:
    
    notacompesoling1=(pesoling1*nota_linguagens)
    notacompesohum1=(pesohum1*nota_humanas)
    notacompesonatu1=(pesonatu1*nota_natureza)
    notacompesomat1=(pesomat1*nota_matematica)
    notacompesored1=(pesored1*nota_redacao)
    
    print('\nSegundo a divisão oficial da UFG, seu curso está contido no GRUPO 1.')
    print('\nNOTAS COM PESO DO GRUPO 1')
    print('\nLinguagens: {}'.format(round(notacompesoling1, 2)))
    print('Matemática: {}'.format(round(notacompesomat1, 2)))
    print('C. Natureza: {}'.format(round(notacompesonatu1, 2)))
    print('C. Humanas: {}'.format(round(notacompesohum1, 2)))
    print('Redação: {}'.format(round(notacompesored1, 2)))
    
    mediafinal = ((notacompesoling1+notacompesohum1+notacompesonatu1+notacompesomat1+notacompesored1)/10)
    print('\nA sua média final é de {}'.format(round(mediafinal, 2)))

elif cursoinserido in grupo2:

    notacompesoling2=(pesoling2*nota_linguagens)
    notacompesohum2=(pesohum2*nota_humanas)
    notacompesonatu2=(pesonatu2*nota_natureza)
    notacompesomat2=(pesomat2*nota_matematica)
    notacompesored2=(pesored2*nota_redacao)

    print('Segundo a divisão oficial da UFG, seu curso está contido no GRUPO 2.')
    print('\nNOTAS COM PESO DO GRUPO 2')
    print('\nLinguagens: {}'.format(round(notacompesoling2, 2)))
    print('Matemática: {}'.format(round(notacompesomat2, 2)))
    print('C. Natureza: {}'.format(round(notacompesonatu2, 2)))
    print('C. Humanas: {}'.format(round(notacompesohum2, 2)))
    print('Redação: {}'.format(round(notacompesored2, 2)))
    
    mediafinal = ((notacompesoling2+notacompesohum2+notacompesonatu2+notacompesomat2+notacompesored2)/10)
    print('\nA sua média final é de {}'.format(round(mediafinal, 2)))

elif cursoinserido in grupo3:

    notacompesoling3=(pesoling3*nota_linguagens)
    notacompesohum3=(pesohum3*nota_humanas)
    notacompesonatu3=(pesonatu3*nota_natureza)
    notacompesomat3=(pesomat3*nota_matematica)
    notacompesored3=(pesored3*nota_redacao)

    print('Segundo a divisão oficial da UFG, seu curso está contido no GRUPO 3.')
    print('\nNOTAS COM PESO DO GRUPO 3')
    print('\nLinguagens: {}'.format(round(notacompesoling3, 2)))
    print('Matemática: {}'.format(round(notacompesomat3, 2)))
    print('C. Natureza: {}'.format(round(notacompesonatu3, 2)))
    print('C. Humanas: {}'.format(round(notacompesohum3, 2)))
    print('Redação: {}'.format(round(notacompesored3, 2)))
    
    mediafinal = ((notacompesoling3+notacompesohum3+notacompesonatu3+notacompesomat3+notacompesored3)/10)
    print('\nA sua média final é de {}'.format(round(mediafinal, 2)))

elif cursoinserido in grupo4:

    notacompesoling4=(pesoling4*nota_linguagens)
    notacompesohum4=(pesohum4*nota_humanas)
    notacompesonatu4=(pesonatu4*nota_natureza)
    notacompesomat4=(pesomat4*nota_matematica)
    notacompesored4=(pesored4*nota_redacao)

    print('Segundo a divisão oficial da UFG, seu curso está contido no GRUPO 4.')
    print('\nNOTAS COM PESO DO GRUPO 4')
    print('\nLinguagens: {}'.format(round(notacompesoling4, 2)))
    print('Matemática: {}'.format(round(notacompesomat4, 2)))
    print('C. Natureza: {}'.format(round(notacompesonatu4, 2)))
    print('C. Humanas: {}'.format(round(notacompesohum4, 2)))
    print('Redação: {}'.format(round(notacompesored4, 2)))
    
    mediafinal = ((notacompesoling4+notacompesohum4+notacompesonatu4+notacompesomat4+notacompesored4)/10)
    print('\nA sua média final é de {}'.format(round(mediafinal, 2)))

elif cursoinserido in grupo5:

    notacompesoling5=(pesoling5*nota_linguagens)
    notacompesohum5=(pesohum5*nota_humanas)
    notacompesonatu5=(pesonatu5*nota_natureza)
    notacompesomat5=(pesomat5*nota_matematica)
    notacompesored5=(pesored5*nota_redacao)

    print('Segundo a divisão oficial da UFG, seu curso está contido no GRUPO 5.')
    print('\nNOTAS COM PESO DO GRUPO 5')
    print('\nLinguagens: {}'.format(round(notacompesoling5, 2)))
    print('Matemática: {}'.format(round(notacompesomat5, 2)))
    print('C. Natureza: {}'.format(round(notacompesonatu5, 2)))
    print('C. Humanas: {}'.format(round(notacompesohum5, 2)))
    print('Redação: {}'.format(round(notacompesored5, 2)))
    
    mediafinal = ((notacompesoling5+notacompesohum5+notacompesonatu5+notacompesomat5+notacompesored5)/10)
    print('\nA sua média final é de {}'.format(round(mediafinal, 2)))

elif cursoinserido in grupo6:

    notacompesoling6=(pesoling6*nota_linguagens)
    notacompesohum6=(pesohum6*nota_humanas)
    notacompesonatu6=(pesonatu6*nota_natureza)
    notacompesomat6=(pesomat6*nota_matematica)
    notacompesored6=(pesored6*nota_redacao)

    print('Segundo a divisão oficial da UFG, seu curso está contido no GRUPO 2.')
    print('\nNOTAS COM PESO DO GRUPO 2')
    print('\nLinguagens: {}'.format(round(notacompesoling6, 2)))
    print('Matemática: {}'.format(round(notacompesomat6, 2)))
    print('C. Natureza: {}'.format(round(notacompesonatu6, 2)))
    print('C. Humanas: {}'.format(round(notacompesohum6, 2)))
    print('Redação: {}'.format(round(notacompesored6, 2)))
    
    mediafinal = ((notacompesoling6+notacompesohum6+notacompesonatu6+notacompesomat6+notacompesored6)/10)
    print('\nA sua média final é de {}'.format(round(mediafinal, 2)))

elif cursoinserido in grupo7:

    notacompesoling7=(pesoling7*nota_linguagens)
    notacompesohum7=(pesohum7*nota_humanas)
    notacompesonatu7=(pesonatu7*nota_natureza)
    notacompesomat7=(pesomat7*nota_matematica)
    notacompesored7=(pesored7*nota_redacao)

    print('Segundo a divisão oficial da UFG, seu curso está contido no GRUPO 7.')
    print('\nNOTAS COM PESO DO GRUPO 7')
    print('\nLinguagens: {}'.format(round(notacompesoling7, 2)))
    print('Matemática: {}'.format(round(notacompesomat7, 2)))
    print('C. Natureza: {}'.format(round(notacompesonatu7, 2)))
    print('C. Humanas: {}'.format(round(notacompesohum7, 2)))
    print('Redação: {}'.format(round(notacompesored7, 2)))
    
    mediafinal = ((notacompesoling7+notacompesohum7+notacompesonatu7+notacompesomat7+notacompesored7)/10)
    print('\nA sua média final é de {}'.format(round(mediafinal, 2)))

elif cursoinserido in grupo8:

    notacompesoling8=(pesoling8*nota_linguagens)
    notacompesohum8=(pesohum8*nota_humanas)
    notacompesonatu8=(pesonatu8*nota_natureza)
    notacompesomat8=(pesomat8*nota_matematica)
    notacompesored8=(pesored8*nota_redacao)

    print('Segundo a divisão oficial da UFG, seu curso está contido no GRUPO 8.')
    print('\nNOTAS COM PESO DO GRUPO 8')
    print('\nLinguagens: {}'.format(round(notacompesoling8, 2)))
    print('Matemática: {}'.format(round(notacompesomat8, 2)))
    print('C. Natureza: {}'.format(round(notacompesonatu8, 2)))
    print('C. Humanas: {}'.format(round(notacompesohum8, 2)))
    print('Redação: {}'.format(round(notacompesored8, 2)))
    
    mediafinal = ((notacompesoling8+notacompesohum8+notacompesonatu8+notacompesomat8+notacompesored8)/10)
    print('\nA sua média final é de {}'.format(round(mediafinal, 2)))




