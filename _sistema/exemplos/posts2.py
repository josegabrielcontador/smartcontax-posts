from helpers import *

POSTS = [

img("2026-11-20", "feriado-trabalho-em-dobro", {
    "theme": "light", "kicker": "Feriado nacional",
    "title": "Funcionou no *feriado*? Confira a regra",
    "text": "O trabalho em feriado sem folga compensatória em outro dia deve ser pago em dobro, conforme a Lei 605/1949.",
    "box": "Antes de escalar a equipe, verifique também o que diz a convenção coletiva da sua categoria.",
}, """
Hoje é feriado nacional da Consciência Negra.

Se a sua clínica ou loja funciona hoje, a regra é clara: o trabalho em feriado sem folga compensatória em outro dia deve ser pago em dobro, conforme a Lei 605/1949. A convenção coletiva da categoria pode trazer regras adicionais, por isso vale conferir antes de montar a escala.

Salve e compartilhe com quem cuida da escala da equipe.

#departamentopessoal #feriado #legislacaotrabalhista #gestaodepessoas
"""),

car("2026-11-21", "black-friday-descontos", [
    C("Comércio", "Desconto na *Black Friday*: a forma muda o imposto", "Nem todo desconto reduz a base de cálculo dos tributos.", "A diferença entre condicional e incondicional"),
    S("01", "Desconto *incondicional*", [("O que é", "O desconto dado no ato da venda, destacado na própria nota fiscal, sem depender de nenhuma condição futura."), ("Efeito", "Reduz a receita bruta e a base dos tributos sobre a venda.")]),
    S("02", "Desconto *condicional*", [("O que é", "O desconto que depende de um evento posterior, como pagamento antecipado de uma parcela."), ("Efeito", "Não reduz a base dos tributos sobre a venda. É tratado como despesa financeira.")]),
    S("03", "O erro *comum*", ["Vender com preço cheio na nota e conceder o desconto por fora, no caixa ou no recebimento.", "Nesse caso, o imposto é calculado sobre um valor que você não recebeu."]),
    S("04", "O jeito certo", ["Configure o sistema para destacar o desconto na nota fiscal.", "Confira se o cupom ou a NF-e mostra o valor cheio, o desconto e o valor final."], box="Desconto incondicional mal registrado faz a empresa pagar imposto sobre uma receita que não existiu."),
    A("Promoção sem imposto a mais", "Revise a configuração do seu sistema antes de 27/11.", "Envie para quem emite as notas da loja"),
], """
Na Black Friday, a forma como o desconto aparece na nota fiscal muda o imposto que você paga.

Desconto incondicional, dado no ato da venda e destacado na nota, reduz a receita bruta e a base de cálculo. Desconto condicional, que depende de um evento futuro, não reduz a base e é tratado como despesa financeira.

O erro mais comum é emitir a nota com o preço cheio e dar o desconto no caixa. Assim, o imposto é calculado sobre um valor que a loja não recebeu.

Salve e envie para quem emite as notas antes do dia 27.

#blackfriday #comercio #notafiscal #descontoincondicional #contabilidade
"""),

car("2026-11-22", "4-numeros-semana", [
    C("Gestão financeira", "4 números que o dono deve olhar *toda semana*", "Não é preciso ser financeiro para acompanhar o essencial.", "Leva menos de 15 minutos"),
    S("01", "Saldo de *caixa*", ["Quanto há disponível hoje em todas as contas da empresa.", "Compare com o da semana anterior para entender a tendência."]),
    S("02", "Contas a *receber*", ["O que já foi vendido e ainda não entrou: cartão a receber, boletos, convênios e parcelamentos."]),
    S("03", "Contas a *pagar*", ["O que vence nos próximos 30 dias: folha, impostos, fornecedores e aluguel.", "Janeiro concentra os impostos sobre o faturamento de dezembro."]),
    S("04", "Faturamento *acumulado*", ["Quanto a empresa faturou no mês até agora, comparado com a meta e com o mesmo período do mês anterior."], box="Saldo + a receber − a pagar mostra se a empresa fecha o mês no positivo. Esse é o número que evita susto."),
    A("Gestão começa por rotina", "Escolha um dia fixo da semana e reserve 15 minutos para esses quatro números.", "Envie para quem cuida do financeiro"),
], """
Você não precisa de um relatório de 20 páginas para saber como a empresa está. Quatro números, olhados toda semana, resolvem a maior parte das decisões do dia a dia.

Saldo de caixa, contas a receber, contas a pagar nos próximos 30 dias e faturamento acumulado do mês. Com esses quatro, você sabe se fecha o mês no positivo e tem tempo de agir se não fechar.

Em janeiro isso é ainda mais importante, porque os impostos sobre o faturamento de dezembro vencem agora.

Salve e reserve 15 minutos fixos na sua semana.

#gestaofinanceira #fluxodecaixa #empreendedorismo #gestaoempresarial #contabilidade
"""),

car("2026-11-23", "credito-ibs-cbs", [
    C("Reforma Tributária", "Crédito de IBS e CBS: o que muda na *conta*", "A Reforma amplia a não cumulatividade. Entenda o que isso significa.", "Explicado com um exemplo simples"),
    S("01", "Como é *hoje*", ["Empresas no Lucro Presumido pagam PIS e Cofins no regime cumulativo, com 3,65% sobre a receita e sem direito a crédito sobre compras."]),
    S("02", "Como *fica*", ["Com a CBS e o IBS, a regra geral é a não cumulatividade ampla.", "O imposto pago nas compras vira crédito para abater o imposto devido nas vendas, com exceções previstas em lei."]),
    S("03", "Um *exemplo*", ["A empresa compra R$ 1.000 em insumos com R$ 100 de tributo destacado e vende por R$ 2.000 com R$ 200 de tributo.", "Ela recolhe a diferença: R$ 100."]),
    S("04", "O que isso *exige*", ["Fornecedores regulares e notas fiscais corretas.", "Controle das compras que geram crédito e das que não geram."], box="Valores ilustrativos. As alíquotas de referência ainda serão definidas, e o crédito depende do pagamento do tributo pelo fornecedor."),
    A("Fornecedor passa a pesar no imposto", "Comprar de quem não destaca o tributo corretamente pode significar perder crédito a partir de 2027.", "Envie para quem cuida das compras"),
], """
Uma das mudanças mais relevantes da Reforma Tributária é a não cumulatividade ampla.

Hoje, empresas no Lucro Presumido pagam PIS e Cofins sobre a receita, sem crédito nas compras. Com CBS e IBS, a regra geral passa a ser outra: o tributo pago nas compras vira crédito para abater o tributo devido nas vendas, com exceções previstas em lei.

Isso muda a importância do fornecedor. Comprar de quem não emite nota correta ou não recolhe o tributo pode significar perder crédito.

Os valores do exemplo são ilustrativos. Salve e envie para quem cuida das compras da empresa.

#reformatributaria #ibs #cbs #naocumulatividade #contabilidade
"""),

car("2026-11-24", "dentista-clt-autonomo-socio", [
    C("Gestão de clínicas", "Dentista na equipe: *CLT, autônomo ou sócio*?", "Cada formato tem custo e risco diferentes.", "Compare antes de contratar"),
    S("01", "CLT", [("Quando faz sentido", "Profissional com horário fixo, rotina definida pela clínica e subordinação direta."), ("Atenção", "Maior custo de encargos, mas menor risco trabalhista.")]),
    S("02", "Autônomo ou PJ", [("Quando faz sentido", "Profissional com autonomia real de agenda, que atende em vários lugares e assume os próprios custos."), ("Atenção", "Se houver subordinação, horário imposto e habitualidade, a relação pode ser reconhecida como vínculo de emprego.")]),
    S("03", "Sócio", [("Quando faz sentido", "Profissional que participa do risco e do resultado da clínica."), ("Atenção", "Exige contrato social bem redigido e regras claras de entrada, saída e divisão de lucros.")]),
    S("04", "O que *decide*", ["Não é o contrato que define a relação, é a forma como ela acontece na prática.", "Os requisitos do vínculo estão no artigo 3º da CLT: pessoalidade, habitualidade, onerosidade e subordinação."], box="Formalize por escrito e garanta que a rotina corresponde ao que está no contrato."),
    A("O formato certo protege a clínica", "A escolha errada costuma aparecer anos depois, em uma ação trabalhista.", "Envie para o sócio da clínica"),
], """
Contratar um dentista como CLT, autônomo ou sócio não é só uma questão de custo.

CLT tem mais encargos e menos risco. Autônomo ou PJ reduz encargos, mas exige autonomia real: se houver horário imposto, subordinação e habitualidade, a relação pode ser reconhecida como vínculo de emprego. Sócio participa do risco e do resultado, e precisa de um contrato social bem estruturado.

O que define a relação é a prática, não o nome do contrato.

Salve e compartilhe com quem está montando a equipe da clínica.

#clinicaodontologica #gestaodeclinicas #contratacao #direitotrabalhista #contabilidade
"""),

img("2026-11-25", "simples-continua", {
    "theme": "navy", "chip": "Verdade",
    "title": "O *Simples Nacional* continua depois da Reforma",
    "text": "O regime segue existindo, com o DAS. A novidade é que, a partir de 2027, a empresa do Simples poderá optar por recolher IBS e CBS fora do DAS.",
    "box": "Essa opção pode fazer sentido para quem vende para outras empresas que aproveitam crédito.",
}, """
O Simples Nacional não acaba com a Reforma Tributária.

O regime continua, com recolhimento unificado no DAS. A novidade é que a empresa do Simples poderá optar por recolher IBS e CBS pelo regime regular, fora do DAS. Isso pode ser vantajoso para quem vende para outras empresas, porque permite transferir crédito integral ao cliente.

Para quem vende para o consumidor final, como a maioria das clínicas, a análise é outra.

Salve e acompanhe o próximo post, em que explicamos quando essa opção faz sentido.

#simplesnacional #reformatributaria #ibs #cbs
"""),

car("2026-11-26", "simples-das-ou-por-fora", [
    C("Simples na Reforma", "Ficar no DAS ou recolher IBS e CBS *por fora*?", "Uma decisão nova para empresas do Simples Nacional.", "Como pensar a escolha"),
    S("01", "No DAS", [("Como funciona", "IBS e CBS continuam dentro do recolhimento unificado do Simples."), ("O efeito no cliente", "Quem compra de você aproveita como crédito apenas o valor recolhido no DAS, que tende a ser menor.")]),
    S("02", "Por fora", [("Como funciona", "A empresa continua no Simples para os demais tributos, mas apura IBS e CBS pelo regime regular."), ("O efeito no cliente", "O cliente pessoa jurídica aproveita o crédito integral destacado na nota.")]),
    S("03", "Quando faz *sentido*", [("Recolher por fora", "Quando a maior parte dos clientes são empresas que aproveitam crédito."), ("Ficar no DAS", "Quando a empresa vende principalmente para consumidor final, como clínicas e varejo.")]),
    S("04", "O que *considerar*", ["Perfil de clientes, margem, créditos nas compras e custo de controle.", "A opção é semestral: em setembro, para o 1º semestre, e de 1º a 31 de março, para o 2º semestre. Quem optou em setembro de 2026 pode cancelar até 30/11."], box="Não existe resposta padrão. A decisão depende de simulação com os números da empresa."),
    A("Simule antes de escolher", "A empresa que vende para outras empresas pode perder clientes se não fizer essa conta.", "Envie para um empresário do Simples"),
], """
Com a Reforma Tributária, a empresa do Simples Nacional ganha uma escolha nova: manter IBS e CBS dentro do DAS ou recolher esses tributos pelo regime regular.

Dentro do DAS, o cliente pessoa jurídica aproveita como crédito apenas o valor recolhido no Simples. Por fora, o crédito é integral. Para quem vende para outras empresas, isso pode decidir uma negociação. Para quem vende para consumidor final, como clínicas, ficar no DAS tende a ser mais simples.

A opção é semestral. Para o 1º semestre de 2027, a janela foi setembro de 2026, com cancelamento possível até 30/11. Para o 2º semestre, a opção é feita de 1º a 31 de março de 2027. A decisão depende de simulação com os números reais.

Salve e envie para um empresário do Simples.

#simplesnacional #reformatributaria #ibs #cbs #planejamentotributario
"""),

car("2026-11-27", "black-friday-margem", [
    C("Comércio", "Black Friday *sem prejuízo*: faça esta conta antes", "Desconto que parece bom no caixa pode destruir a margem.", "4 passos para definir o desconto máximo"),
    S("01", "Descubra o *custo real*", ["Custo do produto, frete de compra, impostos sobre a venda, taxa do cartão ou da plataforma e comissão."]),
    S("02", "Calcule a *margem atual*", ["Preço de venda menos o custo real.", "Exemplo: produto vendido a R$ 100 com custo total de R$ 70 tem margem de R$ 30."]),
    S("03", "Defina o *limite*", ["Um desconto de 20% sobre R$ 100 tira R$ 20 da margem de R$ 30.", "Sobram R$ 10. Para lucrar o mesmo, você precisa vender três vezes mais unidades."]),
    S("04", "Escolha o *produto certo*", ["Concentre os maiores descontos em itens com margem alta ou em estoque parado.", "Proteja os produtos de margem baixa."], box="Desconto não é estratégia. Margem é."),
    A("Promoção boa é a que fecha a conta", "Revise hoje os preços antes de abrir as vendas.", "Envie para o dono da loja"),
], """
Hoje é Black Friday. Antes de aplicar qualquer desconto, faça uma conta simples.

Um produto vendido a R$ 100 com custo total de R$ 70 tem margem de R$ 30. Com 20% de desconto, a margem cai para R$ 10. Para lucrar o mesmo que antes, a loja precisa vender três vezes mais unidades.

Concentre os descontos maiores em produtos com margem alta ou em estoque parado, e proteja os itens de margem baixa. E lembre: desconto incondicional deve estar destacado na nota.

Salve e envie para quem define os preços da loja.

#blackfriday #comercio #margemdelucro #precificacao #varejo
"""),

img("2026-11-28", "o-que-e-dre", {
    "theme": "white", "kicker": "Em uma frase",
    "title": "O que é *DRE*?",
    "text": "É o relatório que mostra quanto a empresa faturou, quanto gastou e quanto sobrou de lucro em um período.",
    "box": "Faturamento mostra quanto entrou. A DRE mostra quanto ficou.",
}, """
DRE é a Demonstração do Resultado do Exercício.

Em uma frase: é o relatório que mostra quanto a empresa faturou, quanto gastou e quanto sobrou de lucro em um período. É ela que responde se o negócio está dando resultado, e não apenas movimentando dinheiro.

Se você nunca recebeu a DRE da sua empresa, peça ao seu contador.

Salve e compartilhe com quem está começando a empreender.

#dre #contabilidade #gestaofinanceira #empreendedorismo
"""),

car("2026-11-29", "margem-contribuicao", [
    C("Gestão financeira", "Margem de contribuição: o número que mostra o que *dá lucro*", "Nem todo serviço que vende bem contribui igual para o resultado.", "Explicado com um exemplo de clínica"),
    S("01", "O que é", ["É o quanto sobra de cada venda depois de pagar os custos variáveis dela: materiais, impostos sobre a receita, taxas de cartão e repasses."]),
    S("02", "Um *exemplo*", ["Procedimento A: R$ 400, com R$ 220 de custos variáveis. Margem de R$ 180.", "Procedimento B: R$ 250, com R$ 80 de custos variáveis. Margem de R$ 170."]),
    S("03", "A *leitura*", ["O procedimento A é mais caro, mas o B contribui quase o mesmo.", "Se o B leva menos tempo de cadeira, ele pode ser mais rentável por hora."]),
    S("04", "Como *usar*", ["Calcule a margem dos principais serviços ou produtos.", "Compare a margem por hora ou por unidade, e use isso para decidir onde investir em divulgação."], box="A margem de contribuição precisa cobrir os custos fixos. O que sobra depois disso é o lucro."),
    A("Conheça a margem de cada serviço", "É a base para precificar, divulgar e decidir o que manter.", "Envie para o sócio da clínica"),
], """
O serviço mais caro nem sempre é o que mais contribui para o lucro.

Margem de contribuição é o que sobra de cada venda depois de pagar os custos variáveis dela: materiais, impostos, taxas e repasses. Um procedimento de R$ 400 com R$ 220 de custos variáveis contribui com R$ 180. Um de R$ 250 com R$ 80 de custos contribui com R$ 170, e pode ser mais rentável se ocupar menos tempo.

Esse número ajuda a decidir preço, divulgação e quais serviços priorizar.

Salve e compartilhe com o sócio da clínica.

#margemdecontribuicao #gestaodeclinicas #gestaofinanceira #precificacao #contabilidade
"""),

img("2026-11-30", "alerta-13-hoje", {
    "theme": "orange", "kicker": "Vence hoje", "big": "HOJE", "bigsize": 220,
    "title": "Prazo final da *1ª parcela* do 13º salário",
    "text": "Metade do valor proporcional, sem descontos de INSS e IR. A 2ª parcela deve ser paga até 18/12, já que 20/12 cai em um domingo.",
}, """
Hoje, 30 de novembro, é o último dia para pagar a 1ª parcela do 13º salário.

O valor corresponde a metade do 13º proporcional, sem descontos de INSS e IR. A 2ª parcela vence em 20 de dezembro, mas como a data cai em um domingo, o pagamento deve ser feito até sexta-feira, 18/12.

Se ainda não pagou, regularize hoje para evitar multa.

Compartilhe com quem cuida da folha.

#13salario #departamentopessoal #prazos #contabilidade
"""),

car("2026-12-01", "checklist-dezembro", [
    C("Planejamento 2027", "Checklist de dezembro para *começar 2027* organizado", "O que fazer agora evita retrabalho e imposto a mais em janeiro.", "6 itens para conferir este mês"),
    S("01", "Revisar o *regime tributário*", ["Simule Simples, Presumido e Real com os números de 2026 e a projeção de 2027.", "Fora do Simples, a escolha entre Presumido e Real se confirma no primeiro pagamento de 2027. A entrada no Simples teve prazo em setembro."]),
    S("02", "Atualizar o *sistema de notas*", ["Confirme com o fornecedor se o emissor está preparado para IBS e CBS em 2027."]),
    S("03", "Planejar as *retiradas*", ["Defina pró-labore e distribuição de lucros de 2027 considerando as regras da Lei 15.270/2025."]),
    S("04", "Organizar a *folha*", ["13º, férias e encargos de dezembro no caixa.", "Revise salários e o reajuste previsto na convenção coletiva."]),
    S("05", "Conferir *certidões e cadastros*", ["Certidões negativas, certificado digital, alvarás e licenças com validade."]),
    S("06", "Inventário e *conciliação*", ["Empresas com estoque devem fazer o inventário em 31/12.", "Concilie extratos e contas a receber antes do fechamento."], box="Um dezembro organizado é o que permite um balanço confiável e decisões melhores em 2027."),
    A("Use como lista de tarefas", "Marque cada item ao longo do mês. Os mais urgentes são o regime e o sistema de notas.", "Envie para o seu sócio"),
], """
Dezembro é o mês que define como a empresa começa o ano seguinte.

Seis itens para conferir: regime tributário de 2027, atualização do sistema de notas para IBS e CBS, planejamento das retiradas dos sócios, folha de dezembro, validade de certidões e certificado digital, e inventário com conciliação para quem tem estoque.

Os dois mais urgentes são o regime e o sistema de notas, porque dependem de decisão antes de janeiro.

Salve como lista de tarefas e compartilhe com o seu sócio.

#planejamentotributario #fechamentodeano #gestaoempresarial #reformatributaria #contabilidade
"""),

img("2026-12-02", "frase-contador-decidir", {
    "theme": "light", "kicker": "Nossa visão",
    "title": "Seu contador deveria te ajudar a *decidir*, não só avisar o que pagar.",
    "text": "Contratar, investir, retirar lucro, mudar de regime. Todas essas decisões passam pelos números da empresa.",
}, """
A guia de imposto é a parte mais visível da contabilidade, mas não é a mais importante.

Contratar, investir, retirar lucro, mudar de regime, abrir uma filial: todas essas decisões dependem dos números da empresa. O contador que só aparece no vencimento da guia deixa o empresário decidindo sozinho.

É esse o papel que a Smartcontax assume com cada cliente.

Compartilhe com quem pensa da mesma forma.

#contabilidadeconsultiva #gestaoempresarial #contabilidade
"""),

car("2026-12-03", "saude-reducao-60", [
    C("Reforma para clínicas", "Saúde terá *redução de 60%* no IBS e na CBS", "O benefício existe, mas não é automático para toda clínica.", "O que você precisa saber"),
    S("01", "O que a lei *prevê*", ["A LC 214/2025 reduz em 60% as alíquotas de IBS e CBS para os serviços de saúde listados em anexo da própria lei."]),
    S("02", "Para *quem* vale", ["Para os serviços listados, conforme a classificação do serviço prestado.", "O enquadramento depende do serviço, não apenas do tipo de clínica."]),
    S("03", "E no *Simples*?", ["Empresas do Simples Nacional seguem recolhendo pelo DAS, com as regras próprias do regime.", "A redução de 60% se aplica ao regime regular de IBS e CBS."]),
    S("04", "O que *conferir*", ["Se os serviços da clínica estão na lista do anexo.", "Se o cadastro e a classificação das notas fiscais estão corretos."], box="Clínica veterinária: verifique o enquadramento separadamente, porque a regra aplicável pode ser outra."),
    A("Confira o enquadramento da sua clínica", "Benefício aplicado ao serviço errado vira cobrança depois.", "Envie para o sócio da clínica"),
], """
A Reforma Tributária prevê redução de 60% nas alíquotas de IBS e CBS para serviços de saúde. Mas o benefício não é automático para qualquer clínica.

A LC 214/2025 lista em anexo os serviços que têm direito à redução, e o enquadramento depende do serviço prestado, não apenas do tipo de empresa. Para clínicas do Simples Nacional, o recolhimento continua pelo DAS. Clínicas veterinárias devem conferir o enquadramento separadamente.

O primeiro passo é revisar a classificação dos serviços nas notas fiscais.

Salve e envie para o sócio da clínica.

#reformatributaria #clinicas #saude #ibs #cbs
"""),

car("2026-12-04", "confraternizacao-brindes", [
    C("Fim de ano", "Confraternização e brindes: o que a lei *permite*", "Cuidados fiscais com as despesas de dezembro.", "Depende do regime da sua empresa"),
    S("01", "Simples e *Presumido*", ["Nesses regimes, o imposto é calculado sobre o faturamento.", "As despesas não reduzem o IR, mas precisam ser da empresa e estar documentadas."]),
    S("02", "Lucro Real: *brindes*", ["Brindes são indedutíveis para IRPJ e CSLL, conforme a Lei 9.249/1995.", "O gasto pode ser feito, mas não reduz o imposto."]),
    S("03", "Lucro Real: *equipe*", ["Despesas com confraternização dos funcionários tendem a ser aceitas quando ligadas à atividade, oferecidas a todos e bem documentadas."]),
    S("04", "Em *qualquer* regime", ["Exija nota fiscal em nome da empresa.", "Não misture despesas pessoais dos sócios com despesas da empresa."], box="Despesa sem documento ou sem relação com a atividade pode ser glosada em fiscalização."),
    A("Celebre com segurança", "Nota fiscal em nome da empresa é o mínimo para qualquer despesa de fim de ano.", "Envie para quem organiza a festa"),
], """
Confraternização da equipe e brindes para clientes são despesas comuns em dezembro, e o tratamento fiscal depende do regime da empresa.

No Simples e no Presumido, o imposto é calculado sobre o faturamento, então as despesas não reduzem o IR, mas precisam ser da empresa e estar documentadas. No Lucro Real, brindes são indedutíveis conforme a Lei 9.249/1995, enquanto despesas com a equipe tendem a ser aceitas quando oferecidas a todos e bem documentadas.

Em qualquer regime: nota fiscal em nome da empresa e nada de despesa pessoal no meio.

Salve e compartilhe com quem está organizando o fim de ano.

#fimdeano #lucroreal #despesasdedutiveis #gestaoempresarial #contabilidade
"""),

]
