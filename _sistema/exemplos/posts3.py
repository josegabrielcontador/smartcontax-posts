from helpers import *

POSTS = [

car("2026-12-05", "erros-nota-servico", [
    C("Erros fiscais", "5 erros na *nota fiscal de serviço* que geram problema", "A nota é a principal prova da receita da empresa.", "Confira se a sua clínica comete algum"),
    S("01", "Código de serviço *errado*", [("O risco", "Alíquota de ISS incorreta e informação divergente para o fisco."), ("O jeito certo", "Use o código que corresponde ao serviço efetivamente prestado.")]),
    S("02", "Nota *sem dados* do tomador", [("O risco", "Dificulta a comprovação da receita e a dedução pelo paciente no Imposto de Renda."), ("O jeito certo", "Informe nome e CPF ou CNPJ de quem pagou.")]),
    S("03", "Valor *diferente* do recebido", [("O risco", "Receita declarada diferente do que entrou na conta."), ("O jeito certo", "A nota deve refletir o valor efetivamente cobrado.")]),
    S("04", "Emitir *depois* do mês", [("O risco", "Receita lançada na competência errada, com reflexo no imposto apurado."), ("O jeito certo", "Emita a nota no mês em que o serviço foi prestado.")]),
    S("05", "Deixar de *emitir*", [("O risco", "Omissão de receita, uma das infrações mais autuadas, hoje cruzada com dados de cartão e PIX."), ("O jeito certo", "Toda prestação de serviço deve ter nota.")], box="A Receita cruza notas emitidas com recebimentos de cartão e PIX informados pelas instituições financeiras."),
    A("Nota correta é proteção", "Revise como a sua clínica emite notas antes que a fiscalização faça isso.", "Envie para quem emite as notas"),
], """
A nota fiscal de serviço é a principal prova da receita da sua empresa, e pequenos erros na emissão geram problemas grandes.

Os cinco mais comuns: código de serviço errado, nota sem os dados do tomador, valor diferente do recebido, emissão fora do mês da prestação e, o mais grave, deixar de emitir. A Receita cruza as notas com os recebimentos de cartão e PIX informados pelas instituições financeiras.

Revise o processo de emissão da sua clínica.

Salve e envie para quem emite as notas.

#notafiscal #nfse #clinicas #omissaodereceita #contabilidade
"""),

img("2026-12-06", "faturamento-2026-define-2027", {
    "theme": "navy", "kicker": "Planejamento 2027",
    "title": "O faturamento de *2026* influencia o imposto de *2027*",
    "text": "No Simples, a alíquota considera a receita dos últimos 12 meses. Para confirmar o regime de 2027 e planejar 2028, os números de 2026 são o ponto de partida.",
    "box": "Simulação feita com números antigos leva a decisões erradas.",
}, """
O planejamento tributário de 2027 começa pelos números de 2026.

No Simples Nacional, a alíquota efetiva é calculada sobre a receita bruta dos últimos 12 meses. No Presumido e no Real, a comparação depende de faturamento, margem e folha. Em todos os casos, o ano que está terminando é a base da projeção.

Por isso, a contabilidade de 2026 precisa estar em dia agora, e não em março.

Salve e compartilhe com o seu sócio.

#planejamentotributario #simplesnacional #regimetributario #contabilidade
"""),

car("2026-12-07", "simples-x-presumido-clinica", [
    C("Regime tributário", "Simples ou Presumido para a *clínica*?", "Não existe regime melhor. Existe o regime certo para os seus números.", "As 4 variáveis que decidem"),
    S("01", "Faturamento", ["No Simples, a alíquota sobe conforme a receita dos últimos 12 meses.", "No Presumido, os percentuais de presunção são fixos, com adicional de IR acima de determinado lucro presumido."]),
    S("02", "Folha e *Fator R*", ["No Simples, a folha pode levar a atividade do Anexo V para o III.", "No Presumido, a empresa recolhe 20% de contribuição previdenciária sobre folha e pró-labore."]),
    S("03", "Equiparação *hospitalar*", ["Clínicas que se enquadram podem reduzir a base de IRPJ e CSLL no Presumido.", "Esse benefício não existe dentro do Simples."]),
    S("04", "Reforma *Tributária*", ["A partir de 2027, a CBS muda o cálculo no Presumido e a forma como os créditos funcionam.", "A comparação feita em anos anteriores precisa ser refeita."], box="A decisão certa sai de uma simulação com os números reais da clínica, nos dois regimes."),
    A("Refaça a conta com antecedência", "A opção pelo Simples agora é feita em setembro, para o ano seguinte. A simulação precisa estar pronta antes disso.", "Envie para o sócio da clínica"),
], """
Simples ou Presumido? A resposta muda de clínica para clínica.

Quatro variáveis decidem: faturamento, peso da folha e Fator R, possibilidade de equiparação hospitalar e os efeitos da Reforma Tributária a partir de 2027. Uma clínica com folha baixa pode ir para o Anexo V do Simples. Outra, com procedimentos que se enquadram na equiparação hospitalar, pode ter vantagem no Presumido.

Com a CBS em 2027, comparações feitas em anos anteriores precisam ser refeitas. E atenção ao calendário: desde a LC 214/2025, a opção pelo Simples é feita em setembro, para valer no ano seguinte.

Salve e compartilhe com o sócio da clínica.

#simplesnacional #lucropresumido #clinicas #regimetributario #planejamentotributario
"""),

car("2026-12-08", "ferias-coletivas", [
    C("Departamento pessoal", "Férias coletivas no *fim de ano*: as regras", "Muitas clínicas e lojas fecham entre o Natal e o Ano Novo.", "O que é preciso fazer antes"),
    S("01", "Comunicação", ["A CLT exige comunicar o órgão do Ministério do Trabalho e o sindicato com pelo menos 15 dias de antecedência, além de avisar os funcionários.", "Microempresas e empresas de pequeno porte são dispensadas da comunicação ao Ministério."]),
    S("02", "Duração", ["As férias coletivas podem ser divididas em até dois períodos no ano.", "Nenhum deles pode ser inferior a 10 dias corridos."]),
    S("03", "Pagamento", ["Férias e o adicional de 1/3 devem ser pagos até 2 dias antes do início do período."]),
    S("04", "Funcionário *recente*", ["Quem tem menos de 12 meses de empresa tira férias proporcionais e começa um novo período aquisitivo."], box="Para fechar a partir de 23/12, a comunicação precisa ser feita até hoje."),
    A("Planeje o recesso com antecedência", "Férias coletivas mal comunicadas podem ser questionadas depois.", "Envie para quem cuida da folha"),
], """
Se a sua empresa vai fechar entre o Natal e o Ano Novo, as férias coletivas precisam seguir as regras da CLT.

A comunicação ao órgão do Ministério do Trabalho e ao sindicato deve ser feita com pelo menos 15 dias de antecedência, além do aviso aos funcionários. Microempresas e empresas de pequeno porte estão dispensadas da comunicação ao Ministério. As férias podem ser divididas em até dois períodos, nenhum menor que 10 dias, e devem ser pagas com o adicional de 1/3 até 2 dias antes do início.

Para fechar a partir de 23/12, o prazo de comunicação termina hoje.

Salve e envie para quem cuida da folha.

#feriascoletivas #departamentopessoal #clt #gestaodepessoas #contabilidade
"""),

img("2026-12-09", "alerta-13-segunda", {
    "theme": "navy", "kicker": "Alerta de prazo", "big": "18/12", "bigsize": 230,
    "title": "Pague a *2ª parcela* do 13º até sexta-feira",
    "text": "O prazo legal é 20/12, mas em 2026 a data cai em um domingo. Na 2ª parcela são descontados INSS e IR.",
    "foot": "Lei 4.749/1965",
}, """
A 2ª parcela do 13º salário tem prazo legal em 20 de dezembro. Em 2026, essa data cai em um domingo, então o pagamento deve ser feito até sexta-feira, 18/12.

É nesta parcela que são descontados INSS e Imposto de Renda, calculados sobre o valor total do 13º. Separe também o FGTS e os encargos no caixa.

Salve e compartilhe com quem cuida do financeiro.

#13salario #departamentopessoal #prazos #contabilidade
"""),

car("2026-12-10", "split-payment", [
    C("Reforma Tributária", "Split payment: o imposto *separado* no pagamento", "Uma das mudanças que mais vão afetar o caixa das empresas.", "Entenda em 4 pontos"),
    S("01", "O que é", ["Um mecanismo previsto na LC 214/2025 em que o IBS e a CBS são separados no momento do pagamento da venda.", "O valor do tributo vai direto para o fisco, sem passar pela conta da empresa."]),
    S("02", "Como *funciona*", ["Quando o cliente paga por cartão, PIX ou boleto, o sistema de pagamento separa a parte do tributo.", "A empresa recebe o valor líquido."]),
    S("03", "O efeito no *caixa*", ["Hoje, muitas empresas usam o imposto recebido como capital de giro até o vencimento da guia.", "Com o split payment, esse dinheiro deixa de passar pelo caixa."]),
    S("04", "Quando *começa*", ["A implantação será gradual e ainda depende de regulamentação e de adaptação dos sistemas de pagamento."], box="O momento de rever o capital de giro é antes do split payment começar, não depois."),
    A("Prepare o caixa para a mudança", "Empresas que dependem do imposto como capital de giro são as mais afetadas.", "Envie para quem cuida do financeiro"),
], """
O split payment é um dos pontos da Reforma Tributária com maior impacto no caixa das empresas.

Previsto na LC 214/2025, ele separa o IBS e a CBS no momento do pagamento da venda: o tributo vai direto para o fisco e a empresa recebe o valor líquido. Para quem usa o imposto recebido como capital de giro até o vencimento da guia, isso muda a dinâmica do caixa.

A implantação será gradual e ainda depende de regulamentação, mas o planejamento do capital de giro precisa começar antes.

Salve e compartilhe com quem cuida do financeiro.

#splitpayment #reformatributaria #fluxodecaixa #ibs #cbs
"""),

car("2026-12-11", "irpf-socio-organizar", [
    C("Imposto de Renda", "Sócio: comece a organizar o *IR de 2027* agora", "A declaração de 2027 se refere ao que aconteceu em 2026.", "O que separar ainda em dezembro"),
    S("01", "Informes da *empresa*", ["Pró-labore e lucros distribuídos em 2026, com os valores de IR retido.", "Peça ao contador o informe de rendimentos da empresa."]),
    S("02", "Bens e *investimentos*", ["Compras e vendas de imóveis, veículos e participações.", "Informes de bancos e corretoras."]),
    S("03", "Despesas *dedutíveis*", ["Saúde, educação, previdência privada PGBL e dependentes.", "Guarde recibos e notas com CPF."]),
    S("04", "Renda *alta*", ["Com a Lei 15.270/2025, rendas totais acima de R$ 600 mil no ano passam a ter imposto mínimo.", "Lucros recebidos em 2026 entram nessa conta."], box="Declaração feita com pressa no último mês tem mais chance de cair na malha."),
    A("Organize antes do prazo", "Quanto antes os documentos estiverem reunidos, mais tempo para revisar com calma.", "Envie para o seu sócio"),
], """
A declaração de Imposto de Renda de 2027 se refere ao ano de 2026, e o sócio que organiza tudo em dezembro declara com mais segurança.

Separe os informes de pró-labore e lucros recebidos da empresa, os informes de bancos e corretoras, as compras e vendas de bens e as despesas dedutíveis com saúde, educação e previdência. Para rendas totais acima de R$ 600 mil no ano, a Lei 15.270/2025 criou o imposto mínimo, e os lucros recebidos entram nessa conta.

Salve e compartilhe com o seu sócio.

#impostoderenda #irpf #socios #distribuicaodelucros #contabilidade
"""),

img("2026-12-12", "o-que-e-pro-labore", {
    "theme": "white", "kicker": "Em uma frase",
    "title": "O que é *pró-labore*?",
    "text": "É a remuneração que o sócio recebe pelo trabalho que exerce na empresa, com recolhimento de INSS e Imposto de Renda.",
    "box": "Pró-labore remunera o trabalho. Distribuição de lucros remunera o investimento.",
}, """
Pró-labore é a remuneração do sócio pelo trabalho que ele exerce na empresa.

Sobre ele incidem INSS e Imposto de Renda. É diferente da distribuição de lucros, que remunera o investimento do sócio e depende do resultado apurado.

Todo sócio que trabalha na empresa deve ter pró-labore definido.

Salve e compartilhe com quem está abrindo uma empresa.

#prolabore #socios #contabilidade #empreendedorismo
"""),

car("2026-12-13", "carga-efetiva", [
    C("Gestão tributária", "Quanto sua empresa *pagou de imposto* em 2026?", "Saber esse número é o primeiro passo para avaliar se ele está correto.", "Como calcular a carga efetiva"),
    S("01", "Some todos os *tributos*", ["Impostos sobre a receita, como DAS, ISS, ICMS, PIS, Cofins, IRPJ e CSLL.", "Encargos sobre a folha, como INSS patronal e FGTS."]),
    S("02", "Divida pelo *faturamento*", ["Total de tributos do ano dividido pela receita bruta do ano.", "O resultado é a carga tributária efetiva, em percentual."]),
    S("03", "Compare com o *esperado*", ["O percentual é compatível com o regime e com a atividade?", "Variações grandes de um ano para o outro precisam de explicação."]),
    S("04", "Use para *decidir*", ["É com esse número que se compara regimes, se avalia preço e se projeta o ano seguinte."], box="Se ninguém consegue te dizer esse percentual, a empresa está sem uma informação básica de gestão."),
    A("Peça esse número ao seu contador", "Carga tributária efetiva é o ponto de partida de qualquer planejamento.", "Envie para o seu sócio"),
], """
Você sabe qual percentual do faturamento da sua empresa foi para impostos em 2026?

A conta é simples: some todos os tributos pagos no ano, sobre a receita e sobre a folha, e divida pela receita bruta. O resultado é a carga tributária efetiva. É com ele que se compara regimes, se avalia preço e se projeta o ano seguinte.

Se ninguém consegue te informar esse número, comece por ele.

Salve e compartilhe com o seu sócio.

#cargatributaria #planejamentotributario #gestaoempresarial #contabilidade
"""),

car("2026-12-14", "ncm-errado", [
    C("Comércio", "NCM errado: um código que *custa caro*", "A classificação fiscal do produto define o imposto que você paga.", "4 efeitos de uma classificação incorreta"),
    S("01", "ICMS-ST *indevido*", ["Produto classificado como sujeito à substituição tributária sem estar.", "Ou o contrário: ST que deveria ser recolhida e não foi."]),
    S("02", "PIS e Cofins *em dobro*", ["No Simples, produtos monofásicos devem ser segregados no DAS.", "Com o NCM errado, a empresa paga de novo um tributo que já foi recolhido pelo fabricante."]),
    S("03", "Reforma *Tributária*", ["O NCM também define reduções e regimes específicos de IBS e CBS.", "Cadastro errado em 2027 significa imposto errado na nota."]),
    S("04", "Fiscalização", ["Divergências entre o cadastro da empresa e o do fornecedor são cruzadas pelos sistemas do fisco."], box="Revisar o cadastro fiscal de produtos é uma das ações com retorno mais rápido para o comércio."),
    A("Revise o cadastro antes de 2027", "Comece pelos produtos de maior volume de venda.", "Envie para o dono da loja"),
], """
O NCM é o código de classificação fiscal do produto, e ele define boa parte do imposto que o comércio paga.

Com o NCM errado, a empresa pode recolher ICMS-ST indevido, deixar de recolher o que devia, ou pagar PIS e Cofins de novo sobre produtos monofásicos no Simples. A partir de 2027, o NCM também define reduções e regimes específicos de IBS e CBS.

Revisar o cadastro fiscal de produtos é uma das ações com retorno mais rápido para o comércio. Comece pelos itens de maior venda.

Salve e envie para o dono da loja.

#ncm #comercio #icmsst #monofasico #reformatributaria
"""),

car("2026-12-15", "kpis-clinica", [
    C("Gestão de clínicas", "5 indicadores que toda clínica deveria *acompanhar*", "Faturamento sozinho não mostra se a clínica está saudável.", "Acompanhe mensalmente"),
    S("01", "Ticket *médio*", ["Faturamento dividido pelo número de pacientes atendidos.", "Mostra quanto cada paciente gera, em média."]),
    S("02", "Ocupação da *agenda*", ["Horas atendidas divididas pelas horas disponíveis.", "Agenda com muitas lacunas é custo fixo sem receita."]),
    S("03", "Inadimplência", ["Valores vencidos e não recebidos, em percentual do faturamento.", "Inclui parcelamentos próprios e glosas de convênios."]),
    S("04", "Custo *fixo* sobre receita", ["Quanto da receita é consumido por aluguel, folha e estrutura.", "Ajuda a entender o quanto a clínica depende de volume."]),
    S("05", "Margem *líquida*", ["O que sobra depois de todos os custos e impostos, em percentual do faturamento."], box="Indicador só tem valor quando é comparado: com o mês anterior, com a meta e com o mesmo mês do ano passado."),
    A("Comece com esses cinco", "Uma planilha simples, atualizada todo mês, já muda a qualidade das decisões.", "Envie para o sócio da clínica"),
], """
Faturamento alto não garante uma clínica saudável. Cinco indicadores mostram muito mais.

Ticket médio, ocupação da agenda, inadimplência, custo fixo sobre a receita e margem líquida. Juntos, eles respondem se a clínica atende bem, ocupa bem a estrutura, recebe o que vende e transforma faturamento em lucro.

O valor está na comparação mês a mês e com a meta.

Salve e compartilhe com o sócio da clínica.

#gestaodeclinicas #indicadores #kpi #clinicaodontologica #gestaofinanceira
"""),

img("2026-12-16", "mito-cnpj-sempre-paga-menos", {
    "theme": "light", "chip": "Mito", "chipbg": "#B3261E",
    "title": "“Abrir CNPJ *sempre* paga menos imposto que atuar como pessoa física.”",
    "text": "Na maioria dos casos de renda mais alta, a empresa reduz a carga. Mas não em todos: depende do faturamento, das despesas e do regime.",
    "box": "A decisão certa vem de uma simulação comparando os dois cenários.",
}, """
Abrir empresa costuma reduzir o imposto do profissional liberal, mas não é regra para todos os casos.

Com faturamento baixo, muitas despesas dedutíveis no livro-caixa ou atividade que cairia no Anexo V do Simples, a diferença pode ser pequena ou até desfavorável depois de somar contabilidade, taxas e obrigações.

A resposta vem de uma simulação com os seus números.

Salve e envie para um colega que está pensando em abrir empresa.

#pessoajuridica #profissionalliberal #planejamentotributario #contabilidade
"""),

car("2026-12-17", "dentista-pf-x-pj", [
    C("Profissional de saúde", "Quando o dentista deve *abrir empresa*?", "Atender como pessoa física ou como pessoa jurídica tem custos diferentes.", "Como comparar os dois cenários"),
    S("01", "Como *pessoa física*", ["Imposto de Renda pelo carnê-leão, com alíquota que pode chegar a 27,5%.", "INSS de autônomo, limitado ao teto, e possibilidade de deduzir despesas pelo livro-caixa."]),
    S("02", "Como *empresa*", ["No Simples, a odontologia está sujeita ao Fator R, com alíquota inicial de 6% no Anexo III ou de 15,5% no Anexo V.", "Também é possível o Lucro Presumido."]),
    S("03", "Custos *além* do imposto", ["Abertura, contabilidade mensal, certificado digital, alvarás e taxas do conselho para a pessoa jurídica."]),
    S("04", "Outros *fatores*", ["Clínicas e convênios que só contratam pessoa jurídica.", "Planos de crescimento, como contratar outros profissionais."], box="Compare o líquido final nos dois cenários, depois de todos os impostos e custos."),
    A("Faça a conta com seus números", "O ponto de virada muda conforme faturamento, despesas e forma de atuação.", "Envie para um colega dentista"),
], """
Atender como pessoa física ou abrir empresa? Para o dentista, a resposta depende de números.

Como pessoa física, o IR pelo carnê-leão pode chegar a 27,5%, além do INSS de autônomo. Como empresa, no Simples a odontologia está sujeita ao Fator R, com alíquota inicial de 6% no Anexo III ou 15,5% no Anexo V. Também há o Lucro Presumido. Do lado da empresa, entram custos de contabilidade, taxas e obrigações.

A comparação certa olha o valor líquido final nos dois cenários.

Salve e envie para um colega dentista.

#dentista #contabilidadeparadentistas #pessoajuridica #carneleao #simplesnacional
"""),

img("2026-12-18", "alerta-13-hoje-segunda", {
    "theme": "orange", "kicker": "Vence hoje", "big": "HOJE", "bigsize": 220,
    "title": "Último dia útil para a *2ª parcela* do 13º",
    "text": "O prazo legal é 20/12, que em 2026 cai em um domingo. Não deixe para segunda-feira.",
}, """
Hoje é o último dia útil para pagar a 2ª parcela do 13º salário.

O prazo legal é 20 de dezembro, mas a data cai em um domingo. Pagar na segunda-feira, dia 21, significa pagar em atraso.

Na 2ª parcela são descontados INSS e IR. Confira os valores e regularize hoje.

Compartilhe com quem cuida da folha.

#13salario #departamentopessoal #prazos #contabilidade
"""),

car("2026-12-19", "sistema-notas-2027", [
    C("Reforma Tributária", "Seu sistema de notas está pronto para *2027*?", "Nota fiscal com IBS e CBS errados vira problema desde o primeiro dia.", "O que perguntar ao fornecedor do sistema"),
    S("01", "Campos de *IBS e CBS*", ["O sistema já preenche os grupos de IBS e CBS na NF-e, na NFC-e e na NFS-e?"]),
    S("02", "Classificação *tributária*", ["Cada item ou serviço precisa ter CST e código de classificação tributária (cClassTrib) corretos.", "Quem define o código para cada produto ou serviço?"]),
    S("03", "Cadastro de *produtos*", ["O NCM e a NBS dos itens estão revisados?", "Eles definem reduções e regimes específicos."]),
    S("04", "Testes", ["Peça para emitir notas de teste e confira o XML com o seu contador antes de janeiro."], box="Não presuma que o sistema foi atualizado. Peça a confirmação por escrito."),
    A("Valide antes da virada", "Em 2027 a CBS passa a ser cobrada. Nota errada significa imposto errado.", "Envie para quem emite as notas"),
], """
Em 2027 a CBS passa a ser cobrada de verdade, e a nota fiscal é onde tudo começa.

Pergunte ao fornecedor do seu sistema: os campos de IBS e CBS já são preenchidos na NF-e, na NFC-e e na NFS-e? Cada item tem CST e cClassTrib corretos? Quem define esse código? O NCM e a NBS dos produtos e serviços estão revisados?

Peça notas de teste e confira o XML com o seu contador antes de janeiro. E peça a confirmação por escrito.

Salve e envie para quem emite as notas.

#reformatributaria #notafiscal #cclasstrib #ibs #cbs
"""),

]
