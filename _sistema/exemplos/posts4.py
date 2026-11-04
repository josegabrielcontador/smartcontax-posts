from helpers import *

POSTS = [

car("2026-12-20", "taxas-cartao", [
    C("Gestão financeira", "Taxas de cartão: o custo que *ninguém revisa*", "Pequenos percentuais sobre todo o faturamento viram um valor relevante no ano.", "4 pontos para conferir na maquininha"),
    S("01", "Taxa por *modalidade*", ["Débito, crédito à vista e parcelado têm taxas diferentes.", "Confira se o que está no extrato é o que foi contratado."]),
    S("02", "Antecipação", ["Receber antes do prazo tem custo, que funciona como juros sobre o valor antecipado.", "Antecipação automática costuma estar ativada sem que o dono saiba."]),
    S("03", "Parcelamento *sem juros*", ["Quando a clínica ou loja parcela sem juros, quem paga a taxa do parcelamento é a empresa.", "Esse custo precisa estar no preço."]),
    S("04", "Faça a *conta anual*", ["Some todas as taxas pagas no ano e compare com o faturamento no cartão.", "Com esse número em mãos, negocie ou compare com outras empresas de pagamento."], box="Taxa de cartão é custo variável e precisa entrar no cálculo da margem de cada venda."),
    A("Revise o contrato da maquininha", "Uma renegociação pode render mais que muitos cortes de despesa.", "Envie para quem cuida do financeiro"),
], """
A taxa de cartão parece pequena porque é cobrada em percentual. Somada ao longo do ano, sobre todo o faturamento, costuma virar um dos maiores custos variáveis da empresa.

Confira se as taxas por modalidade correspondem ao contrato, se a antecipação automática está ativada sem necessidade e se o custo do parcelamento sem juros está no preço. Depois, some as taxas pagas no ano e use o número para negociar.

Salve e envie para quem cuida do financeiro.

#taxasdecartao #gestaofinanceira #margemdelucro #fluxodecaixa #contabilidade
"""),

car("2026-12-21", "saida-de-socio", [
    C("Societário", "Sócio saindo da empresa: o que *formalizar*", "Saída sem documentação gera conflito e responsabilidade anos depois.", "4 etapas para uma saída segura"),
    S("01", "Alteração *contratual*", ["A saída precisa ser registrada por alteração do contrato social na Junta Comercial.", "Até o registro, o sócio continua aparecendo como integrante da empresa."]),
    S("02", "Apuração de *haveres*", ["É o cálculo do valor que o sócio que sai tem a receber.", "Deve seguir o que diz o contrato social, normalmente com base em um balanço levantado na data da saída."]),
    S("03", "Forma de *pagamento*", ["Prazo, parcelas e garantias devem estar por escrito.", "O pagamento impacta o caixa e precisa ser planejado."]),
    S("04", "Responsabilidade", ["Pelo Código Civil, o sócio que se retira continua respondendo pelas obrigações sociais anteriores por até 2 anos após a averbação da saída."], box="Contas bancárias, procurações, certificados digitais e cadastros também precisam ser atualizados."),
    A("Saída bem feita protege os dois lados", "Envolva o contador e o advogado antes de assinar qualquer acordo.", "Envie para quem está passando por isso"),
], """
A saída de um sócio é um dos momentos mais delicados de uma empresa, e o que não é formalizado costuma virar conflito.

Quatro etapas: alteração do contrato social registrada na Junta Comercial, apuração de haveres conforme o contrato social, forma de pagamento definida por escrito e atenção à responsabilidade. Pelo Código Civil, o sócio que sai continua respondendo pelas obrigações anteriores por até 2 anos após a averbação.

Também é preciso atualizar contas bancárias, procurações, certificados e cadastros.

Salve e compartilhe com quem está passando por isso.

#societario #saidadesocio #contratosocial #gestaoempresarial #contabilidade
"""),

img("2026-12-22", "institucional-onde-voce-esta", {
    "theme": "navy", "kicker": "Como trabalhamos",
    "title": "Contabilidade *100% digital*, com um contador *presente*",
    "text": "• Atendimento por WhatsApp e videochamada\n• Visitas à sua empresa quando necessário\n• Foco em clínicas e comércio",
    "box": "Você não precisa ir até um escritório para ter um contador perto.",
}, """
Na Smartcontax, a contabilidade é 100% digital, mas o atendimento é próximo.

Falamos por WhatsApp e videochamada, e vamos até a sua empresa quando faz sentido. Atendemos clínicas odontológicas, médicas e veterinárias e empresas do comércio, com foco em clareza nos números e segurança fiscal.

Quer conhecer melhor? Fale com a gente pelo link da bio.

#contabilidadedigital #contabilidadeconsultiva #clinicas #smartcontax
"""),

img("2026-12-23", "das-dezembro-janeiro", {
    "theme": "light", "kicker": "Recesso não é pausa fiscal",
    "title": "O DAS de *dezembro* vence em *20 de janeiro*",
    "text": "Os tributos sobre o faturamento de dezembro são pagos no mês seguinte. O caixa de janeiro precisa estar preparado.",
    "box": "Dezembro costuma ter faturamento maior, e o imposto acompanha esse aumento.",
}, """
Os impostos sobre o faturamento de dezembro vencem em janeiro.

No Simples Nacional, o DAS de dezembro vence em 20 de janeiro de 2027. Nos demais regimes, os tributos também são pagos no mês seguinte, com datas próprias. Como dezembro costuma ter faturamento maior, o imposto de janeiro tende a ser maior também, justamente quando o caixa já foi pressionado por 13º, férias e despesas de fim de ano.

Reserve o valor ainda em dezembro.

Salve e compartilhe com quem cuida do financeiro.

#simplesnacional #das #fluxodecaixa #prazos #contabilidade
"""),

car("2026-12-24", "3-perguntas-2027", [
    C("Planejamento", "3 perguntas para fazer *antes de 2027*", "Planejamento começa com perguntas certas, não com planilhas.", "Responda com seu sócio"),
    S("01", "Para onde a empresa vai se *nada mudar*?", ["Projete o próximo ano com o mesmo ritmo de vendas, custos e retiradas.", "Se o resultado não agrada, algo precisa mudar agora."]),
    S("02", "Qual decisão foi *adiada* em 2026?", ["Contratar, trocar de regime, reajustar preços, separar contas, encerrar um serviço que não dá lucro.", "Decisão adiada também tem custo."]),
    S("03", "Que número você quer *acompanhar*?", ["Escolha um ou dois indicadores para olhar todo mês em 2027: margem, caixa, ticket médio ou ocupação."], box="Escreva as respostas. Decisão que fica só na cabeça raramente vira ação em janeiro."),
    A("Comece 2027 com clareza", "Três respostas honestas valem mais que um planejamento longo que ninguém segue.", "Envie para o seu sócio"),
], """
Antes de montar qualquer planilha para 2027, responda três perguntas com o seu sócio.

Para onde a empresa vai se nada mudar? Qual decisão importante foi adiada em 2026? Que número você vai acompanhar todo mês no próximo ano?

As respostas mostram o que precisa ser feito em janeiro. E escreva: decisão que fica só na cabeça raramente vira ação.

Salve e compartilhe com o seu sócio.

#planejamento #gestaoempresarial #metas2027 #empreendedorismo
"""),

img("2026-12-25", "natal", {
    "theme": "navy", "kicker": "25 de dezembro",
    "title": "Feliz *Natal*",
    "text": "Obrigado aos clientes, parceiros e seguidores que confiaram na Smartcontax em 2026. Que este dia seja de descanso e de tempo com quem importa.",
    "foot": "Equipe Smartcontax",
}, """
Hoje o perfil faz uma pausa no conteúdo técnico.

Obrigado aos clientes, parceiros e seguidores que confiaram na Smartcontax em 2026. Que o dia seja de descanso e de tempo com quem importa.

Feliz Natal.

#feliznatal #smartcontax
"""),

car("2026-12-26", "retrospectiva-2026", [
    C("Retrospectiva", "As mudanças fiscais de *2026* que afetam 2027", "Um ano de muitas novidades para empresas e sócios.", "5 pontos para ter em mente"),
    S("01", "Teste da *Reforma*", ["Em 2026, CBS e IBS foram destacados nas notas com alíquotas de teste.", "Em 2027, a CBS passa a ser cobrada."]),
    S("02", "IR sobre *dividendos*", ["A Lei 15.270/2025 criou retenção de 10% sobre lucros acima de R$ 50 mil por mês para a mesma pessoa física."]),
    S("03", "Imposto *mínimo* anual", ["Pessoas físicas com renda total acima de R$ 600 mil no ano passaram a ter tributação mínima."]),
    S("04", "Isenção do IR na *folha*", ["Pela mesma lei, rendimentos mensais até R$ 5 mil ficaram isentos de IR, com redução parcial para faixas próximas."]),
    S("05", "Notas fiscais", ["Os documentos fiscais passaram a exigir novos campos e classificações ligados à Reforma."], box="Todas essas mudanças afetam o planejamento de 2027: regime, retiradas, folha e sistemas."),
    A("Use 2026 como base para planejar", "O que mudou neste ano define as decisões do próximo.", "Envie para o seu sócio"),
], """
2026 foi um ano de mudanças importantes para empresas e sócios.

A Reforma Tributária entrou em fase de teste, com CBS e IBS destacados nas notas. A Lei 15.270/2025 trouxe retenção de 10% sobre lucros acima de R$ 50 mil por mês para a mesma pessoa física, imposto mínimo para rendas acima de R$ 600 mil no ano e isenção de IR para rendimentos mensais até R$ 5 mil. E os sistemas de notas precisaram se adaptar.

Tudo isso pesa nas decisões de 2027.

Salve e compartilhe com o seu sócio.

#retrospectiva2026 #reformatributaria #lei15270 #impostoderenda #contabilidade
"""),

img("2026-12-27", "ipi-zero-2027", {
    "theme": "white", "kicker": "Reforma Tributária",
    "title": "IPI com alíquota *zero* a partir de 2027",
    "text": "A regra vale para a maioria dos produtos. A exceção são os produtos com industrialização incentivada na Zona Franca de Manaus.",
    "box": "Para o comércio, vale revisar preços de compra e o custo dos produtos com os fornecedores.",
}, """
A partir de 2027, o IPI passa a ter alíquota zero para a maioria dos produtos. A exceção são os produtos com industrialização incentivada na Zona Franca de Manaus.

Para o comércio, isso pode mudar o custo de compra de alguns produtos. Vale conversar com os fornecedores e revisar preços e margens no início do ano.

Salve e acompanhe os próximos posts sobre a virada da Reforma.

#ipi #reformatributaria #comercio #varejo
"""),

car("2026-12-28", "cronograma-reforma", [
    C("Reforma Tributária", "O cronograma da Reforma de *2026 a 2033*", "A transição é longa. Saber onde estamos evita decisões precipitadas.", "Linha do tempo em 4 etapas"),
    S("01", "2026: *teste*", ["CBS com 0,9% e IBS com 0,1% destacados nas notas, em caráter de teste.", "Os tributos atuais continuaram valendo normalmente."]),
    S("02", "2027 e 2028: *CBS*", ["A CBS substitui PIS e Cofins e o IPI é zerado para a maioria dos produtos. O Imposto Seletivo está previsto para começar.", "O IBS segue com alíquota reduzida, de transição."]),
    S("03", "2029 a 2032: *transição*", ["ICMS e ISS são reduzidos gradualmente, ano a ano, enquanto o IBS aumenta na mesma proporção."]),
    S("04", "2033: *modelo final*", ["ICMS e ISS deixam de existir.", "O sistema passa a funcionar com IBS, CBS e Imposto Seletivo."], box="Cada etapa exige ajustes em preço, sistemas e regime. O planejamento precisa acompanhar o calendário."),
    A("Salve para consultar ao longo dos anos", "A Reforma vai estar no seu planejamento até 2033.", "Envie para quem precisa entender a transição"),
], """
A Reforma Tributária tem uma transição longa, e saber em que etapa estamos evita decisões precipitadas.

2026 foi o ano de teste. Em 2027 e 2028, a CBS substitui PIS e Cofins, o IPI é zerado para a maioria dos produtos, o Imposto Seletivo está previsto para começar e o IBS segue com alíquota reduzida. De 2029 a 2032, ICMS e ISS caem gradualmente enquanto o IBS sobe. Em 2033, o modelo final entra em vigor.

Salve para consultar ao longo dos próximos anos.

#reformatributaria #ibs #cbs #impostoseletivo #contabilidade
"""),

car("2026-12-29", "orcamento-anual", [
    C("Planejamento 2027", "Como montar o *orçamento* da empresa para 2027", "Um orçamento simples já muda a qualidade das decisões do ano.", "5 passos práticos"),
    S("01", "Projete a *receita*", ["Parta do faturamento de 2026, mês a mês.", "Considere sazonalidade, reajustes de preço e a capacidade real de atendimento."]),
    S("02", "Liste os *custos fixos*", ["Aluguel, folha, pró-labore, sistemas, contabilidade e contratos.", "Inclua reajustes previstos para o ano."]),
    S("03", "Estime os *variáveis*", ["Materiais, impostos sobre a receita, taxas de cartão e repasses, em percentual da receita."]),
    S("04", "Separe os *investimentos*", ["Equipamentos, reformas, marketing e contratações planejadas, com o mês previsto."]),
    S("05", "Acompanhe todo *mês*", ["Compare o realizado com o orçado e ajuste a rota a cada trimestre."], box="Orçamento não é previsão perfeita. É uma referência para perceber cedo quando algo sai do esperado."),
    A("Planeje com números reais", "Use a contabilidade de 2026 como base, não estimativas de memória.", "Envie para o seu sócio"),
], """
Um orçamento simples já muda a forma como a empresa toma decisões ao longo do ano.

Projete a receita mês a mês a partir de 2026, liste os custos fixos com reajustes, estime os custos variáveis em percentual da receita, separe os investimentos com o mês previsto e compare o realizado com o orçado todo mês.

O orçamento não precisa acertar tudo. Ele existe para mostrar cedo quando algo sai do esperado.

Salve e compartilhe com o seu sócio.

#orcamento #planejamento2027 #gestaofinanceira #gestaoempresarial #contabilidade
"""),

img("2026-12-30", "inventario-31-12", {
    "theme": "navy", "kicker": "Empresas com estoque", "big": "31/12", "bigsize": 230,
    "title": "Dia de fazer o *inventário* do estoque",
    "text": "A contagem física do estoque no último dia do ano é base para o balanço e para o livro Registro de Inventário.",
    "foot": "Comércio e indústria",
}, """
Amanhã, 31 de dezembro, é o dia do inventário para empresas com estoque.

A contagem física dos produtos no último dia do ano é base para o balanço, para o cálculo do custo das mercadorias vendidas e para o livro Registro de Inventário. Estoque contado errado distorce o lucro do ano e pode gerar divergências fiscais.

Organize a equipe e envie a contagem ao seu contador.

Salve e compartilhe com quem cuida do estoque.

#inventario #estoque #comercio #fechamentodeano #contabilidade
"""),

img("2026-12-31", "ano-novo", {
    "theme": "orange", "kicker": "31 de dezembro",
    "title": "Que *2027* seja um ano de decisões *mais claras*",
    "text": "Obrigado por acompanhar a Smartcontax. Seguimos juntos no próximo ano, com conteúdo de segunda a sexta.",
    "foot": "Equipe Smartcontax",
}, """
Último dia de 2026.

Obrigado por acompanhar o perfil, compartilhar os conteúdos e confiar no nosso trabalho. Em 2027 seguimos com conteúdo de segunda a sexta sobre impostos, gestão e Reforma Tributária.

Que o próximo ano seja de decisões mais claras para a sua empresa.

#anonovo #2027 #smartcontax
"""),

img("2027-01-01", "2027-comecou-cbs", {
    "theme": "navy", "kicker": "Reforma Tributária", "big": "2027", "bigsize": 220,
    "title": "Desde 1º de janeiro, a *CBS* passou a ser cobrada",
    "text": "PIS e Cofins deixam de existir para empresas fora do Simples. O IPI é zerado para a maioria dos produtos, e o IBS segue com alíquota reduzida.",
    "foot": "LC 214/2025",
}, """
Desde 1º de janeiro, a Reforma Tributária pesa no caixa das empresas.

A CBS substitui PIS e Cofins para empresas fora do Simples Nacional. O IPI é zerado para a maioria dos produtos, exceto os incentivados na Zona Franca de Manaus, e o Imposto Seletivo está previsto para começar, com alíquotas ainda em definição. O IBS segue com alíquota reduzida, e ICMS e ISS continuam valendo.

Nas próximas semanas, acompanhe aqui como essas mudanças aparecem na prática.

#reformatributaria #cbs #2027 #contabilidade
"""),

car("2027-01-02", "opcao-simples-setembro", [
    C("Simples Nacional", "A opção pelo Simples *mudou de data*", "Quem ainda espera janeiro para entrar no regime pode perder o ano inteiro.", "O que a LC 214/2025 alterou"),
    S("01", "O novo *prazo*", ["Para empresas já em atividade, a opção pelo Simples passou a ser feita de 1º a 30 de setembro.", "A opção feita em setembro vale a partir de 1º de janeiro do ano seguinte."]),
    S("02", "Janeiro *acabou*", ["Não há mais período de opção em janeiro para CNPJs já constituídos.", "Quem perdeu setembro de 2026 só pode entrar no Simples para 2028."]),
    S("03", "IBS e CBS *por fora*", ["Também é em setembro que a empresa do Simples escolhe recolher IBS e CBS pelo regime regular, com efeitos no semestre seguinte."]),
    S("04", "O que *muda* no planejamento", ["A simulação de regime precisa estar pronta no meio do ano, não em dezembro.", "Para 2028, a decisão será tomada em setembro de 2027."], box="Empresas em início de atividade seguem regras próprias de prazo. Confira o seu caso com o contador."),
    A("Anote setembro no calendário", "A decisão de regime saiu do começo do ano e foi para o segundo semestre.", "Envie para quem ainda pensa que o prazo é janeiro"),
], """
Muita gente ainda acredita que a opção pelo Simples Nacional é feita em janeiro. Não é mais.

Com a LC 214/2025, empresas já em atividade passaram a fazer a opção de 1º a 30 de setembro, com efeitos a partir de 1º de janeiro do ano seguinte. Para 2027, o prazo terminou em 30/09/2026, e não há período de opção em janeiro para CNPJs já constituídos.

Na prática, o planejamento de regime precisa acontecer no meio do ano. Para 2028, a decisão será tomada em setembro de 2027. Empresas em início de atividade seguem regras próprias.

Salve e envie para quem ainda pensa que o prazo é janeiro.

#simplesnacional #regimetributario #lc214 #planejamentotributario #contabilidade
"""),

car("2027-01-03", "decisoes-janeiro", [
    C("Começo de ano", "5 decisões que *não podem esperar* fevereiro", "Janeiro define boa parte do resultado do ano.", "Confira se a sua empresa já resolveu"),
    S("01", "Regime tributário", ["Fora do Simples, a escolha entre Presumido e Real se confirma com o primeiro pagamento do ano. A análise precisa estar feita antes dele."]),
    S("02", "Pró-labore e *retiradas*", ["Definir valores para 2027, considerando o Fator R e as regras de distribuição de lucros."]),
    S("03", "Preços", ["Revisar preços com base em custos reajustados, taxas de cartão e efeitos da CBS para quem está fora do Simples."]),
    S("04", "Sistemas", ["Confirmar que as notas emitidas em janeiro estão com IBS e CBS corretos."]),
    S("05", "Metas", ["Definir os indicadores que serão acompanhados todo mês e quem é responsável por cada um."], box="Uma reunião de 1 hora com o seu contador em janeiro pode evitar meses de ajustes."),
    A("Resolva em janeiro", "Cada mês de atraso em uma decisão tributária é um mês pagando pelo caminho errado.", "Envie para o seu sócio"),
], """
Janeiro concentra decisões que definem o resultado do ano inteiro.

Regime tributário, para quem está no Presumido ou no Real, que confirmam a escolha no primeiro pagamento do ano. Pró-labore e retiradas para 2027. Revisão de preços com custos reajustados e os efeitos da CBS. Conferência das notas emitidas no novo modelo. E definição dos indicadores que serão acompanhados.

Uma reunião de 1 hora com o contador em janeiro pode evitar meses de ajustes.

Salve e compartilhe com o seu sócio.

#planejamento2027 #regimetributario #gestaoempresarial #reformatributaria #contabilidade
"""),

car("2027-01-04", "como-trabalhamos-raio-x", [
    C("Smartcontax", "Como começamos a trabalhar com *uma nova empresa*", "Antes de qualquer proposta, entendemos os números.", "As 4 etapas do nosso processo"),
    S("01", "Conversa *inicial*", ["Entendemos a atividade, o momento da empresa e o que mais preocupa os sócios.", "Por WhatsApp, videochamada ou presencialmente."]),
    S("02", "Diagnóstico", ["Analisamos regime tributário, enquadramento, folha e obrigações em dia.", "Apontamos riscos e oportunidades com base nos números reais."]),
    S("03", "Raio-X da *Reforma*", ["Para clínicas, simulamos o impacto da Reforma Tributária em três cenários.", "Você sabe o que muda antes de a mudança chegar ao caixa."]),
    S("04", "Acompanhamento", ["Contabilidade, fiscal e folha em dia, com atendimento próximo e orientação para as decisões do negócio."], box="O Raio-X da Reforma para clínicas é gratuito. Peça pelo link da bio."),
    A("Comece pelo diagnóstico", "Decisão boa começa com informação certa. Fale com a Smartcontax pelo link da bio.", "Envie para um colega dono de clínica"),
], """
Antes de qualquer proposta, a Smartcontax começa pelos números.

O processo tem quatro etapas: conversa inicial para entender a empresa, diagnóstico de regime, enquadramento, folha e obrigações, Raio-X da Reforma Tributária para clínicas, com simulação em três cenários, e acompanhamento contínuo com atendimento próximo.

O Raio-X da Reforma para clínicas é gratuito. Para pedir o seu, fale com a gente pelo link da bio.

Salve e envie para um colega dono de clínica.

#contabilidadeparaclinicas #reformatributaria #diagnosticotributario #contabilidadeconsultiva #smartcontax
"""),

]
